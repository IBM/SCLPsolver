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

from .matlab_utils import find
from .sparse_matrix_constructor import sparse_matrix_constructor


#'#@profile
def calc_controls(solution, JJ, KK, preserve = True):

    new_dict = solution.get_basis_at(0)
    u = sparse_matrix_constructor(None, None, JJ)
    p = sparse_matrix_constructor(None, None, KK)
    if preserve:
        new_dict = new_dict.copy()

    for place in range(solution.NN):
        klist2 = find(new_dict.dual_name > 0)
        jlist1 = find(new_dict.prim_name < 0)
        kn2 =  new_dict.dual_name[klist2]
        jn1 = -new_dict.prim_name[jlist1]
        u.append(sparse_matrix_constructor(new_dict.simplex_dict[jlist1+1,0].copy(), jn1-1, JJ))
        p.append(sparse_matrix_constructor(new_dict.simplex_dict[0,klist2+1].copy(), kn2-1, KK))
        if place < solution.NN - 1:
            new_dict = solution.get_next_basis_for_solution(new_dict, place, preserve)
    return u.get_matrix(), p.get_matrix()