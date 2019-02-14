import numpy as np
from .simplex_procedures import *


def calc_boundaries(G,F,H,b,d,alpha,gamma, tolerance = 0, solve_gen_LP = False):
    K, J = np.shape(G)
    L = np.shape(F)[1]
    I = np.shape(H)[0]
    if I == 0 & L == 0:
        x_0 = alpha
        q_N = np.vstack(-gamma)
        if np.any(x_0 < 0):
            raise Exception('***  Problem not primal feasible')
        if np.any(q_N < 0):
            raise Exception('***  Problem not dual feasible')
        return x_0, q_N
    if solve_gen_LP:
        DD0 = np.vstack((-np.hstack((0, gamma, np.zeros((1,L)))), np.hstack((alpha, G, F)), np.hstack((np.zeros((I,1)), H, np.zeros((I, L))))))
        pn = np.vstack(np.hstack((np.arange(1,K+1), -np.arange(J + 1, J + I + 1))))
        ps = np.zeros((K + I, 1), dtype = int)
        dn = np.hstack((-np.arange(1,J+1), np.arange(K + 1, K + L + 1)))
        ds = np.zeros((1, J + L), dtype = int)
        DD0, pn, dn, ps, ds, err = simplex_procedures(DD0, pn, dn, ps, ds, tolerance)
        if DD0[0, 0] != 0:
            raise Exception('*** Problem requires impulse controls')
    if np.size(F) > 0:
        DD1 = np.vstack((-np.hstack((0, d)), np.hstack((np.vstack(alpha), F))))
        pn1 = np.vstack(np.arange(1,K+1))
        ps1 = np.zeros((K, 1), dtype = int)
        dn1 = np.arange(K + 1, K + L + 1)
        ds1 = np.zeros((1, L), dtype = int)
        DD1, pn1, dn1, ps1, ds1, err = simplex_procedures(DD1, pn1, dn1, ps1, ds1, tolerance)
        x_0 = np.zeros((K + L, 1))
        x_0[pn1] = DD1[-1, 0]
    else:
        x_0 = alpha

    if np.size(H) > 0:
        DD2 = np.vstack((np.hstack((0, np.hstack(b))), np.hstack((np.vstack(-gamma), -H.transpose()))))
        pn2 = np.vstack(np.arange(1,J+1))
        ps2 = np.zeros((J, 1), dtype = int)
        dn2 = np.arange(J + 1,J + I+1)
        ds2 = np.zeros((1, I), dtype = int)
        DD2, pn2, dn2, ps2, ds2, err = simplex_procedures(DD2, pn2, dn2, ps2, ds2, tolerance)
        q_N = np.zeros((J + I, 1))
        q_N[pn2] = DD2[-1, 0]
    else:
        q_N = -gamma

    return x_0, q_N