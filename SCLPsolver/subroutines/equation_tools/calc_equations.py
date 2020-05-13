import numpy as np
from scipy.linalg import lu_factor, lu_solve
from .eq_tools import build_equations, get_rows, get_new_col, get_left_stability_idx, ftran2eta

#TODO: build method can further improved if we reuse all matricies - note LU factorization is slower if matrix is not contnignous
class time_equations():

    def __init__(self):
        self.coeff = None
        self.lu = None
        self.rrhs = None
        self.var_names = None
        self.var_nums = None
        self.iteration = 0
        self._max_iterations = 30
        self.row_order = np.zeros((2,self._max_iterations), dtype=np.int32, order='C')
        self.pivot_idxs = np.zeros(self._max_iterations, dtype=np.int32, order='C')
        self.solution = None
        self.etas = None

    def build(self, param_line, klist, jlist, pivots, dx, dq, test=False):
        if not test:
            self.iteration = 0
        if len(pivots.outpivots) > 0:
            outp = np.asarray(pivots.outpivots, dtype=np.int32, order='C')
            inp = np.asarray(pivots.inpivots, dtype=np.int32, order='C')
            left_idx = None #get_left_stability_idx(outp, inp)
            self.coeff, self.var_names, self.var_nums, self.rrhs=\
                build_equations(klist, jlist, outp, inp, dx, dq, param_line.x_0, param_line.del_x_0, param_line.q_N, param_line.del_q_N)
        else:
            self.coeff = np.eye(1)
            self.rrhs = np.zeros((1, 2))
            left_idx = 0
        self.rrhs[-1, 0] = param_line.T
        self.rrhs[-1, 1] = param_line.del_T
        return left_idx

    def can_update(self, col_info):
        if col_info.case == 'Case ii_' and col_info.N2 - col_info.N1 == 2 and col_info.Nnew == 0:
            return self.iteration < self._max_iterations and col_info.delta > 1E-5
        else:
            return False

    #TODO: this function does not always correct - however it is not used
    def get_reordered_coeff(self):
        cf = self.coeff.copy()
        for n in range(self.iteration):
            tmp = cf[self.row_order[0,n],:].copy()
            cf[self.row_order[0,n],:] = cf[self.row_order[1,n],:]
            cf[self.row_order[1,n], :] = tmp
        return cf

    def update(self, n, dx, dq):
        if self.iteration == 0:
            self.etas = np.zeros((self._max_iterations, self.coeff.shape[0]), dtype=np.double, order='C')
        row1, row2 = get_rows(n-1, n, self.row_order, self.iteration)
        vec = get_new_col(self.coeff,  self.var_nums,  self.var_names, n, row1, row2, dx, dq)
        self.coeff[:, n] = vec
        vec1 = lu_solve(self.lu, vec, check_finite=False)
        ftran2eta(vec1, self.etas, self.pivot_idxs, self.iteration, n)
        ftran(self.solution[:, 1], self.etas[self.iteration, :], n)
        self.iteration += 1
        return self.solution[:, 1].copy()

    def solve(self):
        self.lu = lu_factor(self.coeff, check_finite=False)
        self.solution = lu_solve(self.lu, self.rrhs, check_finite=False)
        return self.solution[:, 0], self.solution[:, 1].copy()

def to_eta(values, index_to_pivot):
    pivot_val = values[index_to_pivot]
    values /= -values[index_to_pivot]
    values[index_to_pivot] = 1./pivot_val
    return values

def ftran(values, eta, index_to_pivot):
    if values[index_to_pivot] != 0:
        pivot_val = values[index_to_pivot] * eta[index_to_pivot]
        values[:len(eta)] += values[index_to_pivot] * eta
        values[index_to_pivot] = pivot_val
    return values

