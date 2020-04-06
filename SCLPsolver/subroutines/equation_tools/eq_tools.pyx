# cython: infer_types=True
#cython: language_level=3


from cython.parallel import prange
cimport cython



def add_cols(double[:, ::1] result, double[:, :] dx, double[:, :] dq, int[:] nums, int[:] names, int start_row,
                int end_row, int start_col, int end_col, int icorr, int jcorr):
    cdef int i, j, test_col, num
    if start_col + jcorr == 0:
        test_col = end_col
    else:
        test_col = start_col - 1
    for i in prange(start_row, end_row, nogil=True):
        num = nums[i + icorr]
        if names[i + icorr] > 0:
            if result[i, test_col] != 0.:
                for j in range(start_col, end_col):
                    result[i, j] = dx[num, j + jcorr]
            else:
                for j in range(start_col, end_col):
                    result[i, j] = 0.
        else:
            if result[i, test_col] != 0.:
                for j in range(start_col, end_col):
                    result[i, j] = dq[num, j + jcorr]
            else:
                for j in range(start_col, end_col):
                    result[i, j] = 0.

from libc.stdio cimport printf
def add_cols2(double[:, ::1] result, double[:, :] dx, double[:, :] dq, int[:] nums, int[:] names, int start_row,
                int end_row, int start_col, int end_col, int icorr, int jcorr):
    cdef int i, j, test_col1, test_col2, num
    test_col1 = end_col + jcorr
    test_col2 = start_col + jcorr - 1
    for i in prange(start_row, end_row, nogil=True):
        if result[i, end_col] != 0. or result[i, start_col - 1] != 0.:
            num = nums[i + icorr]
            if names[i + icorr] > 0:
                for j in range(start_col, end_col):
                    result[i, j] = dx[num, j + jcorr]

            else:
                for j in range(start_col, end_col):
                    result[i, j] = dq[num, j + jcorr]
        else:
            for j in range(start_col, end_col):
                result[i, j] = 0.

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline int find(int what, int[::1] where, int i_start, Py_ssize_t i_max) nogil:
    cdef int i
    for i in range(i_start, i_max):
        if where[i] == what:
            return i
    return -1

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline int find_back(int what, int[::1] where, int i_start, Py_ssize_t i_max) nogil:
    cdef int i
    for i in range(i_max-1, i_start-1, -1):
        if where[i] == what:
            return i
    return -1


import numpy as np
@cython.boundscheck(False)
@cython.wraparound(False)
def build_equations(int[::1] klist, int[::1] jlist, int[::1] outpivots, int[::1] inpivots, double[:, :] dx, double[:, :] dq):
    cdef Py_ssize_t NN = outpivots.shape[0] + 1
    cdef int n, vv, k, j, i, prev_in, next_in
    result = np.zeros((NN, NN), dtype=np.double, order='C')
    cdef double[:,::1] res_view = result
    nvar_nums = np.zeros(NN, dtype=np.int32, order='C')
    nvar_names = np.zeros(NN, dtype=np.int32, order='C')
    cdef int[::1] var_nums = nvar_nums
    cdef int[::1] var_names = nvar_names
    for n in prange(NN - 1, nogil =True):
        vv = outpivots[n]
        if vv > 0:
            k = find(vv, klist, 0, klist.shape[0])
            var_nums[n] = k
            prev_in = find_back(vv, inpivots, 0, n)
            for i in range(prev_in + 1, n + 1):
                res_view[n, i] = dx[k, i]
            if prev_in > -1:
                var_names[n] = 0
            else:
                var_names[n] = vv
        else:
            j = find(-vv, jlist, 0, jlist.shape[0])
            var_nums[n] = j
            next_in = find(vv, inpivots, n, NN)
            if next_in > -1:
                for i in range(n + 1, next_in + 1):
                    res_view[n, i] = dq[j, i]
                    var_names[n] = 0
            else:
                for i in range(n + 1, NN):
                    res_view[n, i] = dq[j, i]
                    var_names[n] = vv
    for i in range(NN):
        res_view[NN-1, i] = 1.
    return result, nvar_names, nvar_nums

