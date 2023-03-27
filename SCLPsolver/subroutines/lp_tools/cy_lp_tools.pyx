# cython: infer_types=True
#cython: language_level=3


import numpy as np
from cython.parallel import prange
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline int do_partial_pivot(double[:, ::1] dct, int[::1] pn, int[::1] dn, int[::1] ps, int[::1] ds,
 double[::1] prim_v, double[::1] dual_v, int i, int j, Py_ssize_t x_max, Py_ssize_t y_max, double c , double r) nogil:
    cdef int x, y
    if pn[i-1] > 0 and c < 0:
        return 0
    if dn[j-1] < 0 and r < 0:
        return 0
    for y in range(1, y_max):
        dual_v[y] = dct[0, y] + c * dct[i, y]
        if ds[y-1] == 0 and dual_v[y] < 0:
            if y != j:
               return 0
    dual_v[j] = c
    for x in range(1, x_max):
        prim_v[x] = dct[x, 0] - r * dct[x, j]
        if ps[x-1] == 0 and prim_v[x] < 0:
            if x != i:
               return 0
    prim_v[i] = r
    return 1

@cython.boundscheck(False)
@cython.wraparound(False)
def partial_pivotII(double[:, ::1] dct, int[::1] pn, int[::1] dn, int[::1] ps, int[::1] ds, int v_in, int v_out1, int v_out2):
    cdef int j, i=0, index = -1, in_idx, out_idx1=-1, out_idx2=-1
    x_max = dct.shape[0]
    y_max = dct.shape[1]
    for j in range(y_max-1):
        if dn[j] == v_in:
            in_idx = j
            break
    for i in range(x_max-1):
        if pn[i] == v_out1:
            out_idx1 = i
            if out_idx2 != -1:
                break
        elif pn[i] == v_out2:
            out_idx2 = i
            if out_idx1 != -1:
                break
    j = in_idx + 1
    cdef double p1, p2, r, c, rate1 =-1., rate2 = -1.
    prim_vars = np.empty(x_max, dtype=np.double, order='C')
    dual_vars = np.empty(y_max, dtype=np.double, order='C')
    cdef double[::1] prim_v = prim_vars
    cdef double[::1] dual_v = dual_vars
    cdef int x, y, ok = 0
    p1 = dct[out_idx1 + 1, j]
    p2 = dct[out_idx2 + 1, j]
    if p1 != 0:
        rate1 =  -dct[0, j] * dct[out_idx1 + 1, 0] / p1
    if p2 != 0:
        rate2 =  -dct[0, j] * dct[out_idx2 + 1, 0] / p2
    if rate1 >= rate2:
        if rate1 > 0.:
            i = out_idx1 + 1
            ok = do_partial_pivot(dct, pn, dn, ps, ds, prim_v, dual_v, i, j, x_max, y_max, -dct[0, j] / p1, dct[i, 0] / p1)
            if ok == 0:
                if rate2 > 0.:
                    i = out_idx2 + 1
                    ok = do_partial_pivot(dct, pn, dn, ps, ds, prim_v, dual_v, i, j, x_max, y_max, -dct[0, j] / p2, dct[i, 0] / p2)
    else:
        if rate2 > 0.:
            i = out_idx2 + 1
            ok = do_partial_pivot(dct, pn, dn, ps, ds, prim_v, dual_v, i, j, x_max, y_max, -dct[0, j] / p2, dct[i, 0] / p2)
            if ok == 0:
                if rate1 > 0.:
                    i = out_idx1 + 1
                    ok = do_partial_pivot(dct, pn, dn, ps, ds, prim_v, dual_v, i, j, x_max, y_max, -dct[0, j] / p1, dct[i, 0] / p1)
    return ok, prim_vars, dual_vars, i-1, j-1

def partial_ratio_test(double[:, ::1] dct, int[::1] dn, int[::1] ps, int v_in):
    cdef int j, i, index = -1, in_idx
    cdef double m = 1., v
    x_max = dct.shape[0]
    y_max = dct.shape[1]
    for j in range(y_max-1):
        if dn[j] == v_in:
            in_idx = j
            break
    if dct[0, j + 1] < 0:
        for i in range(x_max-1):
            if ps[i] != 1:
                if dct[i+1, 0] != 0.:
                    v = -dct[i+1, j + 1]/dct[i+1, 0]
                    if v > m:
                        m = v
                        index = i
                else:
                    if dct[i+1, j + 1] < 0:
                        m = -1
                        index = i
                        break
    else:
        for i in range(x_max-1):
            if ps[i] != 1:
                if dct[i+1, 0] != 0.:
                    v = -dct[i+1, j + 1]/dct[i+1, 0]
                    if v < m:
                        m = v
                        index = i
                else:
                    if dct[i+1, j + 1] > 0:
                        m = -1
                        index = i
                        break
    return index, in_idx, m

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
    """returns a vector of length the same as the variable-name vector, containing:
        0 when the variable is positive
        1 when the variable is non-restricted
        -1 when the variable is 0
    """
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

@cython.boundscheck(False)
@cython.wraparound(False)
def find_i(double[:, ::1] dct, int j, int[::1] ps, double tolerance):
    cdef int index = -1, i
    cdef double m = 1., v
    cdef Py_ssize_t i_max = ps.shape[0]
    if tolerance == 0.:
        for i in range(i_max):
            if ps[i] == -1:
                if dct[i+1,j+1] !=0.:
                    index = i
                    break
    else:
        for i in range(i_max):
            if ps[i] == -1:
                if abs(dct[i+1,j+1]) > tolerance:
                    index = i
                    break
    if index ==-1:
        if dct[0, j + 1] < 0:
            for i in range(i_max):
                if ps[i] != 1:
                    if dct[i+1, 0] != 0.:
                        v = dct[i+1, j + 1]/dct[i+1, 0]
                        if v > m:
                            m = v
                            index = i
                    else:
                        if dct[i+1, j + 1] < 0:
                            m = -1
                            index = i
                            break
        else:
            for i in range(i_max):
                if ps[i] != 1:
                    if dct[i+1, 0] != 0.:
                        v = -dct[i+1, j + 1]/dct[i+1, 0]
                        if v < m:
                            m = v
                            index = i
                    else:
                        if dct[i+1, j + 1] > 0:
                            m = -1
                            index = i
                            break
        if m > 0.:
            for i in range(i_max):
                if dct[i+1, j+1] != 0:
                    return i
    return index
