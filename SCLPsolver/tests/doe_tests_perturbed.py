# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from doe.doe import run_experiment_perturbation
from doe.data_generators.MCQN import generate_MCQN_data, perturb_MCQN_data
from SCLP import SCLP, SCLP_settings
from subroutines.utils import relative_to_project
# from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
from doe.results_producer import combine_results, write_results_to_csv
import os
import numpy as np

# G0, H0, F0, gamma0, c0, d0, alpha0, a0, b0, TT0, buffer_cost0 = generate_MCQN_data(1000, K=10, I=5,
#                                                                                    alpha_rate=1000,
#                                                                                    cost_scale=20,
#                                                                                    a_rate=0.1)
# solution0, STEPCOUNT0, Tres0, res0 = SCLP(G0, H0, F0, a0, b0, c0, d0, alpha0, gamma0, 500, SCLP_settings())
# reflexive = solution0.is_other_feasible(solution0)
# print("reflexivity of feasible solution: {}".format(reflexive))
#
#
rel_perturbation = 0.1
#
# G, H, F, a, b, c, d, alpha, gamma = perturb_MCQN_data(None, rel_perturbation, True, G0, H0, F0, a0, b0, c0, d0,
#                                                       alpha0, gamma0)
#print("G0={} G={} a0={} a={}".format(G0, G, a0, a))
#print("G0 - G = {}".format(G0-G))

#print("X")

# num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 1, 2000, 200, 500,
#                                                                                {'alpha_rate': 1000,
#                                                                                 'cost_scale': 20,
#                                                                                 'a_rate': 0.1},
#                                                                                rel_perturbation=0.00,
#                                                                                symmetric=True,
#                                                                                starting_seed=1000)

# num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 10, 200, 20, 50,
#                                                                                {'alpha_rate': 1000,
#                                                                                 'cost_scale': 20,
#                                                                                 'a_rate': 0.1},
#                                                                                rel_perturbation=rel_perturbation,
#                                                                                symmetric=True,
#                                                                                starting_seed =1000)

num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 100, 400, 40, 500,
                                                                               {'alpha_rate': 1000,
                                                                                'cost_scale': 20,
                                                                                'a_rate': 0.1},
                                                                               rel_perturbation=rel_perturbation,
                                                                               symmetric=True,
                                                                               starting_seed =1000)

# num_feasible, true_objective, perturbed_obj_vals = run_experiment_perturbation('MCQN', 100, 400, 40, 100,
#                                                                                {'alpha_rate': 1000,
#                                                                                 'cost_scale': 20,
#                                                                                 'a_rate': 0.1},
#                                                                                rel_perturbation=0.01,
#                                                                                symmetric=True,
#                                                                                starting_seed =1000)


#
print(num_feasible, true_objective, perturbed_obj_vals)
