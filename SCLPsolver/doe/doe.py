# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import numpy as np
from functools import partial
from math import sin, pi
from .data_generators.MCQN import generate_MCQN_data, perturb_MCQN_data
from .data_generators.reentrant import generate_reentrant_data
from .data_generators.write_CPLEX_dat import write_CPLEX_dat
from .data_generators.simple_reentrant import generate_simple_reentrant_data
from .doe_utils import path_utils
from SCLP import SCLP, SCLP_settings


def sin_uncertainty(h: float, height: float, width: float, amps: list, freqs: list, shifts: list, t: float):
    """Generate a sine-based continuous uncertainty function of time, centered around h
    and evaluate it at t.

    Parameters
    ----------
    h: float
        The true point.
    height:
        The total height of the uncertainty.
    width: float
        The width of the time interval.
    amps: list
        The amplitudes of each sine function.
    freqs: list
        The frequencies of each sine function.
    shifts: list
        The amount to shift the sin functions.
    t: float
        The time to
    Returns
    -------
    float
        The random function evaluated at t
    """
    k = len(amps)
    if k != len(freqs):
        raise RuntimeError("amps and freqs parameters must have same length")
    if k != len(shifts):
        raise RuntimeError("amps and shifts parameters must have same length")
    return h * (1 + 0.5*height) + 0.5 * sum([amps[i] * sin(freqs[i] * pi * t / width + shifts[i]) for i in range(k)])

# 1. This implemntation defined as \tau(t) = \overline{\tau} + \tilde{\tau}\theta(t), where \tilde{\tau} =
#      perturbation[1] \overline{\tau} and \overline{\tau} are non-zero entries of H. We also need
#      consider perturbation of \mu  = \overline{\mu} + \tilde{\mu}\theta(t) where \tilde{\mu} =  perturbation[1] \overline{\mu}
#      and \overline{\mu} = 1/\overline{\tau}
#  2. For both cases we should implement uncertainty budget - it will be parameter \Gamma: vector of dimension I (number of rows
#       in matrix H). Generated functions should satisfy \sum_{j:s(i)=j} \tilde{\tau}\theta(t) \le \Gamma_i \sum_{j:s(i)=j} \tilde{\tau}
#       and similar for \mu
#  3. Please make "uncertain" function to be parameter and define it separately in this file... default value of this parameter
#       will be your "uncertain" function.
def gen_uncertain_param(params: np.ndarray, domain: tuple, perturbation: tuple,
                        uncertain_func = sin_uncertainty, k: int = 4, seed: int = None) -> np.ndarray:
    """Generate functions for producing the "uncertain" values of parameters.

    This function takes a vector/matrix of parameters and
    generates corresponding continuous functions that are
    a random distance away from the original parameters.
    The functions each take the time value from the domain
    parameter and produce an output in the range.
    The result will be an np.ndarray of such functions.
    The shape of the resulting array is the same as
    the shape of the input parameter.

    Parameters
    ----------
    params : np.ndarray of numbers
        The parameters which will be randomized over time. For each 0 value, the 0 function will be generated.
    domain : tuple of int
        The time domain of the functions
    perturbation : tuple of numbers
        The relative amount to perturb the output range of the functions.
        For example, (0, 0.1) will perturb the parameters 10% on the upside.
    uncertain_func: function
        Function that generates uncertainty functions of time.
        Must accept parameters h, height, width, amps, freqs, shifts, t.
        Default is sin_uncertainty(h, height, width, amps, freqs, shifts, t).
    k: int
        The number of sine wave perturbations. Default is 4.
    seed: int
        Random number generator seed or None (default).

    Returns
    -------
    np.ndarray
        Functions from the domain to the range,
        randomly perturbed from the input.
    """
    if seed:
        np.random.seed(seed)
    shape = params.shape
    left, right = domain
    width = right - left
    result = np.empty(shape, dtype=object)
    perturb_low, perturb_high = perturbation
    height = perturb_high - perturb_low

    for index, h in np.ndenumerate(params):
        if h == 0:
            result[index] = lambda t: 0
        else:
            result[index] = partial(uncertain_func, h, height, width, [h*height/k] * k, range(1,k+1), np.random.uniform(0, 2*pi, k))

    return result


def run_experiment_series(exp_type, exp_num, K, I, T, settings, starting_seed = 1000, solver_settings = None,
                          use_adaptive_T = False, get_raw_tau = True, **kwargs):
    failure_trials = 0
    ps = {'K':K,'I':I,'T':T}
    for k, v in kwargs.items():
        ps[k] = v
    for k,v in settings.items():
        if isinstance(v, object) and hasattr(v, '__name__'):
            ps[k] = v.__name__[:4]
        else:
            ps[k] = str(v)
    #pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
    pu = path_utils("C:/DataD/SCLP_data")
    results = []
    files = []
    if get_raw_tau:
        raw_tau = []
    else:
        raw_tau = None
    for seed in range(starting_seed, starting_seed + exp_num):
        ps['seed'] = seed
        if exp_type == 'MCQN':
            G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)
        elif exp_type == 'reentrant':
            G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_reentrant_data(seed, K, I, **settings)
        elif exp_type == 'simple_reentrant':
            G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_simple_reentrant_data(seed, K, I, **settings)
        else:
            raise Exception('Undefined experiment type!')
        if T is None:
            if TT is None:
                raise Exception('Undefined time horizon!')
            else:
                T = TT
        if solver_settings is None:
            solver_settings = SCLP_settings(find_alt_line=False)
        solver_settings.file_name = pu.get_tmp_data_file_name(exp_type)
        import time
        start_time = time.time()
        solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, T, solver_settings)
        t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(False)
        time_to_solve = time.time() - start_time
        print(obj, err, solution.last_T, maxT)
        print("--- %s seconds ---" % time_to_solve)
        print("--- seed %s ---" % seed)
        Tres  = param_line.T
        if res == 0 or use_adaptive_T:
            if res != 0:
                ps['T'] = 'adpt'
            else:
                ps['T'] = T
            full_file_name = pu.get_CPLEX_data_file_name(exp_type, **ps)
            write_CPLEX_dat(full_file_name, Tres, G, H, alpha, a, b, gamma, c, buffer_cost)
            path, filename = os.path.split(full_file_name)
            buf_cost = total_buffer_cost[0]*Tres+total_buffer_cost[1]*Tres*Tres/2.0
            r = {'file': filename, 'seed': seed, 'result': res, 'objective': obj, 'time': time_to_solve,'steps': STEPCOUNT,
                 'intervals': NN, 'T': Tres, 'maxT': maxT, 'mean_tau': np.mean(tau), 'max_tau': np.max(tau), 'min_tau':np.min(tau),
                 'std_tau':np.std(tau), 'buffer_cost': buf_cost, 'real_objective':buf_cost - obj}
            results.append(r)
            if get_raw_tau:
                raw_tau.append({'file': filename,'raw_tau':tau})
            files.append(full_file_name)
        else:
            failure_trials +=1
    return results, failure_trials, files, raw_tau


def run_experiment_perturbation(exp_type, exp_num, K, I, T, settings, rel_perturbation, symmetric, starting_seed = 1000, solver_settings = SCLP_settings(),
                                use_adaptive_T = False, get_raw_tau = True, **kwargs):

    num_feasible = 0
    true_objective = float("inf")
    perturbed_obj_vals = list()

    # 1. generate the "true" MCQN data
    G0, H0, F0, gamma0, c0, d0, alpha0, a0, b0, TT0, buffer_cost0, xcost0 = generate_MCQN_data(starting_seed, K, I, **settings)

    # 2. Solve using SCLP
    solution0, STEPCOUNT0, param_line0, res0 = SCLP(G0, H0, F0, a0, b0, c0, d0, alpha0, gamma0, T, solver_settings)
    t, x, q, u, p, pivots, obj, err, NN, tau, maxT= solution0.get_final_solution()
    if True:
        true_objective = obj

    for seed in range(starting_seed+1, starting_seed + 1 + exp_num):

        print("\n\n\n==============")
        print(seed)
        print("==============\n\n\n")

        # 3. Perturb the MCQN data
        G, H, F, a, b, c, d, alpha, gamma = perturb_MCQN_data(seed, rel_perturbation, symmetric, G0, H0, F0, a0, b0, c0, d0, alpha0, gamma0)

        # 4. Solve the SCLP with perturbed MCQN
        solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, T, solver_settings)

        # 5. Test
        # a. Check if the "true" values are feasible under perturbation
        is_feasible = solution.is_other_feasible(solution0)
        num_feasible += int(is_feasible)

        # b. Assuming feasibility, get the objective value of the "true" solution under the perturbation
        if is_feasible:
            perturbed_obj_vals.append(solution.other_objective(solution0))

    return num_feasible, true_objective, perturbed_obj_vals

def run_experiment_randomized():
    return 0