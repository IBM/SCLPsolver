import numpy as np
from test import test1

# test1('results_mm.csv', False, 'reentrant', 1, 1000, 100, 200,
#       {'first_alpha':100, 'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0,
#        'gamma_rate': -1, 'c_scale': 0},starting_seed =1004)

# test1('results_mm.csv', False, 'MCQN_routing', 1, 200, 20, 10,
#       {'J':400,'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0, 'sum_rate':0.9, 'nz': 0.4,
#        'gamma_rate': -1, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'reentrant', 4, 1000, 100, 200,
#       {'first_alpha':100, 'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0,
#        'gamma_rate': -1, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1001)

# test1('results_mm.csv', False, 'MCQN', 3, 800, 80, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)

test1('results_mm.csv', False, 'reentrant', 2, 100, 10, 100,
       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)