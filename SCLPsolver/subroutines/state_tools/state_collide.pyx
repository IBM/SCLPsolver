# cython: infer_types=True
# distutils: language = c++
#cython: language_level=3
#cython: boundscheck=False
#cython: wraparound=False

from cython.parallel import prange
cimport cython
from libcpp.vector cimport vector
from libcpp cimport bool
cdef inline double __calc_dstate_prim(double[:, ::1] dv, int from_, double[:] dtau, double[:,::1] dstate_view, int i,
 int x_1, bool first, int dfrom, vector[bool] found_min) nogil:
    cdef int j, dv_idx
    if not found_min[i]:
        for j in range(dfrom, dfrom+x_1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                dstate_view[i, j+1] = dv[i, dv_idx]  * dtau[j] +  dstate_view[i, j]
            else:
                dstate_view[i, j+1] = dstate_view[i, j]
    return dstate_view[i, x_1]

cdef inline double __calc_state_ratio_prim(double[:, ::1] dv, int from_, double[:] tau, double[:,::1] state_view, int x_1, int i,
 double val, int dfrom, vector[bool] found_min) nogil:
    cdef int j, dv_idx
    if not found_min[i]:
        for j in range(dfrom, dfrom+x_1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                state_view[i, j+1] = dv[i, dv_idx]  * tau[j] +  state_view[i, j]
            else:
                state_view[i, j+1] = state_view[i, j]
        found_min[i] = True
    return -val / state_view[i, x_1]

def calc_state_ratio_prim(double[:, ::1] dv, int from_, int to_, double[:] tau, double[:] dtau, double[::1] state0,
 double[::1] dstate0, list loc_mins, list lens, double[:,::1] dstate_view, double[:,::1] state_view, int dfrom):
    i_max = dv.shape[0]
    cdef int y, i, x, y_max, j_max = to_ - from_, r_ind = -1, c_ind = -1, x_max = <int>len(loc_mins)
    cdef int[:] lmin
    cdef vector[int] vlens = lens
    cdef double val, max_val = 0.
    cdef vector[double] r_val
    cdef vector[int] r_idx
    cdef vector[bool] found_dstate_min = vector[bool](i_max, False)
    cdef vector[bool] found_state_min = vector[bool](i_max, False)
    cdef bool first = True
    if dstate0 is not None:
        for i in range(i_max):
            dstate_view[i, dfrom] = dstate0[i]
    if state0 is not None:
        for i in range(i_max):
            state_view[i, dfrom] = state0[i]
    for x in range(x_max-1, -1, -1):
        y_max = vlens[x]
        if y_max > 0:
            lmin = loc_mins[x]
            if y_max == 1:
                i = lmin[0]
                val = __calc_dstate_prim(dv, from_, dtau, dstate_view, i, x+1, first, dfrom, found_dstate_min)
                if val < 0:
                    val = __calc_state_ratio_prim(dv, from_, tau, state_view, x+1, i, val, dfrom, found_state_min)
                    if val > max_val:
                        r_ind = i
                        c_ind = x
                        max_val = val
                found_dstate_min[i] = True
            else:
                r_val = vector[double](y_max)
                r_idx = vector[int](y_max)
                for y in prange(y_max, nogil=True):
                    i = lmin[y]
                    val = __calc_dstate_prim(dv, from_, dtau, dstate_view, i, x+1, first, dfrom, found_dstate_min)
                    if val < 0:
                        val = __calc_state_ratio_prim(dv, from_, tau, state_view, x+1, i, val, dfrom, found_state_min)
                        if val > r_val[y]:
                            r_val[y] = val
                            r_idx[y] = i
                    found_dstate_min[i] = True
                for y in range(y_max):
                    if r_val[y] > max_val:
                        max_val = r_val[y]
                        r_ind = r_idx[y]
                        c_ind = x
            first = False
    return max_val, r_ind, c_ind

cdef inline double __calc_dstate_dual(double[:, ::1] dv, int from_, double[:] dtau, double[:,::1] dstate_view, int i,
 int x, int j_max, bool first, int dfrom, vector[bool] found_min) nogil:
    cdef int j, dv_idx
    if not found_min[i]:
        for j in range(dfrom+j_max-1, dfrom+x-1, -1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                dstate_view[i, j] = dv[i, dv_idx]  * dtau[j] +  dstate_view[i, j+1]
            else:
                dstate_view[i, j] = dstate_view[i, j+1]
    return dstate_view[i, x]

cdef inline double __calc_state_ratio_dual(double[:, ::1] dv, int from_, double[:] tau, double[:,::1] state_view, int x, int i,
 int j_max, double val, int dfrom, vector[bool] found_min) nogil:
    cdef int j, dv_idx
    if not found_min[i]:
        for j in range(dfrom+j_max-1, dfrom+x-1, -1):
            dv_idx = j + from_
            if dv[i, dv_idx] != 0.:
                state_view[i, j] = dv[i, dv_idx]  * tau[j] +  state_view[i, j+1]
            else:
                state_view[i, j] = state_view[i, j+1]
        found_min[i] = True
    return -val / state_view[i, x]

def calc_state_ratio_dual(double[:, ::1] dv, int from_, int to_, double[:] tau, double[:] dtau, double[::1] state0,
 double[::1] dstate0, list loc_mins, list lens, double[:,::1] dstate_view, double[:,::1] state_view, int dfrom):
    i_max = dv.shape[0]
    cdef int y, i, x, y_max, j_max = to_ - from_, r_ind = -1, c_ind = -1, x_max = <int>len(loc_mins)
    cdef int[:] lmin
    cdef vector[int] vlens = lens
    cdef double val, max_val = 0.
    cdef vector[double] r_val
    cdef vector[int] r_idx
    cdef vector[bool] found_dstate_min = vector[bool](i_max, False)
    cdef vector[bool] found_state_min = vector[bool](i_max, False)
    cdef bool first = True
    if dstate0 is not None:
        for i in range(i_max):
            dstate_view[i, dfrom+j_max] = dstate0[i]
    else:
        for i in range(i_max):
            dstate_view[i, dfrom+j_max] = 0.
    if state0 is not None:
        for i in range(i_max):
            state_view[i, dfrom+j_max] = state0[i]
    else:
        for i in range(i_max):
            state_view[i, dfrom+j_max] = 0.
    for x in range(x_max):
        y_max = vlens[x]
        if y_max > 0:
            lmin = loc_mins[x]
            if y_max == 1:
                i = lmin[0]
                val = __calc_dstate_dual(dv, from_, dtau, dstate_view, i, x, j_max, first, dfrom, found_dstate_min)
                if val < 0:
                    val = __calc_state_ratio_dual(dv, from_, tau, state_view, x, i, j_max, val, dfrom, found_state_min)
                    if val > max_val:
                        r_ind = i
                        c_ind = x
                        max_val = val
                found_dstate_min[i] = True
            else:
                r_val = vector[double](y_max)
                r_idx = vector[int](y_max)
                for y in prange(y_max, nogil=True):
                    i = lmin[y]
                    val = __calc_dstate_dual(dv, from_, dtau, dstate_view, i, x, j_max, first, dfrom, found_dstate_min)
                    if val < 0:
                        val = __calc_state_ratio_dual(dv, from_, tau, state_view, x, i, j_max, val, dfrom, found_state_min)
                        if val > r_val[y]:
                            r_val[y] = val
                            r_idx[y] = i
                    found_dstate_min[i] = True
                for y in range(y_max):
                    if r_val[y] > max_val:
                        max_val = r_val[y]
                        r_ind = r_idx[y]
                        c_ind = x
            first = False
    return max_val, r_ind, c_ind