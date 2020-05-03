# cython: infer_types=True
#cython: language_level=3



from cython.parallel import prange
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
def cy_pivot(double[:, ::1] dct, int[::1] pn, int[::1] dn, int i, int j):
    cdef int out_, in_
    out_ = pn[i]
    in_ = dn[j]
    pn[i] = in_
    dn[j] = out_
    i += 1
    j += 1
    cdef double p
    p = dct[i, j]
    x_max = dct.shape[0]
    y_max = dct.shape[1]
    cdef Py_ssize_t x, y
    if p != 1.:
        for y in range(y_max):
            dct[i,y] /= p
    for x in prange(x_max, nogil=True):
        if x != i:
            if dct[x, j] != 0.:
                for y in range(y_max):
                    if y != j:
                        if dct[i,y] != 0.:
                            dct[x, y] -= dct[x, j] * dct[i,y]
    if p == 1.:
        for x in range(x_max):
            dct[x, j] = -dct[x, j]
        dct[i, j] = 1.
    else:
        for x in range(x_max):
            dct[x, j] /= -p
        dct[i, j] = 1. / p
    return in_, out_

@cython.boundscheck(False)
@cython.wraparound(False)
def copy_pivot(double[:, ::1] dct, int[::1] pn, int[::1] dn, int i, int j, double[:, ::1] res):
    cdef int out_, in_
    out_ = pn[i]
    in_ = dn[j]
    pn[i] = in_
    dn[j] = out_
    x_max = dct.shape[0]
    y_max = dct.shape[1]
    cdef Py_ssize_t x, y
    i += 1
    j += 1
    cdef double p
    p = dct[i, j]
    if p != 1.:
        for y in range(y_max):
            res[i,y] = dct[i,y] / p
    else:
        for y in range(y_max):
            res[i,y] = dct[i,y]
    for x in prange(x_max, nogil=True):
        if x != i:
            for y in range(y_max):
                if y != j:
                    res[x, y] = dct[x, y] - dct[x, j] * res[i,y]
    if p == 1.:
        for x in range(x_max):
            res[x, j] = -dct[x, j]
        res[i, j] = 1.
    else:
        for x in range(x_max):
            res[x, j] = dct[x, j] / -p
        res[i, j] = 1. / p
    return in_, out_

import numpy as np
@cython.boundscheck(False)
@cython.wraparound(False)
def get_sign(int[::1] name, int[::1] k_set, int[::1] nj_set, int sign):
    x_max = name.shape[0]
    k_max = k_set.shape[0]
    j_max = nj_set.shape[0]
    result = np.zeros(x_max, dtype=np.int32, order='C')
    cdef int[::1] result_view = result
    cdef int i, k, j
    for i in prange(x_max, nogil=True):
        if name[i] > 0:
            for k in range(k_max):
                if name[i] == k_set[k]:
                    result_view[i] = sign
                    break
        else:
            for j in range(j_max):
                if name[i] == nj_set[j]:
                    result_view[i] = -sign
                    break
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def get_sign1(int[::1] name, int[::1] k_set, int[::1] nj_set, int sign, int[::1] result_view):
    x_max = name.shape[0]
    k_max = k_set.shape[0]
    j_max = nj_set.shape[0]
    cdef int i, k, j
    for i in prange(x_max, nogil=True):
        result_view[i] = 0
        if name[i] > 0:
            for k in range(k_max):
                if name[i] == k_set[k]:
                    result_view[i] = sign
                    break
        else:
            for j in range(j_max):
                if name[i] == nj_set[j]:
                    result_view[i] = -sign
                    break



@cython.boundscheck(False)
@cython.wraparound(False)
def prim_ratio_test(double[:, ::1] dct, int i, int[::1] ds):
    cdef int j, ind = -1
    cdef double val, amax = 0
    x_max = ds.shape[0] +1
    i+=1
    for j in range(1, x_max):
        if ds[j-1]!= 1 and dct[i, j] < 0:
            if dct[0, j] == 0:
                return j
            else:
                val = -dct[i, j]/dct[0, j]
                if val > amax:
                    amax = val
                    ind = j
    return ind

@cython.boundscheck(False)
@cython.wraparound(False)
def dual_ratio_test(double[:, ::1] dct, int j, int[::1] ps):
    cdef int i, ind = -1
    cdef double val, amax = 0
    x_max = ps.shape[0] +1
    j+=1
    for i in range(1, x_max):
        if ps[i-1]!= 1 and dct[i, j] > 0:
            if dct[i, 0] == 0:
                return i
            else:
                val = dct[i, j]/dct[i, 0]
                if val > amax:
                    amax = val
                    ind = i
    return ind


@cython.boundscheck(False)
@cython.wraparound(False)
def copy_pivot2(double[:, :, ::1] dct, int[::1] pn, int[::1] dn, int i, int j, int start, int target):
    cdef int out_, in_
    out_ = pn[i]
    in_ = dn[j]
    pn[i] = in_
    dn[j] = out_
    x_max = dct.shape[1]
    y_max = dct.shape[2]
    cdef Py_ssize_t x, y
    i += 1
    j += 1
    cdef double p
    p = dct[start, i, j]
    if p != 1.:
        for y in range(y_max):
            dct[target, i,y] = dct[start, i,y] / p
    else:
        for y in range(y_max):
            dct[target, i,y] = dct[start, i,y]
    for x in prange(x_max, nogil=True):
        if x != i:
            for y in range(y_max):
                if y != j:
                    dct[target, x,y] = dct[start, x, y] - dct[start, x, j] * dct[target, i,y]
    if p == 1.:
        for x in range(x_max):
            dct[target, x,j] = -dct[start, x, j]
        dct[target,i, j] = 1.
    else:
        for x in range(x_max):
            dct[target,x, j] = dct[start,x, j] / -p
        dct[target,i, j] = 1. / p
    return in_, out_

from libc.string cimport memcpy
@cython.boundscheck(False)
@cython.wraparound(False)
def copy_pivot3(double[:, ::1] dct, int[::1] pn, int[::1] dn, int i, int j, double[:, ::1] res):
    cdef int out_, in_
    out_ = pn[i]
    in_ = dn[j]
    pn[i] = in_
    dn[j] = out_
    x_max = dct.shape[0]
    y_max = dct.shape[1]
    memcpy(&res[0,0], &dct[0,0], 8*x_max*y_max)
    cdef Py_ssize_t x, y
    i += 1
    j += 1
    cdef double p = dct[i,j]
    if p != 1.:
        for y in range(y_max):
            res[i,y] /= p
    for x in prange(x_max, nogil=True):
        if x != i:
            if res[x, j] != 0.:
                for y in range(y_max):
                    if y != j:
                        if res[i,y] != 0.:
                            res[x, y] -= res[x, j] * res[i,y]
    if p == 1.:
        for x in range(x_max):
            res[x, j] = -res[x, j]
        res[i, j] = 1.
    else:
        for x in range(x_max):
            res[x, j] /= -p
        res[i, j] = 1. / p
    return in_, out_