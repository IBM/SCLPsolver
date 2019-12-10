import sys
import os
proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)
from SCLP import SCLP, SCLP_settings
from doe.data_generators.data_loader import load_data
from doe.doe_utils import path_utils

seed = 1000
K = 600
I = 200
pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
exp_path = pu.get_experiment_path_old('reentrant',K=K,I=I,seed=seed)
G, H, F, gamma, c, d, alpha, a, b, T = load_data(exp_path)
import time
start_time = time.time()
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
settings = SCLP_settings(tmp_path=exp_path)
solution, STEPCOUNT, Tres, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, 500, settings)
t, x, q, u, p, pivots, obj, err, NN, tau = solution.get_final_solution()
print(obj, err)
print("--- %s seconds ---" % (time.time() - start_time))
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s)
ps.print_stats()
print(s.getvalue())