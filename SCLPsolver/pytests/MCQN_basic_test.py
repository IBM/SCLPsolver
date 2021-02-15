import pytest
import os, sys

proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)

from SCLPsolver.SCLP import SCLP, SCLP_settings
from SCLPsolver.doe.data_generators.MCQN import generate_MCQN_data


def test_basic_mcqn():
    K = 400
    I = 40
    import time
    solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False,  memory_management= False, suppress_printing = False)

    settings = {'alpha_rate':  1, 'cost_scale':2, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
                        'gamma_rate':0, 'c_scale': 0, 'h_rate': 0.2}
    seed = 1009
    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)
    TT = 100

    result = {'servers': I, 'buffers': K, 'seed': seed}
    start_time = time.time()
    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, 3/12 * TT, solver_settings)
    t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)

    assert obj is not None
    assert 0 < maxT < TT
    assert len(t) > 0


def test_degenerate_mcqn():
    K = 400
    I = 40
    import time
    solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False,  memory_management= False, suppress_printing = False)

    settings = {'alpha_rate':  1, 'cost_scale':2, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
                        'gamma_rate':0, 'c_scale': 0, 'h_rate': 0.2}
    seed = 1009
    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)
    a[0:4] = [0,0,0,0]
    c[6:8] = [0,0]
    TT = 100

    result = {'servers': I, 'buffers': K, 'seed': seed}
    start_time = time.time()
    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, 3/12 * TT, solver_settings)
    t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)

    assert obj is not None
    assert 0 < maxT < TT
    assert len(t) > 0
