import os
import numpy as np
from .data_generators.MCQN import generate_MCQN_data
from .data_generators.reentrant import generate_reentrant_data
from .data_generators.MCQN_routing import generate_MCQN_routing_data
from .data_generators.write_CPLEX_dat import write_CPLEX_dat
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
    pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
    results = []
    files = []
    if get_raw_tau:
        raw_tau = []
    else:
        raw_tau = None
    for seed in range(starting_seed, starting_seed + exp_num):
        ps['seed'] = seed
        if exp_type == 'MCQN':
            G, H, F, gamma, c, d, alpha, a, b, TT = generate_MCQN_data(seed, K, I, **settings)
        elif exp_type == 'reentrant':
            G, H, F, gamma, c, d, alpha, a, b, TT = generate_reentrant_data(seed, K, I, **settings)
        elif exp_type == 'MCQN_routing':
            G, H, F, gamma, c, d, alpha, a, b, TT = generate_MCQN_routing_data(seed, K, I, **settings)
        else:
            raise Exception('Undefined experiment type!')
        if T is None:
            if TT is None:
                raise Exception('Undefined time horizon!')
        import time
        start_time = time.time()
        if solver_settings is None:
            solver_settings = SCLP_settings(find_alt_line=False)
        t, x, q, u, p, pivots, obj, err, NN, tau, STEPCOUNT, Tres, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, T, solver_settings)
        print(obj, err)
        time_to_solve = time.time() - start_time
        print("--- %s seconds ---" % (time_to_solve))
        if res == 0 or use_adaptive_T:
            if res != 0:
                ps['T'] = 'adpt'
                T = Tres
            full_file_name = pu.get_CPLEX_data_file_name(exp_type, **ps)
            write_CPLEX_dat(full_file_name, T, G, H, alpha, a, b, gamma, c)
            path, filename = os.path.split(full_file_name)
            r = {'file': filename, 'seed': seed, 'result': res, 'objective': obj, 'time': time_to_solve,'steps': STEPCOUNT,
                 'intervals': NN, 'mean_tau': np.mean(tau), 'max_tau': np.max(tau), 'min_tau':np.min(tau), 'std_tau':np.std(tau)}
            results.append(r)
            if get_raw_tau:
                raw_tau.append({'file': filename,'raw_tau':tau})
            files.append(full_file_name)
        else:
            failure_trials +=1
    return results, failure_trials, files, raw_tau

