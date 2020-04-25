import numpy as np
from subroutines.equation_tools.not_used.matrix import matrix
from .eq_tools import add_cols, add_cols2


class eq_solver(matrix):

    def __init__(self, size):
        super().__init__(1, size)
        self.bound_var_names = []
        self.var_nums = []

    # '#@profile
    def solve(self, param_line):
        rrhs = np.zeros((self.get_matrix().shape[0],2))
        var_nums = np.array(self.var_nums, dtype=np.int32)
        bound_var_names = np.array(self.bound_var_names, dtype=np.int32)
        lx = bound_var_names > 0
        xx = var_nums[lx]
        rrhs[np.where(lx), 0] = -param_line.x0[xx]
        if param_line.del_x_0 is not None:
            rrhs[np.where(lx), 1] = -param_line.del_q_N[xx]
        lq = bound_var_names < 0
        qq = var_nums[lq]
        rrhs[np.where(lq), 0] = -param_line.q_N[qq]
        if param_line.del_q_N is not None:
            rrhs[np.where(lq), 1] = -param_line.del_q_N[qq]
        rrhs[-1, 0] = param_line.T
        rrhs[-1, 1] = param_line.del_T
        sol = np.linalg.solve(self.get_matrix(), rrhs)
        return sol[:, 0], sol[:, 1]

    def update_caseI(self, N1, N2, pivots, rem_pivots):
        if N1 == -1:
            self._top = N2
            self._left = N2
            del self.bound_var_names[:N2]
            del self.var_nums[:N2]
        elif N2 is None:
            self._right = self._left + N1
            self._bottom = self._top + N1
            del self.bound_var_names[N1:]
            del self.var_nums[N1:]
        else:
            eq_num = rem_pivots.outpivots.index(pivots.outpivots[N1]) + N1
            Ndel = N2 - N1 - 1
            # move top right corner left
            self._matrix[self._top: self._top + N1, self._left + N1 + 1:self._right - Ndel] =\
                self._matrix[self._top: self._top + N1, self._left + N2:self._right]
            for i, qvar in enumerate(rem_pivots.inpivots):
                if qvar < 0:
                    if qvar in rem_pivots.outpivots[i:] and qvar in pivots.outpivots[:N1]:
                        qnum_out = rem_pivots.outpivots.index(qvar, i) + N1
                        # last index of qvar in out pivots
                        qnum_in = next(i for i in reversed(range(len(pivots.outpivots))) if pivots.outpivots[i] == qvar)
                        self.bound_var_names[qnum_in] = qvar
                        self._matrix[self._top + qnum_in: self._top + qnum_in + 1, self._left + N1 + 1:self._right - Ndel] = \
                            self._matrix[self._top + qnum_out: self._top + qnum_out + 1, self._left + N2:self._right]
                else:
                    if qvar in rem_pivots.outpivots[:i] and qvar in pivots.outpivots[N2:]:
                        qnum_out = rem_pivots.outpivots.index(qvar, i) + N1
                        qnum_in = pivots.outpivots.index(qvar, N2)
                        self.bound_var_names[qnum_in] = qvar
                        self._matrix[self._top + qnum_in: self._top + qnum_in + 1, self._left:self._left + N1 + 1] = \
                            self._matrix[self._top + qnum_out: self._top + qnum_out + 1, self._left:self._left + N1 + 1]
            # move left part of equation up
            if eq_num > N1:
                self._matrix[self._top + N1: self._top + N1 + 1, :self._left + N1 + 1] = \
                    self._matrix[self._top + eq_num: self._top + eq_num + 1, :self._left + N1 + 1]
                self.bound_var_names[N1] = self.bound_var_names[eq_num]
                self.var_nums[N1] = self.var_nums[eq_num]
            del self.bound_var_names[N1 + 1:N2]
            del self.var_nums[N1 + 1:N2]
            # move right part of equation left
            self._matrix[self._top + N1: self._top + N1 + 1, self._left + N1 + 1:self._right - Ndel] = \
                self._matrix[self._top + eq_num: self._top + eq_num + 1, self._left + N2:self._right]
            # move bottom left corner up
            self._matrix[self._top + N1 + 1: self._bottom - Ndel, :self._left + N1 + 1 ] = \
                self._matrix[self._top + N2: self._bottom, :self._left + N1 + 1]
            # move bottom right corner
            self._matrix[self._top + N1 + 1: self._bottom - Ndel, self._left + N1 + 1:self._right - Ndel] =\
                self._matrix[self._top + N2: self._bottom, self._left + N2:self._right]
            self._bottom -= Ndel
            self._right -= Ndel

    def update_caseII(self, klist, jlist, pivots, dx, dq, N1, N2, Nnew):
        if N1 == -1:
            # v = list(set(new_pivots.outpivots).intersection(self.var_names[:N2]))
            # eq_num = self.var_names.index(v[0], 0, N2)
            # new_num = new_pivots.outpivots.index(v[0]) + N1
            del self.bound_var_names[:N2]
            del self.var_nums[:N2]
            if self._top >= Nnew:
                self._top = self._top - Nnew
                self._left = self._left - Nnew
            else:
                self.enlarge(Nnew)
            self.add_rows(klist, jlist, pivots, dx, dq, 0, Nnew)
            var_nums = np.array(self.var_nums, dtype=np.int32)
            var_names = np.array(pivots.outpivots, dtype=np.int32)
            add_cols(self._matrix, dx, dq, var_nums, var_names, self._top + Nnew, self._bottom - 1, self._left,
                     self._left + Nnew, -self._top, -self._left)
            self._matrix[self._bottom-1,self._left:self._right] = np.ones(self._right-self._left)
        elif N2 is None:
            # v = list(set(new_pivots.outpivots).intersection(self.var_names[N1:]))
            # eq_num = self.var_names.index(v[0], N1)
            # new_num = new_pivots.outpivots.index(v[0]) + N1
            del self.bound_var_names[N1:]
            del self.var_nums[N1:]
            if self._bottom + Nnew <= self._matrix.shape[0]:
                # insert down
                self._bottom = self._bottom + Nnew
                self._right = self._right + Nnew
            else:
                self.enlarge(Nnew)
            self.add_rows(klist, jlist, pivots, dx, dq, N1, N1+Nnew)
            self._matrix[self._bottom-1,self._left:self._right] = np.ones(self._right-self._left)
            var_nums = np.array(self.var_nums, dtype=np.int32)
            var_names = np.array(pivots.outpivots, dtype=np.int32)
            add_cols(self._matrix, dx, dq, var_nums, var_names, self._top, self._bottom - Nnew-1, self._right - Nnew,
                     self._right, -self._top, -self._right+ Nnew + N1+1)
        else:
            if N2- N1 -1 >0:
                Nadd = N2- N1 -1 -Nnew
            else:
                Nadd = Nnew
            # vees = list(set(new_pivots.outpivots).intersection(self.var_names[N1:N2]))
            # eq_num1 = self.var_names.index(vees[0], N1, N2)
            # new_num1 = new_pivots.outpivots.index(vees[0], N1, N2)
            # eq_num2 = self.var_names.index(vees[1], N1, N2)
            # new_num2 = new_pivots.outpivots.index(vees[1], N1, N2)
            del self.bound_var_names[N1:N2]
            del self.var_nums[N1:N2]
            if self._bottom + Nadd <= self._matrix.shape[0]:
                # insert down
                self._bottom = self._bottom + Nadd
                self._right = self._right + Nadd
            else:
                self.enlarge(Nadd)
            # move top right corner left
            if Nadd != 0:
                self._matrix[self._top: self._top + N1, self._left + N2: self._right] =\
                    self._matrix[self._top: self._top + N1, self._left + N2 + Nadd:self._right + Nadd]
                # move bottom left corner up
                self._matrix[self._top + N2: self._bottom, :self._left + N1 + 1] = \
                    self._matrix[self._top + N2 + Nadd: self._bottom + Nadd, :self._left + N1 + 1]
                # move bottom right corner
                self._matrix[self._top + N2: self._bottom, self._left + N2: self._right] =\
                    self._matrix[self._top + N2 + Nadd: self._bottom + Nadd, self._left + N2 + Nadd:self._right + Nadd]
            self.add_rows(klist, jlist, pivots, dx, dq, N1, N2 + Nadd)
            var_nums = np.array(self.var_nums, dtype=np.int32)
            var_names = np.array(pivots.outpivots, dtype=np.int32)
            add_cols2(self._matrix, dx, dq, var_nums, var_names, self._top, self._top + N1, self._left + N1 + 1,
                     self._left + N2 + Nadd, -self._top, -self._left)
            add_cols2(self._matrix, dx, dq, var_nums[N2 + Nadd:], var_names[N2 + Nadd:], self._top + N2 + Nadd, self._bottom-1,
                     self._left + N1 + 1, self._left + N2 + Nadd, -(self._top + N2 + Nadd), -self._left)
            self._matrix[self._bottom-1,self._left:self._right] = np.ones(self._right-self._left)

    def enlarge(self, size = 1):
        self._allocation_size = 2 * (self._allocation_size + 2 * size)
        mat = np.zeros((self._allocation_size, self._allocation_size), order='C')
        pad = round(self._allocation_size / 4)
        mat[pad:pad + self._bottom - self._top,
        pad:pad + self._right - self._left] = \
            self._matrix[self._top:self._bottom, self._left:self._right]
        self._matrix = mat
        self._top = pad
        self._left = pad
        self._bottom = pad + self._bottom - self._top + size
        self._right = pad + self._right - self._left + size

    def add_rows(self, klist, jlist, pivots, dx, dq, from_, to_):
        for n in range(from_, to_):
            vv = pivots.outpivots[n]
            if vv > 0:
                k = np.where(klist == vv)[0][0]
                self.var_nums.insert(n, k)
                prev_in = pivots.get_previous_in(n)
                if prev_in is not None:
                    self._matrix[self._top + n, self._left:self._left + prev_in + 1] = np.zeros(prev_in + 1)
                    self._matrix[self._top + n, self._left + prev_in + 1:self._left + n + 1] = dx[k, prev_in + 1:n + 1]
                    self.bound_var_names.insert(n, 0)
                else:
                    self._matrix[self._top + n, self._left:self._left+n+1] = dx[k, 0:n + 1]
                    self.bound_var_names.insert(n, vv)
                self._matrix[self._top + n, self._left + n + 1:self._right] = np.zeros(self._right-(self._left + n + 1))
            else:
                j = np.where(jlist == -vv)[0][0]
                next_in = pivots.get_next_in(n)
                self.var_nums.insert(n, j)
                if next_in is not None:
                    self._matrix[self._top + n, self._left + n + 1:self._left + next_in + 1] = dq[j, n + 1:next_in + 1]
                    self._matrix[self._top + n, self._left + next_in + 1:self._right] = np.zeros(self._right - self._left - next_in - 1)
                    self.bound_var_names.insert(n, 0)
                else:
                    self._matrix[self._top + n, self._left + n + 1:self._right] = dq[j, n + 1:]
                    self.bound_var_names.insert(n, vv)
                self._matrix[self._top + n, 0:self._left + n + 1] = np.zeros(self._left + n + 1)