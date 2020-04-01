import numpy as np
from .matrix import matrix


class eq_solver(matrix):

    def __init__(self, rhs, drhs, size):
        super().__init__(1, size)
        self.rhs = rhs
        self.drhs = drhs

    # '#@profile
    def solve(self):
        sol = np.linalg.solve(self.get_matrix(), np.hstack((np.reshape(self.rhs, (-1, 1)), np.reshape(self.drhs, (-1, 1)))))
        return sol[:, 0], sol[:, 1]

    def update_caseI(self, N1, N2, num):
        if N1 == -1:
            self._top = N2
            self._left = N2
        elif N2 is None:
            self._right = self._left + N1
            self._bottom = self._top + N1
        else:
            Ndel = N2 - N1 - 1
            # move top right corner
            self._matrix[self._top + N1 + 1:self._top + N1 + 2, :] = self._matrix[self._top + num + 1:self._top + num + 2, :]
            self._matrix[self._top + N1 + 2:self._bottom-Ndel, :] = self._matrix[self._top + N2 + 1:self._bottom, :]
            # move bottom right corner
            self._matrix[self._top + index:self._bottom - 1, self._left + index:self._right - 1] = self._matrix[
                                                                                                   self._top + index + 1:self._bottom,
                                                                                                   self._left + index + 1:self._right]
            # move bottom left corner
            self._matrix[self._top + index:self._bottom - 1, self._left:self._left + index] = self._matrix[
                                                                                              self._top + index + 1:self._bottom,
                                                                                              self._left:self._left + index]

            self._bottom -= 1
            self._right -= 1

    # '#@profile
    @staticmethod
    def build_equations(param_line, klist, jlist, pivots, dx, dq):
        NN = len(pivots) + 1
        coeff = np.zeros((NN, NN))
        rhs = np.zeros(NN)
        drhs = np.zeros(NN)
        for n in range(NN - 1):
            vv = pivots[n][0]
            if vv > 0:
                k = find(klist == vv)[0]
                prev_in = pivots.get_previous_in(n)
                if prev_in is not None:
                    coeff[n, prev_in + 1:n + 1] = dx[k, prev_in + 1:n + 1]
                else:
                    coeff[n, 0:n + 1] = dx[k, 0:n + 1]
                    rhs[n] = -param_line.x_0[k]
                    if param_line.del_x_0 is not None:
                        drhs[n] = -param_line.del_x_0[k]
            else:
                j = find(jlist == -vv)[0]
                next_in = pivots.get_next_in(n)
                if next_in is not None:
                    coeff[n, n + 1:next_in + 1] = dq[j, n + 1:next_in + 1]
                else:
                    coeff[n, n + 1:] = dq[j, n + 1:]
                    rhs[n] = -param_line.q_N[j]
                    if param_line.del_q_N is not None:
                        drhs[n] = -param_line.del_q_N[j]
        coeff[NN - 1, :] = np.ones(NN)
        rhs[NN - 1] = param_line.T
        drhs[NN - 1] = param_line.del_T
        return time_equations(coeff, rhs, drhs)