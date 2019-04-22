# from doe.doe import run_experiment_series
# from subroutines.utils import relative_to_project
# from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
# from doe.doe_utils import path_utils
# from doe.results_producer import combine_results, write_results_to_csv
import numpy as np
# import os
from test import test1

# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)



test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)









test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)














test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)





















test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
















test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)




test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)













test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)




test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
      {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)









# results, ftrials, files = run_experiment_series('MCQN', 10, 200, 20, 500, {'gdist':np.random.exponential, 'gdist_params':[0.5], 'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000 )
# pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
# DATADIRd = pu.get_CPLEX_data_path()
# cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main10.mod'), files)
# results = combine_results(results, cplex_results, 10)
# cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main100.mod'), files)
# results = combine_results(results, cplex_results, 100)
# res_file = relative_to_project('results_mm.csv')
# write_results_to_csv(results, res_file, True)
#
