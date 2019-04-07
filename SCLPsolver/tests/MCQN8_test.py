import sys
import os
proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)
from SCLP8 import SCLP
from data_generators.data_loader import load_data


def relative_to_project(file_path):
    if os.path.isabs(file_path):
        return file_path
    else:
        proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
        return os.path.join(proj, file_path)

seed = 1013
K = 2000
I = 200
#tmp_path =  relative_to_project('tests/data/MCQN')
tmp_path =  'C:/Users/evgensh/Box/SCLP comparison/data/MCQN'
G, H, F, gamma, c, d, alpha, a, b, T = load_data(K, I, seed, tmp_path)
import time
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
start_time = time.time()
t, x, q, u, p, pivots, obj, err, NN, STEPCOUNT = SCLP(G, H, F, a, b, c, d, alpha, gamma, 500, {}, 1E-11)
print(obj, err)
print("--- %s seconds ---" % (time.time() - start_time))
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s)
ps.print_stats()
print(s.getvalue())
