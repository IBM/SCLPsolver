import numpy as np
from .matlab_utils import *
from .pivot import *


#'#@profile
def simplex_procedures(A,pn,dn,ps,ds, tolerance = 0):

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
        A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds)
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
        A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds)
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
            A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds)
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
            A, pn, dn, ps, ds = full_pivot(A, i, j, pn, dn, ps, ds)
            dtest = find(np.logical_and(ds == 0, A[0, 1:] < 0))
    elif ptest.size > 0 and dtest.size > 0:
        B = np.zeros((mm+1,nn+1))
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
            B, pn, dn, ps, ds = full_pivot(B, i, j, pn, dn, ps, ds)
            mat = np.divide(-B[0, 1:-1], B[-1, 1:-1], out=np.zeros_like(B[0, 1:-1]), where=np.logical_and(B[-1, 1:-1] > 0, ds != 1))
            j = np.argmax(mat)
            mu1 = mat[j]
            mat = np.divide(-B[1:-1, 0], B[1:-1, -1], out=np.zeros_like(B[1:-1, 0]), where=np.logical_and(B[1:-1, -1] > 0, ps != 1))
            i = np.argmax(mat)
            mu2 = mat[i]
            mu = max(mu1, mu2)
        A = B[:-1, :-1]
    return A, pn, dn, ps, ds, err