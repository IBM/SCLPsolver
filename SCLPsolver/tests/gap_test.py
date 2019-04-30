import numpy as np
from test import test1

test1('results_mm.csv', False, 'MCQN', 1, 200, 20, 10000,
      {'alpha_rate':  40, 'cost_scale':0.1, 'a_rate' : 0.05, 'sum_rate':0.8, 'nz': 0.6,
       'gamma_rate': -10, 'c_scale': 1},starting_seed =1004)