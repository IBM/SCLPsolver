from doe.doe import run_experiment_perturbation
from doe.data_generators.MCQN import generate_MCQN_data, perturb_MCQN_data
from subroutines.utils import relative_to_project
# from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
from doe.results_producer import combine_results, write_results_to_csv
import os
import numpy as np

G0, H0, F0, gamma0, c0, d0, alpha0, a0, b0, TT0, buffer_cost0 = generate_MCQN_data(1000, K=10, I=5,
                                                                                   alpha_rate=1000,
                                                                                   cost_scale=20,
                                                                                   a_rate=0.1)
G, H, F, a, b, c, d, alpha, gamma = perturb_MCQN_data(None, 0.5, True, G0, H0, F0, a0, b0, c0, d0,
                                                      alpha0, gamma0)
print("G0={} G={} a0={} a={}".format(G0, G, a0, a))

# num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 1, 2000, 200, 500,
#                                                                                {'alpha_rate': 1000,
#                                                                                 'cost_scale': 20,
#                                                                                 'a_rate': 0.1},
#                                                                                rel_perturbation=0.01,
#                                                                                symmetric=True,
#                                                                                starting_seed =1000)

# num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 100, 200, 20, 50,
#                                                                                {'alpha_rate': 1000,
#                                                                                 'cost_scale': 20,
#                                                                                 'a_rate': 0.1},
#                                                                                rel_perturbation=0.01,
#                                                                                symmetric=True,
#                                                                                starting_seed =1000)

num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 100, 400, 40, 100,
                                                                               {'alpha_rate': 1000,
                                                                                'cost_scale': 20,
                                                                                'a_rate': 0.1},
                                                                               rel_perturbation=0.01,
                                                                               symmetric=True,
                                                                               starting_seed =1000)
print(num_feasible, true_objective, perturbed_obj_vals)

#
# print(num_feasible, true_objective, perturbed_obj_vals)
