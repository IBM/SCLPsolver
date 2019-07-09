from doe.data_generators.MCQN import generate_MCQN_data
from SCLP import SCLP, SCLP_settings
import matplotlib.pyplot as plt

seed = 1000
G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_data(seed, 12, 4)
T = 60
import time
start_time = time.time()
solver_settings = SCLP_settings(find_alt_line=False, collect_plot_data=True)
solution, STEPCOUNT, Tres, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, T, solver_settings)
t, x, q, u, p, pivots, obj, err, NN, tau = solution.extract_final_solution(alpha, a, b, gamma, c, d)
print(obj, err)
time_to_solve = time.time() - start_time
pp = solution.plot_history(plt)
pp.show()
print("--- %s seconds ---" % time_to_solve)
print("--- seed %s ---" % seed)