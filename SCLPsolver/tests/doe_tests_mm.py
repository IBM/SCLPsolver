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
#














# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)


























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
#
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
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)















# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)




















# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)














# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)

































# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# Not run yet -  start!!!!!!!!!!
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 80, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
#
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
# Not run yet - end












# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.01, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.1, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.4 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 120, 500,
#       {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
#        'alpha_rate':  1000, 'cost_scale':20, 'a_rate' : 0.2, 'sum_rate':0.99, 'nz': 0.6 },starting_seed =1000)









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

# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 250,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 250,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 250,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 250,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 1000,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 1000,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)


# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 600, 60, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 1000, 100, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 1000, 100, 500,
#       {'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 3, 600, 60, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 3, 600, 60, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 3, 800, 80, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 3, 800, 80, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 3, 1000, 100, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.2, 'sum_rate':0.8, 'nz': 0.2 },starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 3, 1000, 100, 500,
#       {'alpha_rate':  100, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6 },starting_seed =1000)


# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#


# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 400, 40, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 800, 80, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 1600, 160, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#        starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 1600, 160, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 1600, 160, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 1600, 160, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 1600, 160, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 1600, 160, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 3200, 320, 250,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#        starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 3200, 320, 500,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 3200, 320, 1000,
#       {'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.1, 'sum_rate': 0.9, 'nz': 0.6,
#        'gamma_rate': -1000, 'c_scale': 1},
#       starting_seed=1013)
#
#
# test1('results_mm.csv', False, 'MCQN', 10, 3200, 320, 250,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 3200, 320, 500,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)
#
# test1('results_mm.csv', False, 'MCQN', 10, 3200, 320, 1000,
#       {'gdist': np.random.exponential, 'gdist_params': [0.5], 'hdist': np.random.exponential, 'hdist_params': [0.5],
#        'alpha_dist': np.random.exponential, 'alpha_dist_params': [0.5], 'cost_dist': np.random.exponential,
#        'cost_dist_params': [0.5],
#        'alpha_rate': 1000, 'cost_scale': 2, 'a_rate': 0.01, 'sum_rate': 0.8, 'nz': 0.2,
#        'gamma_rate': -1000, 'gamma_dist': np.random.exponential, 'gamma_dist_params': [0.5], 'c_scale': 1, 'c_dist': np.random.exponential, 'c_dist_params': [0.5]},
#       starting_seed=1013)



# test1('results_mm.csv', False, 'MCQN', 10, 100, 10, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 3, 400, 40, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN', 3, 100, 10, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.1, 'sum_rate':0.9, 'nz': 0.6,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 10,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0, 'sum_rate':1, 'nz': 0.4,
#        'gamma_rate': -1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN_routing', 1, 200, 20, 1000,
#       {'J':1000,'alpha_rate':  1000, 'cost_scale':1, 'a_rate' : 0, 'sum_rate':0.9, 'nz': 0.8,
#        'gamma_rate': -1, 'c_scale': 0},starting_seed =1004)

# test1('results_mm.csv', False, 'reentrant', 5, 1000, 100, 10,
#       {'first_alpha':100, 'alpha_rate':  100, 'cost_scale':-1, 'a_rate' : 0.000001,
#        'gamma_rate': -1, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'reentrant', 5, 1000, 100, 10,
#       {'first_alpha':500, 'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 1,
#        'gamma_rate': -1, 'c_scale': 1},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate':  40, 'cost_scale':0.1, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.6,
#        'gamma_rate': -10, 'c_scale': 1},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 100,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 10},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 100,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 10},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 100,
#       {'alpha_rate':  100, 'cost_scale':0.1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 100,
#       {'alpha_rate':  100, 'cost_scale':0.1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 100,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 1},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 100,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 1},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 200,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 10},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 200,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 10},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 200,
#       {'alpha_rate':  100, 'cost_scale':0.1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 200,
#       {'alpha_rate':  100, 'cost_scale':0.1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 200,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 1},starting_seed =1000)
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 200,
#       {'alpha_rate':  100, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 1},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN', 10, 100, 10, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 10, 200, 20, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 5, 400, 40, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1005)
#
# test1('results_mm.csv', False, 'MCQN', 2, 600, 60, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 600, 60, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1002)
#
# test1('results_mm.csv', False, 'MCQN', 2, 600, 60, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1004)
#
# test1('results_mm.csv', False, 'MCQN', 2, 800, 80, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 800, 80, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1002)
#
# test1('results_mm.csv', False, 'MCQN', 2, 800, 80, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1004)
#
# test1('results_mm.csv', False, 'MCQN', 2, 1000, 100, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 1000, 100, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1002)
#
# test1('results_mm.csv', False, 'MCQN', 2, 1000, 100, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1004)

# test1('results_mm.csv', False, 'MCQN', 3, 125, 12, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'reentrant', 3, 125, 12, 1000,
#       {'alpha_rate':  10, 'cost_scale':1, 'a_rate' : 0.05,
#        'gamma_rate':-1, 'c_scale': 0},starting_seed =1000)

# Large gap!!!
# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.01, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.01, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.01, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)



# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)


# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)



# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.01, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.01, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.01, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.01, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.01, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.01, 'c_scale': 0},starting_seed =1000)
#
#
# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 100, 10, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 200, 20, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'MCQN', 2, 400, 40, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':-0.1, 'c_scale': 0},starting_seed =1000)


# Problems!
# test1('results_mm.csv', False, 'reentrant', 2, 100, 10, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'reentrant', 2, 200, 20, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'reentrant', 2, 400, 40, 100,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'reentrant', 2, 100, 10, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'reentrant', 2, 200, 20, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
#
# test1('results_mm.csv', False, 'reentrant', 2, 400, 40, 10000,
#       {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1000)



test1('results_mm.csv', False, 'MCQN_routing', 2, 100, 10, 100,
      {'J':200, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
       'gamma_rate':0, 'c_scale': 0},starting_seed =1000)

test1('results_mm.csv', False, 'MCQN_routing', 2, 200, 20, 100,
      {'J':400, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
       'gamma_rate':0, 'c_scale': 0},starting_seed =1000)

test1('results_mm.csv', False, 'MCQN_routing', 2, 400, 40, 100,
      {'J':800, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
       'gamma_rate':0, 'c_scale': 0},starting_seed =1000)

test1('results_mm.csv', False, 'MCQN_routing', 2, 100, 10, 10000,
      {'J':200, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
       'gamma_rate':0, 'c_scale': 0},starting_seed =1000)

test1('results_mm.csv', False, 'MCQN_routing', 2, 200, 20, 10000,
      {'J':400, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
       'gamma_rate':0, 'c_scale': 0},starting_seed =1000)

test1('results_mm.csv', False, 'MCQN_routing', 2, 400, 40, 10000,
      {'J':800, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.001, 'sum_rate':0.99, 'nz': 0.5,
       'gamma_rate':0, 'c_scale': 0},starting_seed =1000)
