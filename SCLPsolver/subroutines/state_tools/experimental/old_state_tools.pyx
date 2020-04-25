@cython.boundscheck(False)
@cython.wraparound(False)
def cy_calc_state(double[:, ::1] dx, int from_x, int to_x, double[:, ::1] dq, int from_q, int to_q, double[:] tau,
 double[:] dtau, double[::1] x_0, double[::1] del_x_0, double[::1] q_N, double[::1] del_q_N, double[:,::1] x,
  double[:,::1] del_x, double[:,::1] q, double[:,::1] del_q, bint checked = False):
    cdef int i
    for i in prange(4, nogil=True, num_threads = 4):
        if i==0:
            calc_state_prim1(dx, from_x, to_x, tau, x_0, x, checked)
        elif i==1:
            calc_state_prim1(dx, from_x, to_x, dtau, del_x_0, del_x, checked)
        elif i==2:
            calc_state_dual1(dq, from_q, to_q, tau, q_N, q, checked)
        else:
            calc_state_dual1(dq, from_q, to_q, dtau, del_q_N, del_q, checked)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void calc_state_prim1(double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0, double[:,::1] result,
 bint checked = False) nogil:
    cdef int j_max
    cdef Py_ssize_t i, j
    i_max = dv.shape[0]
    j_max = to_ - from_
    if state0 is not None:
        for i in range(i_max):
            result[i, 0] = state0[i]
    for i in prange(i_max, num_threads = 4):
        for j in range(j_max):
            if dv[i, j + from_] != 0. or checked:
                result[i, j+1] = dv[i, j + from_]  * tau[j] +  result[i, j]

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void calc_state_dual1(double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0, double[:,::1] result,
 bint checked = False) nogil:
    cdef int j_max
    cdef Py_ssize_t i, j
    i_max = dv.shape[0]
    j_max = to_ - from_
    if state0 is not None:
        for i in range(i_max):
            result[i, j_max] = state0[i]
    for i in prange(i_max, num_threads = 4):
        for j in range(j_max-1, -1, -1):
            if dv[i, j + from_] != 0. or checked:
                result[i, j] = dv[i, j + from_]  * tau[j] +  result[i, j+1]

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_state_partial_prim(double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0, list loc_mins, list lens):
    i_max = dv.shape[0]
    cdef int y, y_max, j_max = to_ - from_
    cdef Py_ssize_t i, j, x, x_max = len(loc_mins)
    cdef int[:] lmin
    cdef vector[int] vlens = lens
    result = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef double[:,::1] result_view = result
    if state0 is not None:
        for i in range(i_max):
            result_view[i, 0] = state0[i]
    for x in range(x_max-1, -1, -1):
        y_max = vlens[x]
        if y_max > 0:
            lmin = loc_mins[x]
            for y in prange(y_max, nogil=True):
                i = lmin[y]
                if x == x_max-1 or result_view[i, x+1] == 0.:
                    for j in range(x+1):
                        if dv[i, j + from_] != 0.:
                            result_view[i, j+1] = dv[i, j + from_]  * tau[j] +  result_view[i, j]
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_state_partial_dual(double[:, ::1] dv, int from_, int to_, double[:] tau, double[::1] state0, list loc_mins, list lens):
    i_max = dv.shape[0]
    cdef int y, y_max, j_max = to_ - from_
    cdef Py_ssize_t i, j, x, x_max = len(loc_mins)
    cdef int[:] lmin
    cdef vector[int] vlens = lens
    result = np.zeros((i_max, j_max+1), dtype= np.float64, order='C')
    cdef double[:,::1] result_view = result
    if state0 is not None:
        for i in range(i_max):
            result_view[i, j_max] = state0[i]
    for x in range(x_max):
        y_max = vlens[x]
        if y_max > 0:
            lmin = loc_mins[x]
            for y in prange(y_max, nogil=True):
                i = lmin[y]
                if x == 0 or result_view[i, x-1] == 0.:
                    for j in range(j_max-1, x-1, -1):
                        if dv[i, j + from_] != 0.:
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