import numpy as np
from .matlab_utils import *


#'#@profile
def calc_equations(klist,jlist,pivots,x_0,del_x_0,q_N,del_q_N,T,del_T,dx,dq):
    NN = len(pivots)+1
    coeff = np.zeros((NN,NN))
    rhs = np.zeros(NN)
    drhs = np.zeros(NN)
    for n in range(NN-1):
        vv = pivots[n][0]
        if vv > 0:
            try:
                k = find(klist == vv)[0]
            except:
                print(vv)
            coeff[n,0:n+1] = dx[k, 0:n+1]
            rhs[n] = -x_0[k]
            drhs[n] = -del_x_0[k]
        else:
            j = find(jlist == -vv)[0]
            coeff[n,n+1:] = dq[j, n+1:]
            rhs[n] = -q_N[j]
            drhs[n] = -del_q_N[j]
    coeff[NN-1,:] = np.ones(NN)
    rhs[NN-1] = T
    drhs[NN-1] = del_T
    sol = np.linalg.solve(coeff, np.hstack((np.reshape(rhs,(-1,1)),np.reshape(drhs,(-1,1)))))
    # tau =clean(sol(:,1));%
    # dtau=clean(sol(:,2));%
    return sol[:,0], sol[:,1]