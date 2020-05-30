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
from .data_generators.MCQN import generate_MCQN_data, perturb_MCQN_data
from .data_generators.reentrant import generate_reentrant_data
from .data_generators.MCQN_routing1 import generate_MCQN_routing_data
from .data_generators.write_CPLEX_dat import write_CPLEX_dat
from .data_generators.simple_reentrant import generate_simple_reentrant_data
from .doe_utils import path_utils
from SCLP import SCLP, SCLP_settings


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
        elif exp_type == 'MCQN_routing':
            G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_routing_data(seed, K, I, **settings)
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

