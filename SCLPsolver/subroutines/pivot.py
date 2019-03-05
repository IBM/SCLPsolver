import numpy as np
#from scipy.linalg.blas import dger


#'#@profile
def base_pivot(A, i, j):
    i = i + 1
    j = j + 1
    p = A[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = A[i,:] / p
    c = A[:, j].copy()
    A -= np.outer(c, rp)
    A[i,:] = rp
    A[:, j] = c / -p
    A[i, j] = 1. / p
    return A


#'#@profile
def full_pivot(A, i, j, pn, dn, ps, ds):
    nam = pn[i]
    pn[i] = dn[j]
    dn[j] = nam
    sam = ps[i]
    ps[i] = - ds[j]
    ds[j] = - sam
    i = i + 1
    j = j + 1
    p = A[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = A[i,:] / p
    c = A[:, j].copy()
    A -= np.outer(c, rp)
    #A = dger(-1.0, c, rp, a=A, overwrite_a= 1)
    A[i,:] = rp
    A[:, j] = c / -p
    A[i, j] = 1. / p
    return A, pn, dn, ps, ds


#'#@profile
def dict_pivot(dct, i, j):
    nam = dct['prim_name'][i]
    dct['prim_name'][i] = dct['dual_name'][j]
    dct['dual_name'][j] = nam
    i = i + 1
    j = j + 1
    p = dct['A'][i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = dct['A'][i, :] / p
    c = dct['A'][:, j].copy()
    dct['A'] -= np.outer(c, rp)
    dct['A'][i, :] = rp
    dct['A'][:, j] = c / -p
    dct['A'][i, j] = 1. / p
    return dct