from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
import csv
import os
import numpy as np

results, ftrials, files = run_experiment_series('MCQN', 1, 200, 20, 500, {'gdist':np.random.exponential, 'gdist_params':[0.5], 'hdist':np.random.exponential, 'hdist_params':[0.5], 'alpha_dist':np.random.exponential, 'alpha_dist_params':[0.5], 'cost_dist':np.random.exponential, 'cost_dist_params':[0.5],
       'alpha_rate':  1000, 'cost_scale':2, 'a_rate' : 0.01, 'sum_rate':0.8, 'nz': 0.2, 'gamma_rate':  -50, 'gamma_dist':np.random.exponential, 'gamma_dist_params':[0.5], 'c_scale':  -10, 'c_dist':np.random.exponential, 'c_dist_params':[0.5]},starting_seed =1001 )
print(results)