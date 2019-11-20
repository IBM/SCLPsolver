from doe.doe import run_experiment_perturbation
from subroutines.utils import relative_to_project
# from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
from doe.results_producer import combine_results, write_results_to_csv
import os
import numpy as np

num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 1, 2000, 200, 500, {'alpha_rate':  1000, 'cost_scale':20,'a_rate' : 0.1}, rel_error=0.01, starting_seed =1000)

print(num_feasible, true_objective, perturbed_obj_vals)