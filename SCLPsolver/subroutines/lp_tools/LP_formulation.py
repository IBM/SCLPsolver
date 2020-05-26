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
from .simplex_procedures import simplex_procedures
from .cy_lp_tools import get_sign, get_sign1, partial_pivotII
from .pivot import signed_pivot_ij


class LP_formulation():

    __slots__ = ["simplex_dict", "prim_name", "dual_name", "prim_sign", "dual_sign"]

    def __init__(self, simplex_dict, prim_name, dual_name, prim_sign=None, dual_sign=None):
        self.simplex_dict, self.prim_name, self.dual_name, self.prim_sign, self.dual_sign =\
            simplex_dict, prim_name, dual_name, prim_sign, dual_sign

    def __copy__(self):
        if self.prim_sign is None:
            return LP_formulation(self.simplex_dict.copy(), self.prim_name.copy(), self.dual_name.copy())
        else:
            return LP_formulation(self.simplex_dict.copy(), self.prim_name.copy(), self.dual_name.copy(), self.prim_sign.copy(), self.dual_sign.copy())

    def copy(self):
        return self.__copy__()
        
def solve_ratesLP(LP_form, Kset, nJset, bases_mm, tolerance=0, build_sign=True):
    if build_sign:
        get_sign1(LP_form.prim_name, Kset, nJset, 1, bases_mm.ps)
        get_sign1(LP_form.dual_name, Kset, nJset, -1, bases_mm.ds)
    # part = False
    # if v1 is not None:
    #     ok, prim_vars, dual_vars, i, j = partial_pivotII(LP_form.simplex_dict, LP_form.prim_name, LP_form.dual_name, bases_mm.ps, bases_mm.ds, v1, in_diff[0], in_diff[1])
    #     if ok == 1:
    #         part = True
    #         prim_name, dual_name = LP_form.prim_name, LP_form.dual_name
    tmp_dict = bases_mm.pop()
    if tmp_dict is None:
        tmp_dict = LP_formulation(np.empty_like(LP_form.simplex_dict), None, None)
        #LP_form, ps, ds, pivots, err = simplex_procedures(LP_form.copy(), prim_sign, dual_sign, tolerance)
    #else:
    LP_form, ps, ds, pivots, err = simplex_procedures(LP_form, bases_mm.ps, bases_mm.ds, tolerance, tmp_dict)
    # if part:
    #     dual_name = dual_name.copy()
    #     tmp = dual_name[j]
    #     dual_name[j] = prim_name[i]
    #     prim_name = prim_name.copy()
    #     prim_name[i] = tmp
    #     if np.setdiff1d(prim_name, LP_form.prim_name, assume_unique=True).shape[0] > 0 or\
    #         np.setdiff1d(dual_name, LP_form.dual_name, assume_unique=True).shape[0] > 0:


        # if np.any(np.fabs(prim_vars[1:] - LP_form.simplex_dict[1:,0]) > 1E-10) or\
        #         np.any(np.fabs(dual_vars[1:] -LP_form.simplex_dict[0,1:]) > 1E-10):
        #     dual_name = dual_name.copy()
        #     tmp = dual_name[j]
        #     dual_name[j] = prim_name[i]
        #     prim_name = prim_name.copy()
        #     prim_name[i] = tmp
        #     print(np.any(LP_form.dual_name == v1), np.any(LP_form.dual_name == v2))
        #    print('????')
    return LP_form, pivots, err

def partial_solve_caseII(LP_form, Kset, nJset, bases_mm, v1, in_diff):
    get_sign1(LP_form.prim_name, Kset, nJset, 1, bases_mm.ps)
    get_sign1(LP_form.dual_name, Kset, nJset, -1, bases_mm.ds)
    ok, prim_vars, dual_vars, i, j = partial_pivotII(LP_form.simplex_dict, LP_form.prim_name, LP_form.dual_name,
                                                     bases_mm.ps, bases_mm.ds, v1, in_diff[0], in_diff[1])
    return ok, prim_vars, dual_vars, i, j

def solve_simple_caseII(LP_form, Kset, nJset, bases_mm, v1, in_diff):
    get_sign1(LP_form.prim_name, Kset, nJset, 1, bases_mm.ps)
    get_sign1(LP_form.dual_name, Kset, nJset, -1, bases_mm.ds)
    ok, prim_vars, dual_vars, i, j = partial_pivotII(LP_form.simplex_dict, LP_form.prim_name, LP_form.dual_name,
                                                     bases_mm.ps, bases_mm.ds, v1, in_diff[0], in_diff[1])
    tmp_dict = bases_mm.pop()
    if tmp_dict is None:
        tmp_dict = LP_formulation(np.empty_like(LP_form.simplex_dict), None, None)
    if ok==1:
        (LP_form, in_, out_), ps, ds = signed_pivot_ij(LP_form, bases_mm.ps, bases_mm.ds, i, j, tmp_dict)
        return ok, LP_form, (in_, out_), None
    else:
        LP_form, ps, ds, pivots, err = simplex_procedures(LP_form, bases_mm.ps, bases_mm.ds, 0, tmp_dict)
        return ok, LP_form, pivots, err

def solve_LP(LP_form, ps, ds, tolerance=0):
    LP_form, ps, ds, pivots, err = simplex_procedures(LP_form.copy(), ps, ds, tolerance)
    return LP_form, err

def solve_LP_in_place(LP_form, ps, ds, tolerance=0):
    LP_form, ps, ds, pivots, err = simplex_procedures(LP_form, ps, ds, tolerance)
    return LP_form, err


def get_pivot(b1, b2, prim):
    if prim:
        return np.setdiff1d(b1.prim_name, b2.prim_name, assume_unique=True)
    else:
        return np.setdiff1d(b1.dual_name, b2.dual_name, assume_unique=True)


def get_value_by_name(basis, name, prim):
    if prim:
        return basis.simplex_dict[1:, 0][basis.prim_name == name][0]
    else:
        return basis.simplex_dict[0, 1:][basis.dual_name == name][0]

def get_dx_names(basis):
    return basis.prim_name[basis.prim_name > 0]

def get_dq_names(basis):
    return basis.dual_name[basis.dual_name < 0]




