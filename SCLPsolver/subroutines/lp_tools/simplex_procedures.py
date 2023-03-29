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
from .LP_formulation import LP_formulation
from .pivot import pivot_ij, signed_pivot_ij
from .in_out_pivot import in_out_pivot
from .cy_lp_tools import prim_ratio_test, dual_ratio_test, find_i

def simplex_procedures(dct, ps, ds, tolerance = 0, res_dct = None):

    err = dict()
    err['result'] = 0
    mm = dct.simplex_dict.shape[0]
    nn = dct.simplex_dict.shape[1]
    pivots = in_out_pivot()

    pneg = find(ps == -1)
    while pneg.size > 0:
        i = pneg[0]
        if tolerance == 0:
            cond = dct.simplex_dict[i + 1, 1:] != 0
        else:
            cond = np.absolute(dct.simplex_dict[i + 1, 1:]) > tolerance
        jj = find(np.logical_and(ds == -1, cond))
        if jj.size > 0:
            j = jj[0]
        else:
            mat = dct.simplex_dict[i + 1, 1:] / dct.simplex_dict[0, 1:]
            if dct.simplex_dict[i + 1, 0] > 0:
                j = np.argmax(mat * (ds != 1))
                m = mat[j]
            else:
                j = np.argmin(mat * (ds != 1))
                m = -mat[j]
            if m <=0:
                jj = find(dct.simplex_dict[i + 1, 1:])
                if jj.size > 0:
                    j = jj[0]
                else:
                    raise Exception('*** No pivot available')
        (dct, in_, out_), ps, ds = signed_pivot_ij(dct, ps, ds, i, j, res_dct)
        pivots.pivot(in_, out_)
        res_dct = None
        pneg = find(ps == -1)

    dneg = find(ds == -1)
    while dneg.size > 0:
        j = dneg[0]
        #TODO: this should be double-checked
        i = find_i(dct.simplex_dict, j, ps, 0.)
        # if tolerance == 0:
        #     cond = dct.simplex_dict[1:, j + 1] != 0
        # else:
        #     cond = np.absolute(dct.simplex_dict[1:, j + 1]) > tolerance
        # ii = find(np.logical_and(ps == -1, cond))
        # if ii.size > 0:
        #     i = ii[0]
        # else:
        #     mat = -dct.simplex_dict[1:, j + 1] / dct.simplex_dict[1:, 0]
        #     if dct.simplex_dict[0, j + 1] < 0:
        #         i = np.nanargmax(mat * (ps != 1))
        #         print('max_pivot:', i, j)
        #         test = True
        #         m = mat[i]
        #     else:
        #         i = np.nanargmin(mat * (ps != 1))
        #         print('min_pivot:', i, j)
        #         test = True
        #         m = -mat[i]
        #     if m <=0:
        #         ii = find(dct.simplex_dict[1:, j+1])
        #         if ii.size > 0:
        #             i = ii[0]
        #         else:
        #             raise Exception('*** No pivot available')
        if i < 0:
            raise Exception('*** No pivot available')
        # if i1 != i:
        #     raise Exception('Incorrect i')
        (dct, in_, out_), ps, ds= signed_pivot_ij(dct, ps, ds, i, j, res_dct)
        pivots.pivot(in_, out_)
        res_dct = None
        dneg = find(ds == -1)

    ptest = find(np.logical_and(ps == 0,  dct.simplex_dict[1:, 0] < 0))
    dtest = find(np.logical_and(ds == 0,  dct.simplex_dict[0, 1:] < 0))

    if ptest.size > 0 and dtest.size == 0:
        while ptest.size > 0:
            i = ptest[0]
            j = prim_ratio_test(dct.simplex_dict, i, ds)-1
            if j < -1:
                dct.simplex_dict[0, 0] = -np.inf
                err['result'] = 1
                err['message'] = '***  problem is primal infeasible'
                return dct, ps, ds, pivots, err
            (dct, in_, out_), ps, ds = signed_pivot_ij(dct, ps, ds, i, j, res_dct)
            pivots.pivot(in_, out_)
            res_dct = None
            ptest = find(np.logical_and(ps == 0, dct.simplex_dict[1:, 0] < 0))
    elif ptest.size == 0 and dtest.size > 0:
        while dtest.size > 0:
            j = dtest[0]
            i = dual_ratio_test(dct.simplex_dict, j, ps)-1
            if i < -1:
                dct.simplex_dict[0, 0] = np.inf
                err['result'] = 2
                err['message'] = '***  problem is dual infeasible'
                return dct, ps, ds, pivots, err
            (dct, in_, out_), ps, ds = signed_pivot_ij(dct, ps, ds, i, j, res_dct)
            pivots.pivot(in_, out_)
            res_dct = None
            dtest = find(np.logical_and(ds == 0, dct.simplex_dict[0, 1:] < 0))
    elif ptest.size > 0 and dtest.size > 0:
        B = np.zeros((mm+1,nn+1), order='C')
        tmp_matrix = np.zeros_like(B)
        B[:-1,-1:] = np.random.rand(mm, 1) + 1
        B[-1:,:-1] = np.random.rand(1, nn) + 1
        B[:-1, :-1] = dct.simplex_dict
        mat = np.divide(-dct.simplex_dict[0, 1:], B[-1, 1:-1], out=np.zeros_like(dct.simplex_dict[0, 1:]), where=np.logical_and(B[-1, 1:-1] > 0, ds != 1) )
        j = np.argmax(mat)
        mu1 = mat[j]
        mat = np.divide(-dct.simplex_dict[1:, 0], B[1:-1, -1], out=np.zeros_like(dct.simplex_dict[1:, 0]), where=np.logical_and(B[1:-1, -1] > 0, ps != 1) )
        i = np.argmax(mat)
        mu2 = mat[i]
        mu = max(mu1,mu2)
        from .LP_formulation import LP_formulation
        dct2 = LP_formulation(B, dct.prim_name.copy(), dct.dual_name.copy())
        while mu > 0:
            if mu1 > mu2:
                div = dct2.simplex_dict[1:-1, 0] + mu * dct2.simplex_dict[1:-1, -1]
                mat = np.divide(dct2.simplex_dict[1:-1, j+1], div, out=np.zeros_like(dct2.simplex_dict[1:-1, j+1]), where= np.logical_and(div !=0, ps != 1))
                i = np.argmax(mat)
                if mat[i] <= 0:
                    dct2.simplex_dict[0, 0] = np.inf
                    err['result'] = 2
                    err['message'] = '***  problem is dual infeasible'
                    return LP_formulation(np.ascontiguousarray(dct2.simplex_dict[:-1,:-1]), dct2.prim_name, dct2.dual_name), ps, ds, pivots, err
            else:
                div = dct2.simplex_dict[0, 1:-1] + mu * dct2.simplex_dict[-1, 1:-1]
                mat = np.divide(-dct2.simplex_dict[i + 1, 1:-1], div, out=np.zeros_like(dct2.simplex_dict[i + 1, 1:-1]), where= np.logical_and(div !=0, ds != 1))
                j = np.argmax(mat)
                if mat[j] <= 0:
                    dct2.simplex_dict[0, 0] = - np.inf
                    err['result'] = 1
                    err['message'] = '***  problem is primal infeasible'
                    return LP_formulation(np.ascontiguousarray(dct2.simplex_dict[:-1,:-1]), dct2.prim_name, dct2.dual_name), ps, ds, pivots,  err
            (dct2, in_, out_), ps, ds = signed_pivot_ij(dct2, ps, ds, i, j)
            pivots.pivot(in_, out_)
            mat = np.divide(-dct2.simplex_dict[0, 1:-1], dct2.simplex_dict[-1, 1:-1], out=np.zeros_like(dct2.simplex_dict[0, 1:-1]), where=np.logical_and(dct2.simplex_dict[-1, 1:-1] > 0, ds != 1))
            j = np.argmax(mat)
            mu1 = mat[j]
            mat = np.divide(-dct2.simplex_dict[1:-1, 0], dct2.simplex_dict[1:-1, -1], out=np.zeros_like(dct2.simplex_dict[1:-1, 0]), where=np.logical_and(dct2.simplex_dict[1:-1, -1] > 0, ps != 1))
            i = np.argmax(mat)
            mu2 = mat[i]
            mu = max(mu1, mu2)
        dct = LP_formulation(np.ascontiguousarray(dct2.simplex_dict[:-1,:-1]), dct2.prim_name, dct2.dual_name)
    return dct, ps, ds, pivots, err

def unsigned_simplex(lp: LP_formulation, tolerance: float = 1E-12, counter: list = None) -> (LP_formulation, dict):

    err = dict()
    err['result'] = 0
    ptest = find(lp.simplex_dict[1:, 0] < -tolerance)
    dtest = find(lp.simplex_dict[0, 1:] < -tolerance)

    if ptest.size > 0 and dtest.size == 0:
        while ptest.size > 0:
            i = ptest[0]
            j = prim_ratio_test(lp.simplex_dict, i, tolerance=tolerance) - 1
            if j < -1:
                lp.simplex_dict[0, 0] = -np.inf
                err['result'] = 1
                err['message'] = '***  problem is primal infeasible'
                return lp, err
            lp, in_, out_ = pivot_ij(lp, i, int(j), counter=counter)
            ptest = find(lp.simplex_dict[1:, 0] < -tolerance)
    elif ptest.size == 0 and dtest.size > 0:
        while dtest.size > 0:
            j = dtest[0]
            i = dual_ratio_test(lp.simplex_dict, j, tolerance=tolerance) - 1
            if i < -1:
                lp.simplex_dict[0, 0] = np.inf
                err['result'] = 2
                err['message'] = '***  problem is dual infeasible'
                return lp, err
            lp, in_, out_ = pivot_ij(lp, int(i), j, counter=counter)
            dtest = find(lp.simplex_dict[0, 1:] < -tolerance)
    elif ptest.size > 0 and dtest.size > 0:
        mm, nn = lp.simplex_dict.shape
        B = np.zeros((mm+1,nn+1), order='C')
        B[:-1, -1:] = np.random.rand(mm, 1) + 1
        B[-1:, :-1] = np.random.rand(1, nn) + 1
        B[:-1, :-1] = lp.simplex_dict
        lp_form2 = LP_formulation(B, lp.prim_name, lp.dual_name)
        mat = np.divide(-lp.simplex_dict[0, 1:], B[-1, 1:-1], out=np.zeros_like(lp.simplex_dict[0, 1:]), where=B[-1, 1:-1] > 0)
        j = np.argmax(mat)
        mu1 = mat[j]
        mat = np.divide(-lp.simplex_dict[1:, 0], B[1:-1, -1], out=np.zeros_like(lp.simplex_dict[1:, 0]), where=B[1:-1, -1] > 0)
        i = np.argmax(mat)
        mu2 = mat[i]
        mu = max(mu1,mu2)
        while mu > 0:
            if mu1 > mu2:
                div = lp_form2.simplex_dict[1:-1, 0] + mu * lp_form2.simplex_dict[1:-1, -1]
                mat = np.divide(lp_form2.simplex_dict[1:-1, j+1], div, out=np.zeros_like(lp_form2.simplex_dict[1:-1, j+1]), where= div !=0)
                i = np.argmax(mat)
                if mat[i] <= 0:
                    B[0, 0] = np.inf
                    err['result'] = 2
                    err['message'] = '***  problem is dual infeasible'
                    lp.simplex_dict = np.ascontiguousarray(lp_form2.simplex_dict[:-1, :-1])
                    return lp, err
            else:
                div = lp_form2.simplex_dict[0, 1:-1] + mu * lp_form2.simplex_dict[-1, 1:-1]
                mat = np.divide(-lp_form2.simplex_dict[i + 1, 1:-1], div, out=np.zeros_like(lp_form2.simplex_dict[i + 1, 1:-1]), where= div !=0)
                j = np.argmax(mat)
                if mat[j] <= 0:
                    B[0, 0] = - np.inf
                    err['result'] = 1
                    err['message'] = '***  problem is primal infeasible'
                    lp.simplex_dict = np.ascontiguousarray(lp_form2.simplex_dict[:-1, :-1])
                    return lp, err
            lp_form2, in_, out_ = pivot_ij(lp_form2, int(i), int(j), counter=counter)
            mat = np.divide(-lp_form2.simplex_dict[0, 1:-1], lp_form2.simplex_dict[-1, 1:-1],
                            out=np.zeros_like(lp_form2.simplex_dict[0, 1:-1]), where=lp_form2.simplex_dict[-1, 1:-1] > 0)
            j = np.argmax(mat)
            mu1 = mat[j]
            mat = np.divide(-lp_form2.simplex_dict[1:-1, 0], lp_form2.simplex_dict[1:-1, -1], out=np.zeros_like(B[1:-1, 0]), where=lp_form2.simplex_dict[1:-1, -1] > 0)
            i = np.argmax(mat)
            mu2 = mat[i]
            mu = max(mu1, mu2)
        lp.simplex_dict = np.ascontiguousarray(lp_form2.simplex_dict[:-1, :-1])
        lp.prim_name = lp_form2.prim_name
        lp.dual_name = lp_form2.dual_name
    return lp, err