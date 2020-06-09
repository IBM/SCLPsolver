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
from doe.data_generators.MCQN import generate_MCQN_data
from doe.data_generators.write_CPLEX_dat import write_CPLEX_dat
from doe.doe_utils import path_utils
from subroutines.utils import relative_to_project


# I - number of servers
# K - number of buffers
# settings - data generation parameters, including
#   - \alpha_k ~ U(0, alpha_rate) initial amount of fluids
#   - a_k ~ U(0, alpha_rate) exogeneous input rates
#   - \sum_k p_{j,k} = sum_rate \forall j proportion of fluids kept in the system
#   - nz proportion of non-zero p_{j,k}
#   - h_j ~ U(0, cost_scale) holding costs
#   - \gamma_j ~ U(0, gamma_rate) constant control cost
#   - c_j ~ U(0, c_scale) linearly changing control cost
#   - H_{i=s(j),j} ~ U(0, h_rate) service time for a single unit of job class j
#   - there are other possible parameters changing distributions, etc.

I = 100
K = 1000
settings = {'alpha_rate':  1, 'cost_scale':2, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
                    'gamma_rate':0, 'c_scale': 0, 'h_rate': 0.2}
seed = 1000
G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)
TT = 100
# calculating total buffer cost for the target T:
#   tot_buf_cost = h' \alpha T + h' a T^2/2
tot_buf_cost = total_buffer_cost[0]*TT+total_buffer_cost[1]*TT*TT/2.0
# solver_settings - parameters fot SCLP solver
solver_settings = SCLP_settings(find_alt_line =False)
# set suppress_printing = False if you would like to see summary of each iteration
solver_settings.suppress_printing = True
solver_settings.memory_management = False
import time
start_time = time.time()
# run simplex-type algorithm to solve SCLP
solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, solver_settings)
# extract detailed solution including primal and dual controls
t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(False)
# problem objective is h'x(t) or h' \alpha T + h' a T^2/2 - V(SCLP)
pobj = tot_buf_cost - obj
print("SCLP objective:", obj, "Problem objective:", pobj, "steps:", STEPCOUNT, "intervals:", len(tau))
sol_time = time.time() - start_time
print("Time: --- %s seconds ---" % (sol_time))
# preparing CPLEX .dat file name
ps = {'K': K, 'I': I, 'T': TT}
for k, v in settings.items():
    if isinstance(v, object) and hasattr(v, '__name__'):
        ps[k] = v.__name__[:4]
    else:
        ps[k] = str(v)
# uses current directory change if you wnat to store CPLEX dat file in the specific directory
pu = path_utils('')
full_file_name = pu.get_CPLEX_data_file_name('MCQN', **ps)
# writing .dat file for CPLEX
write_CPLEX_dat(full_file_name, TT, G, H, alpha, a, b, gamma, c, buffer_cost)
# next line requires CPLEX - comment this line if you have no CPLEX
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
discretization = 10
# note on discretization .mod file names
#   - discretization x1     main1xobj.mod
#   - discretization x10    main10xobj.mod
#   - discretization x100   main100xobj.mod
#   - discretization x1000  main1000xobj.mod
cplex_results = run_cplex_experiments(pu.get_CPLEX_data_path(),
                                      relative_to_project('doe/cplex_integration/mod_files/main' + str(discretization) +'xobj.mod'),
                                      [full_file_name])
optimality_gap = cplex_results[0]['objective'] - pobj
relative_error = optimality_gap/abs(pobj)
relative_time = cplex_results[0]['time'] / sol_time
print("Discretization relative error:", relative_error, "discretization relative solution time:", relative_time)
