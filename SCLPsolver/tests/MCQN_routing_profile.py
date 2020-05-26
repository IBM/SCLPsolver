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
import os
proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)
from SCLP import SCLP, SCLP_settings
from doe.data_generators.MCQN_routing1 import generate_MCQN_routing_data
from doe.doe_utils import path_utils

K = 600
I = 60
seed = 1000
solver_settings = SCLP_settings(find_alt_line =False)

settings = {'J':1200, 'alpha_rate':  4, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.5,
                    'gamma_rate':0, 'c_scale': 0, 'h_rate': 4}
G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_routing_data(seed, K, I, **settings)
TT = 100
import time
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
start_time = time.time()
solution, STEPCOUNT, Tres, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, solver_settings)
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(False)
pr.disable()
print(obj, err, maxT)
print("--- %s seconds ---" % (time.time() - start_time))
s = io.StringIO()
ps = pstats.Stats(pr, stream=s)
ps.print_stats()
print(s.getvalue())