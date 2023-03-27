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
from .matlab_utils import find
from .classification import classification
from .SCLP_pivot import SCLP_pivot
from .collision_info import collision_info
from .parametric_line import parametric_line
from .SCLP_solver import SCLP_solver

#'#@profile
def SCLP_x0_solver(solution, param_line, target_x0, target_T, DEPTH, STEPCOUNT, ITERATION, settings, tolerance, find_alt_line=True, mm=None):

    ITERATION[DEPTH] = 0
    K_add_set = find(np.logical_and(param_line.x_0 == 0, target_x0 > 0))

    pivot_problem = {'result': 0}
    solution.print_short_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], 0, 0, 'x0')
    solution.clear_collision_stack()
    source_T = param_line.T

    for v1 in K_add_set:
        col_info = collision_info('x0: ' + str(v1), 0, -1, 0, v1+1, [])
        solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(param_line.Kset_0, param_line.Jset_N, solution, col_info, DEPTH, STEPCOUNT,
                                                                   ITERATION, settings, tolerance)
        param_line = param_line.get_x0_parline(solution, v1+1, target_x0[v1])
        res = solution.update_state(param_line, settings.check_intermediate_solution, tolerance * 100)
        if not res:
            return solution, STEPCOUNT, {'result': 1}
        col_info, problem = classification(solution, param_line, tolerance)
        theta = param_line.theta
        if param_line.is_end(col_info.delta):
            param_line.forward_to_end()
        else:
            param_line.forward_to(col_info.delta/2)
        STEPCOUNT = STEPCOUNT + 1
        ITERATION[DEPTH] = ITERATION[DEPTH] + 1
        solution.print_short_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], theta, param_line.theta, 'x0: ' + str(v1))
    if abs(source_T - target_T)  < tolerance:
        param_line = parametric_line(param_line.x_0, param_line.q_N, 1, source_T, 0, target_x0 - param_line.x_0, None,
                               param_line.Kset_0, param_line._Jset_N)
    else:
        param_line = parametric_line(param_line.x_0, param_line.q_N, 1, source_T, target_T - source_T, target_x0 - param_line.x_0, None,
                                     param_line.Kset_0, param_line._Jset_N)
    solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 'update', DEPTH, STEPCOUNT, ITERATION, settings, tolerance, find_alt_line,
                mm)
    return STEPCOUNT, pivot_problem

