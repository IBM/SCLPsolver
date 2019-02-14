import numpy as np

def base_pivot(A, i, j):
    i = i + 1
    j = j + 1
    p = A[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = (A[i,:] / p).copy()
    c = A[:, j].copy()
    A -= np.dot(np.reshape(c, (np.size(c), 1)), np.reshape(rp, (1, np.size(rp))))
    A[i,:] = rp
    A[:, j] = c / -p
    A[i, j] = 1. / p
    return A


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
    rp = (A[i,:] / p).copy()
    c = A[:, j].copy()
    A -= np.dot(np.reshape(c,(np.size(c),1)), np.reshape(rp, (1, np.size(rp))))
    A[i,:] = rp
    A[:, j] = c / -p
    A[i, j] = 1. / p
    return A, pn, dn, ps, ds

def dict_pivot(dct, i, j):
    nam = dct['prim_name'][i]
    dct['prim_name'][i] = dct['dual_name'][j]
    dct['dual_name'][j] = nam
    i = i + 1
    j = j + 1
    p = dct['A'][i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = (dct['A'][i, :] / p).copy()
    c = dct['A'][:, j].copy()
    dct['A'] -= np.dot(np.reshape(c,(np.size(c),1)), np.reshape(rp, (1, np.size(rp))))
    dct['A'][i, :] = rp
    dct['A'][:, j] = c / -p
    dct['A'][i, j] = 1. / p
    return dct