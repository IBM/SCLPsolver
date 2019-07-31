import numpy as np
from .matlab_utils import find
from .pivot import full_pivot
from .pivot_new import base_pivot

#'#@profile
def simplex_procedures(A,pn,dn,ps,ds, tmp_matrix, tolerance = 0):

    err = dict()
    err['result'] = 0
    mm = A.shape[0]
    nn = A.shape[1]

    pneg = find(ps == -1)
    while pneg.size > 0:
        i = pneg[0]
        if tolerance == 0:
            cond = A[i + 1, 1:] != 0
        else:
            cond = np.absolute(A[i + 1, 1:]) > tolerance
        jj = find(np.logical_and(ds == -1, cond))
        if jj.size > 0:
            j = jj[0]
        else:
            mat = A[i + 1, 1:] / A[0, 1:]
            if A[i + 1, 0] > 0:
                j = np.argmax(mat * (ds != 1))
                m = mat[j]
            else:
                j = np.argmin(mat * (ds != 1))
                m = -mat[j]
            if m <=0:
                jj = find(A[i + 1, 1:])
                if jj.size > 0:
                    j = jj[0]
                else:
                    raise Exception('*** No pivot available')
        A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds, tmp_matrix)
        pneg = find(ps == -1)

    dneg = find(ds == -1)
    while dneg.size > 0:
        j = dneg[0]
        if tolerance == 0:
            cond = A[1:, j + 1] != 0
        else:
            cond = np.absolute(A[1:, j + 1]) > tolerance
        ii = find(np.logical_and(ps == -1, cond))
        if ii.size > 0:
            i = ii[0]
        else:
            mat = -A[1:, j + 1] / A[1:, 0]
            if A[0, j + 1] < 0:
                i = np.argmax(mat * (ps != 1))
                m = mat[i]
            else:
                i = np.argmin(mat * (ps != 1))
                m = -mat[i]
            if m <=0:
                ii = find(A[1:, j+1])
                if ii.size > 0:
                    i = ii[0]
                else:
                    raise Exception('*** No pivot available')
        A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds, tmp_matrix)
        dneg = find(ds == -1)

    ptest = find(np.logical_and(ps == 0,  A[1:, 0] < 0))
    dtest = find(np.logical_and(ds == 0,  A[0, 1:] < 0))

    if ptest.size > 0 and dtest.size == 0:
        while ptest.size > 0:
            i = ptest[0]
            mat = np.divide(-A[i + 1, 1:], A[0, 1:], out=np.zeros_like(A[i + 1, 1:]), where=np.logical_and(A[0, 1:]!=0, ds != 1))
            j = np.argmax(mat)
            #j = np.argmax(mat * (ds != 1))
            if mat[j] <= 0:
                A[0, 0] = -np.inf
                err['result'] = 1
                err['message'] = '***  problem is primal infeasible'
                return A, pn, dn, ps, ds, err
            A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds, tmp_matrix)
            ptest = find(np.logical_and(ps == 0, A[1:, 0] < 0))
    elif ptest.size == 0 and dtest.size > 0:
        while dtest.size > 0:
            j = dtest[0]
            mat = np.divide(A[1:, j + 1], A[1:, 0], out=np.zeros_like(A[1:, j + 1]), where=np.logical_and(A[1:, 0] != 0, ps != 1))
            i = np.argmax(mat)
            #i = np.argmax(mat * (ps != 1))
            if mat[i] <= 0:
                A[0, 0] = np.inf
                err['result'] = 2
                err['message'] = '***  problem is dual infeasible'
                return A, pn, dn, ps, ds, err
            A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds, tmp_matrix)
            dtest = find(np.logical_and(ds == 0, A[0, 1:] < 0))
    elif ptest.size > 0 and dtest.size > 0:
        B = np.zeros((mm+1,nn+1))
        tmp_matrix = np.zeros_like(B)
        B[:-1,-1:] = np.random.rand(mm, 1) + 1
        B[-1:,:-1] = np.random.rand(1, nn) + 1
        B[:-1, :-1] = A
        mat = np.divide(-A[0, 1:], B[-1, 1:-1], out=np.zeros_like(A[0, 1:]), where=np.logical_and(B[-1, 1:-1] > 0, ds != 1) )
        j = np.argmax(mat)
        mu1 = mat[j]
        mat = np.divide(-A[1:, 0], B[1:-1, -1], out=np.zeros_like(A[1:, 0]), where=np.logical_and(B[1:-1, -1] >0, ps != 1) )
        i = np.argmax(mat)
        mu2 = mat[i]
        mu = max(mu1,mu2)
        while mu > 0:
            if mu1 > mu2:
                div = B[1:-1, 0] + mu * B[1:-1, -1]
                mat = np.divide(B[1:-1, j+1], div , out=np.full_like(B[1:-1, j+1], -1), where= np.logical_and(div !=0, ps != 1))
                i = np.argmax(mat)
                if mat[i] <= 0:
                    B[0, 0] = np.inf
                    err['result'] = 2
                    err['message'] = '***  problem is dual infeasible'
                    return B[:-1,:-1], pn, dn, ps, ds, err
            else:
                div = B[0, 1:-1] + mu * B[-1, 1:-1]
                mat = np.divide(-B[i + 1, 1:-1], div, out=np.full_like(B[i + 1, 1:-1], -1), where= np.logical_and(div !=0, ds != 1))
                j = np.argmax(mat)
                if mat[j] <= 0:
                    B[0, 0] = - np.inf
                    err['result'] = 1
                    err['message'] = '***  problem is primal infeasible'
                    return B[:-1, :-1], pn, dn, ps, ds, err
            B, pn, dn, ps, ds = full_pivot(B, i, j, pn, dn, ps, ds, tmp_matrix)
            mat = np.divide(-B[0, 1:-1], B[-1, 1:-1], out=np.zeros_like(B[0, 1:-1]), where=np.logical_and(B[-1, 1:-1] > 0, ds != 1))
            j = np.argmax(mat)
            mu1 = mat[j]
            mat = np.divide(-B[1:-1, 0], B[1:-1, -1], out=np.zeros_like(B[1:-1, 0]), where=np.logical_and(B[1:-1, -1] > 0, ps != 1))
            i = np.argmax(mat)
            mu2 = mat[i]
            mu = max(mu1, mu2)
        A = B[:-1, :-1]
    return A, pn, dn, ps, ds, err

def unsigned_simplex(LP_form, tmp_matrix = None, tolerance = 0):

    err = dict()
    err['result'] = 0
    ptest = find(LP_form.simplex_dict[1:, 0] < 0)
    dtest = find(LP_form.simplex_dict[0, 1:] < 0)

    if ptest.size > 0 and dtest.size == 0:
        if tmp_matrix is None:
            tmp_matrix = np.zeros_like(LP_form.simplex_dict)
        while ptest.size > 0:
            i = ptest[0]
            mat = np.divide(-LP_form.simplex_dict[i + 1, 1:], LP_form.simplex_dict[0, 1:],
                            out=np.zeros_like(LP_form.simplex_dict[i + 1, 1:]), where=LP_form.simplex_dict[0, 1:]!=0)
            j = np.argmax(mat)
            if mat[j] <= 0:
                LP_form.simplex_dict[0, 0] = -np.inf
                err['result'] = 1
                err['message'] = '***  problem is primal infeasible'
                return LP_form, err
            LP_form = base_pivot(LP_form, i, j, tmp_matrix)
            ptest = find(LP_form.simplex_dict[1:, 0] < 0)
    elif ptest.size == 0 and dtest.size > 0:
        if tmp_matrix is None:
            tmp_matrix = np.zeros_like(LP_form.simplex_dict)
        while dtest.size > 0:
            j = dtest[0]
            mat = np.divide(LP_form.simplex_dict[1:, j + 1], LP_form.simplex_dict[1:, 0],
                            out=np.zeros_like(LP_form.simplex_dict[1:, j + 1]), where=LP_form.simplex_dict[1:, 0] != 0)
            i = np.argmax(mat)
            if mat[i] <= 0:
                LP_form.simplex_dict[0, 0] = np.inf
                err['result'] = 2
                err['message'] = '***  problem is dual infeasible'
                return LP_form, err
            LP_form = base_pivot(LP_form, i, j, tmp_matrix)
            dtest = find(LP_form.simplex_dict[0, 1:] < 0)
    elif ptest.size > 0 and dtest.size > 0:
        mm = LP_form.simplex_dict.shape[0]
        nn = LP_form.simplex_dict.shape[1]
        B = np.zeros((mm+1,nn+1))
        tmp_matrix = np.zeros_like(B)
        B[:-1,-1:] = np.random.rand(mm, 1) + 1
        B[-1:,:-1] = np.random.rand(1, nn) + 1
        B[:-1, :-1] = LP_form.simplex_dict
        from .LP_formulation import LP_formulation
        LP_form2 = LP_formulation(B,LP_form.prim_name,LP_form.dual_name)
        mat = np.divide(-LP_form.simplex_dict[0, 1:], B[-1, 1:-1], out=np.zeros_like(LP_form.simplex_dict[0, 1:]), where=B[-1, 1:-1] > 0)
        j = np.argmax(mat)
        mu1 = mat[j]
        mat = np.divide(-LP_form.simplex_dict[1:, 0], B[1:-1, -1], out=np.zeros_like(LP_form.simplex_dict[1:, 0]), where=B[1:-1, -1] >0)
        i = np.argmax(mat)
        mu2 = mat[i]
        mu = max(mu1,mu2)
        while mu > 0:
            if mu1 > mu2:
                div = LP_form2.simplex_dict[1:-1, 0] + mu * LP_form2.simplex_dict[1:-1, -1]
                mat = np.divide(LP_form2.simplex_dict[1:-1, j+1], div, out=np.full_like(LP_form2.simplex_dict[1:-1, j+1], -1), where= div !=0)
                i = np.argmax(mat)
                if mat[i] <= 0:
                    B[0, 0] = np.inf
                    err['result'] = 2
                    err['message'] = '***  problem is dual infeasible'
                    LP_form.simplex_dict = LP_form2.simplex_dict[:-1,:-1]
                    return LP_form, err
            else:
                div = LP_form2.simplex_dict[0, 1:-1] + mu * LP_form2.simplex_dict[-1, 1:-1]
                mat = np.divide(-LP_form2.simplex_dict[i + 1, 1:-1], div, out=np.full_like(LP_form2.simplex_dict[i + 1, 1:-1], -1), where= div !=0)
                j = np.argmax(mat)
                if mat[j] <= 0:
                    B[0, 0] = - np.inf
                    err['result'] = 1
                    err['message'] = '***  problem is primal infeasible'
                    LP_form.simplex_dict = LP_form2.simplex_dict[:-1, :-1]
                    return LP_form, err
            LP_form2 = base_pivot(LP_form2, i, j, tmp_matrix)
            mat = np.divide(-LP_form2.simplex_dict[0, 1:-1], LP_form2.simplex_dict[-1, 1:-1],
                            out=np.zeros_like(LP_form2.simplex_dict[0, 1:-1]), where=LP_form2.simplex_dict[-1, 1:-1] > 0)
            j = np.argmax(mat)
            mu1 = mat[j]
            mat = np.divide(-LP_form2.simplex_dict[1:-1, 0], LP_form2.simplex_dict[1:-1, -1], out=np.zeros_like(B[1:-1, 0]), where=LP_form2.simplex_dict[1:-1, -1] > 0)
            i = np.argmax(mat)
            mu2 = mat[i]
            mu = max(mu1, mu2)
        LP_form.simplex_dict = LP_form2.simplex_dict[:-1, :-1]
    return LP_form, err