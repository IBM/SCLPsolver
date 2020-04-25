

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