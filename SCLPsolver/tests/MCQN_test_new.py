import sys
import os
proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)
from SCLP import SCLP, SCLP_settings
from doe.data_generators.MCQN import generate_MCQN_data
from subroutines.utils import relative_to_project
from doe.results_producer import write_results_to_csv

K = 800
I = 80
import time
solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False,  memory_management= False, suppress_printing = False)

settings = {'alpha_rate':  1, 'cost_scale':2, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
                    'gamma_rate':0, 'c_scale': 0, 'h_rate': 0.2}
seed = 1004
G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)
TT = 100

# import cProfile, pstats, io
# pr = cProfile.Profile()
#pr.enable()
result = {'servers': I, 'buffers': K, 'seed': seed}
start_time = time.time()
solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, 3/12 * TT, solver_settings)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)
#pr.disable()
print(obj, err, maxT)
time1 = time.time() - start_time
print("--- %s seconds ---" % time1)
result['time1'] = time1
result['STEPCOUNT1'] = STEPCOUNT
start_time = time.time()
STEPCOUNT, pivot_problem = solution.recalculate(param_line, 1/12 * TT, 4/12 * TT, None, solver_settings, 10E-11, mm = None)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)
print(obj, err, maxT)
time2 = time.time() - start_time
print("--- %s seconds ---" % time2)
result['time2'] = time2
result['STEPCOUNT2'] = STEPCOUNT
start_time = time.time()
STEPCOUNT, pivot_problem =solution.recalculate(param_line, 1/12 * TT, 4/12 * TT, None, solver_settings, 10E-11, mm = None)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)
print(obj, err, maxT)
time3 = time.time() - start_time
print("--- %s seconds ---" % time3)
result['time3'] = time3
result['STEPCOUNT3'] = STEPCOUNT
start_time = time.time()
STEPCOUNT, pivot_problem = solution.recalculate(param_line, 1/12 * TT, 4/12 * TT, None, solver_settings, 10E-11, mm = None)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)
print(obj, err, maxT)
time4 = time.time() - start_time
print("--- %s seconds ---" % time4)
result['time4'] = time4
result['STEPCOUNT4'] = STEPCOUNT
results = [result]
res_file = relative_to_project('online_results.csv')
write_results_to_csv(results, res_file)
# s = io.StringIO()
# ps = pstats.Stats(pr, stream=s)
# ps.print_stats()
# print(s.getvalue())