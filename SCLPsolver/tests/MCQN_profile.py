import sys
import os
proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)
from SCLP import SCLP, SCLP_settings
from doe.data_generators.MCQN import generate_MCQN_data
from doe.doe_utils import path_utils

K = 1000
I = 100
seed = 1001
solver_settings = SCLP_settings(find_alt_line =False)

settings = {'alpha_rate':  1, 'cost_scale':2, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
                    'gamma_rate':0, 'c_scale': 0, 'h_rate': 0.2}
G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)
TT = 1000
import time
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
start_time = time.time()
solution, STEPCOUNT, Tres, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, solver_settings)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(False)
pr.disable()
print(obj, err, maxT)
print("--- %s seconds ---" % (time.time() - start_time))
s = io.StringIO()
ps = pstats.Stats(pr, stream=s)
ps.print_stats()
print(s.getvalue())