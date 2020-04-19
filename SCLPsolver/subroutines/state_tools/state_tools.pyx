# cython: infer_types=True
# distutils: language = c++
#cython: language_level=3

from cython.parallel import prange
import numpy as np
cimport cython
from libcpp.vector cimport vector

@cython.boundscheck(False)
@cython.wraparound(False)
def get_prim_loc_mins(double[:,:] v):
    x_max = v.shape[0]
    y_max = v.shape[1]
    len_res = np.zeros(y_max-1, dtype=np.int32, order='C')
    cdef int[::1] len_res_view = len_res
    result = np.zeros((x_max, y_max-1), dtype=np.int32, order='F')
    cdef int[::1, :] result_view = result
    cdef int i, j, y
    for y in prange(y_max-1, nogil=True):
        j=0
        for i in range(x_max):
            if v[i,y] < 0 and v[i,y+1] > 0:
                result_view[j,y] = i
                j = j + 1
        len_res_view[y] = j
    return result, len_res

@cython.boundscheck(False)
@cython.wraparound(False)
def get_dual_loc_mins(double[:,:] v):
    x_max = v.shape[0]
    y_max = v.shape[1]
    len_res = np.zeros(y_max-1, dtype=np.int32, order='C')
    cdef int[::1] len_res_view = len_res
    result = np.zeros((x_max, y_max-1), dtype=np.int32, order='F')
    cdef int[::1, :] result_view = result
    cdef int i, j, y
    for y in prange(y_max-1, nogil=True):
        j=0
        for i in range(x_max):
            if v[i,y] > 0 and v[i,y+1] < 0:
                result_view[j,y] = i
                j = j + 1
        len_res_view[y] = j
    return result, len_res

@cython.boundscheck(False)
@cython.wraparound(False)
def get_loc_min(double[:] v1, double[:] v2):
    x_max = v1.shape[0]
    result = np.zeros(x_max, dtype=np.int32)
    cdef int[:] result_view = result
    cdef int i, j
    j=0
    for i in range(x_max):
        if v1[i] < 0 and v2[i] > 0:
            result_view[j] = i
            j+=1
    return result[:j]

@cython.boundscheck(False)
@cython.wraparound(False)
def get_right_loc_min(double[:] v1):
    x_max = v1.shape[0]
    result = np.zeros(x_max, dtype=np.int32, order='C')
    cdef int[::1] result_view = result
    cdef int i, j
    j=0
    for i in range(x_max):
        if v1[i] < 0:
            result_view[j] = i
            j+=1
    return result[:j]

@cython.boundscheck(False)
@cython.wraparound(False)
def get_left_loc_min(double[:] v1):
    x_max = v1.shape[0]
    result = np.zeros(x_max, dtype=np.int32, order='C')
    cdef int[::1] result_view = result
    cdef int i, j
    j=0
    for i in range(x_max):
        if v1[i] > 0:
            result_view[j] = i
            j+=1
    return result[:j]

@cython.boundscheck(False)
@cython.wraparound(False)
def get_rz_bb(double[:, :] del_state, double[:, :] state, list loc_mins, list lens):
    cdef vector[int] vlens = lens
    cdef Py_ssize_t x_max = len(loc_mins)
    cdef int[:] lmin
    cdef int r_ind = -1, c_ind = -1, j_max, ind, i, j
    cdef double max_val = 0., val
    for i in range(x_max):
        j_max = vlens[i]
        lmin = loc_mins[i]
        for j in range(j_max):
            ind = lmin[j]
            val = del_state[ind, i]
            if val < 0.:
                val = -val / state[ind, i]
                if val > max_val:
                    r_ind = ind
                    c_ind = i
                    max_val = val
    return max_val, r_ind, c_ind


@cython.boundscheck(False)
@cython.wraparound(False)
def calc_state_prim(double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0, bint checked = False):
    i_max = dv.shape[0]
    cdef int j_max = to_ - from_
    cdef Py_ssize_t i, j
    result = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef double[:,::1] result_view = result
    if state0 is not None:
        for i in range(i_max):
            result_view[i, 0] = state0[i]
    for i in prange(i_max, nogil=True):
        for j in range(j_max):
            if dv[i, j + from_] != 0. or checked:
                result_view[i, j+1] = dv[i, j + from_]  * tau[j] +  result_view[i, j]
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_state_dual(double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0, bint checked = False):
    i_max = dv.shape[0]
    cdef int j_max = to_ - from_
    cdef Py_ssize_t i, j
    result = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef double[:,::1] result_view = result
    if state0 is not None:
        for i in range(i_max):
            result_view[i, j_max] = state0[i]
    for i in prange(i_max, nogil=True):
        for j in range(j_max-1, -1, -1):
            if dv[i, j + from_] != 0. or checked:
                result_view[i, j] = dv[i, j + from_]  * tau[j] +  result_view[i, j+1]
    return result

from libcpp cimport bool
@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double _calc_dstate_prim(double[:, ::1] dv, int from_, double[:] dtau, double[:,::1] dstate_view, int i,
 int x_1, bool first) nogil:
    cdef int j, dv_idx
    if first or dstate_view[i, x_1] == 0.:
        for j in range(x_1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                dstate_view[i, j+1] = dv[i, dv_idx]  * dtau[j] +  dstate_view[i, j]
    return dstate_view[i, x_1]

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double _calc_state_ratio_prim(double[:, ::1] dv, int from_, double[:] tau, double[:,::1] state_view, int x_1, int i,
 double val) nogil:
    cdef int j, dv_idx
    if state_view[i, x_1] == 0.:
        for j in range(x_1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                state_view[i, j+1] = dv[i, dv_idx]  * tau[j] +  state_view[i, j]
    return -val / state_view[i, x_1]

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_rz_bb_prim(double[:, ::1] dv, int from_, int to_, double[:] tau, double[:] dtau, double[::1] state0,
 double[::1] dstate0, list loc_mins, list lens):
    i_max = dv.shape[0]
    cdef int y, i, x, y_max, j_max = to_ - from_, r_ind = -1, c_ind = -1, x_max = <int>len(loc_mins)
    cdef int[:] lmin
    cdef vector[int] vlens = lens
    cdef double val, max_val = 0.
    cdef vector[double] r_val
    cdef vector[int] r_idx
    cdef double[:,::1] dstate_view = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef double[:,::1] state_view = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef bool first = True
    if dstate0 is not None:
        for i in range(i_max):
            dstate_view[i, 0] = dstate0[i]
    if state0 is not None:
        for i in range(i_max):
            state_view[i, 0] = state0[i]
    for x in range(x_max-1, -1, -1):
        y_max = vlens[x]
        if y_max > 0:
            lmin = loc_mins[x]
            if y_max == 1:
                i = lmin[0]
                val = _calc_dstate_prim(dv, from_, dtau, dstate_view, i, x+1, first)
                if val < 0:
                    val = _calc_state_ratio_prim(dv, from_, tau, state_view, x+1, i, val)
                    if val > max_val:
                        r_ind = i
                        c_ind = x
                        max_val = val
            else:
                r_val = vector[double](y_max)
                r_idx = vector[int](y_max)
                for y in prange(y_max, nogil=True):
                    i = lmin[y]
                    val = _calc_dstate_prim(dv, from_, dtau, dstate_view, i, x+1, first)
                    if val < 0:
                        val = _calc_state_ratio_prim(dv, from_, tau, state_view, x+1, i, val)
                        if val > r_val[y]:
                            r_val[y] = val
                            r_idx[y] = i
                for y in range(y_max):
                    if r_val[y] > max_val:
                        max_val = r_val[y]
                        r_ind = r_idx[y]
                        c_ind = x
            first = False
    return max_val, r_ind, c_ind

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double _calc_dstate_dual(double[:, ::1] dv, int from_, double[:] dtau, double[:,::1] dstate_view, int i,
 int x, int j_max, bool first) nogil:
    cdef int j, dv_idx
    if first or dstate_view[i, x-1] == 0.:
        for j in range(j_max-1, x-1, -1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                dstate_view[i, j] = dv[i, dv_idx]  * dtau[j] +  dstate_view[i, j+1]
    return dstate_view[i, x]

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double _calc_state_ratio_dual(double[:, ::1] dv, int from_, double[:] tau, double[:,::1] state_view, int x, int i,
 int j_max, double val) nogil:
    cdef int j, dv_idx
    if state_view[i, x] == 0.:
        for j in range(j_max-1, x-1, -1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                state_view[i, j] = dv[i, dv_idx]  * tau[j] +  state_view[i, j+1]
    return -val / state_view[i, x]

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_rz_bb_dual(double[:, ::1] dv, int from_, int to_, double[:] tau, double[:] dtau, double[::1] state0,
 double[::1] dstate0, list loc_mins, list lens):
    i_max = dv.shape[0]
    cdef int y, i, x, y_max, j_max = to_ - from_, r_ind = -1, c_ind = -1, x_max = <int>len(loc_mins)
    cdef int[:] lmin
    cdef vector[int] vlens = lens
    cdef double val, max_val = 0.
    cdef vector[double] r_val
    cdef vector[int] r_idx
    cdef double[:,::1] dstate_view = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef double[:,::1] state_view = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef bool first = True
    if dstate0 is not None:
        for i in range(i_max):
            dstate_view[i, j_max] = dstate0[i]
    if state0 is not None:
        for i in range(i_max):
            state_view[i, j_max] = state0[i]
    for x in range(x_max):
        y_max = vlens[x]
        if y_max > 0:
            lmin = loc_mins[x]
            if y_max == 1:
                i = lmin[0]
                val = _calc_dstate_dual(dv, from_, dtau, dstate_view, i, x, j_max, first)
                if val < 0:
                    val = _calc_state_ratio_dual(dv, from_, tau, state_view, x, i, j_max, val)
                    if val > max_val:
                        r_ind = i
                        c_ind = x
                        max_val = val
            else:
                r_val = vector[double](y_max)
                r_idx = vector[int](y_max)
                for y in prange(y_max, nogil=True):
                    i = lmin[y]
                    val = _calc_dstate_dual(dv, from_, dtau, dstate_view, i, x, j_max, first)
                    if val < 0:
                        val = _calc_state_ratio_dual(dv, from_, tau, state_view, x, i, j_max, val)
                        if val > r_val[y]:
                            r_val[y] = val
                            r_idx[y] = i
                for y in range(y_max):
                    if r_val[y] > max_val:
                        max_val = r_val[y]
                        r_ind = r_idx[y]
                        c_ind = x
            first = False
    return max_val, r_ind, c_ind

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_specific_state_prim(int n, int k, double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0):
    cdef Py_ssize_t i
    cdef double result = 0
    if state0 is not None:
        result = state0[k]
    for i in range(n):
        if dv[k, i + from_] != 0.:
            result += dv[k, i + from_]  * tau[i]
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_specific_state_dual(int n, int j, double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0):
    cdef Py_ssize_t i
    cdef double result = 0
    cdef int j_max = to_ - from_
    if state0 is not None:
        result = state0[j]
    for i in range(j_max-1, n-1, -1):
        if dv[j, i + from_] != 0.:
            result += dv[j, i + from_]  * tau[i]
    return result
