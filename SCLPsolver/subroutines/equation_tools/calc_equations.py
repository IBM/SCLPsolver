import numpy as np
from subroutines.matlab_utils import find
from .eq_tools import build_equations


class time_equations():

    __slots__=['coeff','rrhs']

    def __init__(self, coeff, rrhs):
        self.coeff = coeff
        self.rrhs = rrhs

    #'#@profile
    def solve(self):
        #sol = np.linalg.solve(self.coeff, np.hstack((np.reshape(self.rhs, (-1, 1)), np.reshape(self.drhs, (-1, 1)))))
        sol = np.linalg.solve(self.coeff, self.rrhs)
        return sol[:, 0], sol[:, 1]

    @staticmethod
    #'#@profile
    def build_equations(param_line, klist, jlist, pivots, dx, dq):
        if len(pivots.outpivots) > 0:
            outp = np.asarray(pivots.outpivots, dtype = np.int32, order='C')
            inp =  np.asarray(pivots.inpivots, dtype = np.int32, order='C')
            coeff, bound_var_names, var_nums = build_equations(klist, jlist, outp, inp, dx, dq)
        else:
            coeff = np.eye(1)
        rrhs = np.zeros((coeff.shape[0], 2))
        if len(pivots.outpivots) > 0:
            lx = bound_var_names > 0
            xx = var_nums[lx]
            rrhs[np.where(lx), 0] = -param_line.x_0[xx]
            if param_line.del_x_0 is not None:
                rrhs[np.where(lx), 1] = -param_line.del_x_0[xx]
            lq = bound_var_names < 0
            qq = var_nums[lq]
            rrhs[np.where(lq), 0] = -param_line.q_N[qq]
            if param_line.del_q_N is not None:
                rrhs[np.where(lq), 1] = -param_line.del_q_N[qq]
        rrhs[-1, 0] = param_line.T
        rrhs[-1, 1] = param_line.del_T
        # old_coeff, rhs, drhs = time_equations.build_equations_old(param_line, klist, jlist, pivots, dx, dq)
        # if np.any(np.fabs(old_coeff - coeff) >= 10E-10):
        #      raise Exception('Coeff_problem')
        # if np.any(np.fabs(rrhs[:,0] - rhs) >= 10E-10):
        #     raise Exception('Rhs_problem')
        # if np.any(np.fabs(rrhs[:,1] - drhs) >= 10E-10):
        #     raise Exception('drhs_problem')
        return time_equations(coeff, rrhs)

    @staticmethod
    def build_equations_old(param_line, klist, jlist, pivots, dx, dq):
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
        return coeff, rhs, drhs
