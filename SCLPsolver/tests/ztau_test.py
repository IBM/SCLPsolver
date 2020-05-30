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

import sys
sys.path.append('C:\DataD\Work\CERBERO\CLP\SCLPsolver')
from doe.data_generators.MCQN_routing import generate_MCQN_routing_data
from SCLP import SCLP, SCLP_settings
import os
import numpy as np
settings = SCLP_settings(hot_start =True, save_solution = True, max_iteration=21424)
G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_routing_data(1000, 200, 20, **{'J':400,
        'alpha_rate':  20, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5, 'h_rate': 0.05, 'gamma_rate':0, 'c_scale': 0})
print(a)
print(c)
solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, 100, settings)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution()
print(obj, err)
