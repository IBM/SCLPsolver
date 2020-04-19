import numpy as np

from subroutines.matlab_utils import find


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