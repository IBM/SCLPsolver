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
def build_equations(int[::1] klist, int[::1] jlist, int[::1] outpivots, int[::1] inpivots, double[:, :] dx,
 double[:, :] dq, double[::1] x_0, double[::1] del_x_0, double[::1] q_N, double[::1] del_q_N):
    cdef Py_ssize_t NN = outpivots.shape[0] + 1
    cdef int n, vv, k, j, i, prev_in, next_in
    result = np.zeros((NN, NN), dtype=np.double, order='C')
    cdef double[:,::1] res_view = result
    nvar_nums = np.zeros(NN, dtype=np.int32, order='C')
    nvar_names = np.zeros(NN, dtype=np.int32, order='C')
    cdef int[::1] var_nums = nvar_nums
    cdef int[::1] var_names = nvar_names
    nrrhs = np.zeros((NN, 2), dtype=np.double, order='C')
    cdef double[:, ::1] rrhs = nrrhs
    for n in prange(NN - 1, nogil =True):
        vv = outpivots[n]
        var_names[n] = vv
        if vv > 0:
            k = find(vv, klist, 0, klist.shape[0])
            var_nums[n] = k
            prev_in = find_back(vv, inpivots, 0, n)
            for i in range(prev_in + 1, n + 1):
                res_view[n, i] = dx[k, i]
            if prev_in == -1:
                rrhs[n,0] = -x_0[k]
                if del_x_0 is not None:
                    rrhs[n,1] = -del_x_0[k]
        else:
            j = find(-vv, jlist, 0, jlist.shape[0])
            var_nums[n] = j
            next_in = find(vv, inpivots, n, NN - 1)
            if next_in > -1:
                for i in range(n + 1, next_in + 1):
                    res_view[n, i] = dq[j, i]
            else:
                for i in range(n + 1, NN):
                    res_view[n, i] = dq[j, i]
                rrhs[n,0] = -q_N[j]
                if del_q_N is not None:
                    rrhs[n,1] = -del_q_N[j]
    for i in range(NN):
        res_view[NN-1, i] = 1.
    return result, nvar_names, nvar_nums, nrrhs

@cython.boundscheck(False)
@cython.wraparound(False)
def get_left_stability_idx(int[::1] outpivots, int[::1] inpivots, int start_idx = 0):
    cdef int i, j
    cdef Py_ssize_t end_idx = outpivots.shape[0]
    for i in range(start_idx, end_idx):
        if outpivots[i] < 0:
            return i
    return i

@cython.boundscheck(False)
@cython.wraparound(False)
def get_new_col(double[:,::1] coeff, int[::1] var_nums, int[::1] var_names, int col_num, int row1, int row2, double[:, :] dx, double[:, :] dq):
    cdef Py_ssize_t NN = dx.shape[1]
    cdef int n, vv
    result = np.zeros(NN, dtype=np.double, order='C')
    cdef double[::1] res_view = result
    res_view[NN-1] = 1.
    for n in prange(NN - 1, nogil =True):
        vv = var_names[n]
        if coeff[n, col_num-1] != 0. or coeff[n, col_num+1] != 0. or coeff[n, col_num]:
            if vv > 0:
               res_view[n] = dx[var_nums[n], col_num]
            else:
               res_view[n] = dq[var_nums[n], col_num]
    if var_names[row1] > 0:
        res_view[row1] = dx[var_nums[row1], col_num]
    else:
        res_view[row1] = 0.
    if var_names[row2] > 0:
        res_view[row2] = 0.
    else:
        res_view[row2] = dq[var_nums[row2], col_num]
    return result

@cython.boundscheck(False)
@cython.wraparound(False)
def get_rows(int row1, int row2, int[:,::1] row_order, int iter):
    cdef int n
    for n in range(iter):
        if row_order[0,n] == row1:
            row1 = row_order[1,n]
        elif row_order[1,n] == row1:
            row1 = row_order[0,n]
        if row_order[0,n] == row2:
            row2 = row_order[1,n]
        elif row_order[1,n] == row2:
            row2 = row_order[0,n]
    row_order[0,iter] = row1
    row_order[1,iter] = row2
    return row1, row2

@cython.boundscheck(False)
@cython.wraparound(False)
def reorder_solution(double[::1,:] sol, int[:,::1] row_order, int iter):
    cdef double tmp
    cdef int i, n
    for i in range(2):
        for n in range(iter):
            tmp = sol[i,row_order[0,n]]
            sol[i,row_order[0,n]] = sol[i,row_order[1,n]]
            sol[i,row_order[1,n]] = tmp
    return sol

@cython.boundscheck(False)
@cython.wraparound(False)
def get_reordered_copy(double[::1,:] sol, int[:,::1] row_order, int iter):
    cdef double tmp
    cdef Py_ssize_t NN = sol.shape[0]
    res_sol = np.zeros(NN, dtype=np.double, order='C')
    cdef double[::1] sol_view = res_sol
    cdef int i
    for i in range(NN):
        sol_view[i] = sol[i,1]
    for i in range(iter+1):
        tmp = sol_view[row_order[0,i]]
        sol_view[row_order[0,i]] = sol_view[row_order[1,i]]
        sol_view[row_order[1,i]] = tmp
    return res_sol

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef cy_ftran(double[::1] vec, double[:, ::1] etas, int[::1] pivots, int last):
    cdef Py_ssize_t max_j = vec.shape[0]
    cdef int i, j, pivot_idx
    cdef double pivot_val, new_pivot_val
    for i in range(last):
        pivot_idx = pivots[i]
        pivot_val = vec[pivot_idx]
        if pivot_val != 0.:
            new_pivot_val = pivot_val * etas[i,pivot_idx]
            for j in range(max_j):
                vec[j] += pivot_val * etas[i,j]
            vec[pivot_idx] = new_pivot_val

@cython.boundscheck(False)
@cython.wraparound(False)
def ftran2eta(double[::1] vec, double[:, ::1] etas, int[::1] pivots, int last, int new_pivot):
    cdef Py_ssize_t max_j = vec.shape[0]
    cdef int j
    cdef double pivot_val, new_pivot_val
    cy_ftran(vec, etas, pivots, last)
    pivot_val = -vec[new_pivot]
    for j in range(max_j):
        etas[last,j] = vec[j]/pivot_val
    etas[last,new_pivot] = -1./pivot_val
    pivots[last] = new_pivot
