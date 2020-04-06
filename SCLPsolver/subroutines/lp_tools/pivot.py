import numpy as np
from .matlab_utils import find
from .pivot1 import cy_pivot
#from scipy.linalg.blas import dger


#'#@profile
def base_pivot(A, i, j, pn, dn, tmp):
    nam = pn[i]
    pn[i] = dn[j]
    dn[j] = nam
    i += 1
    j += 1
    p = A[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = A[i,:] / p
    c = A[:, j].copy()
    A -= np.outer(c, rp, out=tmp)
    A[i,:] = rp
    A[:, j] = c / -p
    A[i, j] = 1. / p
    return A, pn, dn

def base_pivot1(A,  pn, dn, i, j):
    cy_pivot(A, pn, dn, i, j)
    return A, pn, dn


#'#@profile
def full_pivot(A, i, j, pn, dn, ps, ds, tmp):
    nam = pn[i]
    pn[i] = dn[j]
    dn[j] = nam
    sam = ps[i]
    ps[i] = - ds[j]
    ds[j] = - sam
    i += 1
    j += 1
    p = A[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = A[i,:] / p
    c = A[:, j].copy()
    A -= np.outer(c, rp, out=tmp)
    #A = dger(-1.0, c, rp, a=A, overwrite_a= 1)
    A[i,:] = rp
    A[:, j] = c / -p
    A[i, j] = 1. / p
    return A, pn, dn, ps, ds

def ok(a, b):
    return all((m == n) or (m == 1) or (n == 1) for m, n in zip(a.shape[::-1], b.shape[::-1]))

#'#@profile
def dict_pivot(dct, i, j, tmp):
    nam = dct['prim_name'][i]
    dct['prim_name'][i] = dct['dual_name'][j]
    dct['dual_name'][j] = nam
    i += 1
    j += 1
    p = dct['A'][i, j]
    if p == 0:
        raise Exception('pivot on zero')
    if not ok(dct['A'][i, :], p):
        print("=========================================")
        print("dct[A][i,:].shape={}, p.shape={}".format(dct['A'][i, :].shape, p.shape))
        raise Exception("Bad shapes! dct[A][i,:].shape={}, p.shape={}".format(dct['A'][i, :].shape, p.shape))
    rp = dct['A'][i, :] / p
    c = dct['A'][:, j].copy()
    dct['A'] -= np.outer(c, rp, out=tmp)
    dct['A'][i, :] = rp
    dct['A'][:, j] = c / -p
    dct['A'][i, j] = 1. / p
    return dct

def pivot_ij(dct, i, j):
    cy_pivot(dct.simplex_dict, dct.prim_name, dct.dual_name, i, j)
    return dct

def pivot_mn(dct, m, n):
    i = find(dct.prim_name == m)
    j = find(dct.dual_name == n)
    if i.size != 1 or j.size != 1:
        raise Exception('Bad pivot names!')
    return pivot_ij(dct, i, j)

def signed_pivot_ij(dct, ps, ds, i, j):
    sam = ps[i]
    ps[i] = - ds[j]
    ds[j] = - sam
    return pivot_ij(dct, i, j), ps, ds

def signed_pivot_mn(dct, ps, ds, m, n):
    i = find(dct.prim_name == m)
    j = find(dct.dual_name == n)
    if i.size != 1 or j.size != 1:
        raise Exception('Bad pivot names!')
    return signed_pivot_ij(dct, ps, ds, i, j)