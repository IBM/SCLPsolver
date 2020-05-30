import sys
import os
proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)
from SCLP import SCLP, SCLP_settings
from doe.data_generators.MCQN_routing1 import generate_MCQN_routing_data
from doe.doe_utils import path_utils

I = 50
K = I * 10
J = K * 2
seed = 1006
solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False, memory_management=False)

settings = {'J': J, 'alpha_rate': 10, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.8, 'nz': 0.5,
                'gamma_rate': 0, 'c_scale': 0, 'h_rate': 4}
G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_routing_data(seed, K, I, **settings)
TT = 200
import time
start_time = time.time()
solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, solver_settings)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(False)
print(obj, err, maxT)
print("--- %s seconds ---" % (time.time() - start_time))
