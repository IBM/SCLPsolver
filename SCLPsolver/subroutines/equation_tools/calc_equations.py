import numpy as np
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

#'#@profile
def get_equations(param_line, klist, jlist, pivots, dx, dq):
    if len(pivots.outpivots) > 0:
        outp = np.asarray(pivots.outpivots, dtype = np.int32, order='C')
        inp =  np.asarray(pivots.inpivots, dtype = np.int32, order='C')
        coeff, bound_var_names, var_nums = build_equations(klist, jlist, outp, inp, dx, dq)
    else:
        coeff = np.eye(1)
    rrhs = np.zeros((coeff.shape[0], 2))
    #TODO: this should be reviewed and restructured
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
