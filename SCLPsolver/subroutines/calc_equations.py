import numpy as np
from .matlab_utils import find


#'#@profile
def calc_equations(param_line, pivots, dx, dq):
    NN = len(pivots)+1
    coeff = np.zeros((NN,NN))
    rhs = np.zeros(NN)
    drhs = np.zeros(NN)
    for n in range(NN-1):
        vv = pivots[n][0]
        if vv > 0:
            k = find(param_line.klist == vv)[0]
            coeff[n,0:n+1] = dx[k, 0:n+1]
            rhs[n] = -param_line.x_0[k]
            if param_line.del_x_0 is not None:
                drhs[n] = -param_line.del_x_0[k]
        else:
            j = find(param_line.jlist == -vv)[0]
            coeff[n,n+1:] = dq[j, n+1:]
            rhs[n] = -param_line.q_N[j]
            if param_line.del_q_N is not None:
                drhs[n] = -param_line.del_q_N[j]
    coeff[NN-1,:] = np.ones(NN)
    rhs[NN-1] = param_line.T
    drhs[NN-1] = param_line.del_T
    sol = np.linalg.solve(coeff, np.hstack((np.reshape(rhs,(-1,1)),np.reshape(drhs,(-1,1)))))
    return sol[:,0], sol[:,1]