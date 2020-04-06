# cython: infer_types=True
#cython: language_level=3


from cython.parallel import prange
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
def cy_pivot(double[:, ::1] dct, int[::1] pn, int[::1] dn, int i, int j):
    cdef int nam
    nam = pn[i]
    pn[i] = dn[j]
    dn[j] = nam
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
    return