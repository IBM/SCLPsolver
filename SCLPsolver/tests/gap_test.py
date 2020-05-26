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

# test1('results_mm.csv', False, 'reentrant', 1, 500, 100, 1000,
#        {'first_alpha':  1, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.05, 'h_rate' : 0.1,
#         'gamma_rate':0, 'c_scale': 0},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN_routing', 1, 90, 30, 1000,
#       {'J':180, 'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
#        'gamma_rate':0, 'c_scale': 0, 'h_rate' : 0.1},starting_seed =1000)

# test1('results_mm.csv', False, 'MCQN_routing', 1, 200, 20, 100,
#       {'J':400, 'alpha_rate':  20, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5, 'h_rate': 0.05,
#        'gamma_rate':0, 'c_scale': 0},starting_seed =1001)

b = np.array([[0, 1], [2, 3]])
np.matrix.resize(b,(3,3))
print(b)