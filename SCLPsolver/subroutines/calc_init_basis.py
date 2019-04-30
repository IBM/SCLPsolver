import numpy as np
from .matlab_utils import find, ismember
from .simplex_procedures import simplex_procedures

#'#@profile
def calc_init_basis(G,F,H,a,b,c,d,x_0,q_N, tolerance = 0):
    K, J = np.shape(G)
    L = np.shape(F)[1]
    I = np.shape(H)[0]

    Kset = find(x_0)
    Jset = find(q_N)
    DD = np.vstack((-np.hstack((0,c,d)), np.hstack((np.vstack(a),G,F)),np.hstack((np.vstack(b),H, np.zeros((I, L))))))
    DD = np.ascontiguousarray(DD)
    tmp_matrix = np.zeros_like(DD)
    pn = np.hstack((np.arange(1,K+1), -np.arange(J + 1, J + I + 1)))
    psx = ismember(np.arange(0,K), Kset).astype(int)
    psu = -ismember(np.arange(J, J + I), Jset).astype(int)
    ps = np.hstack((psx, psu))

    dn = np.hstack((-np.arange(1,J+1), np.arange(K + 1, K + L + 1)))
    dsq = ismember(np.arange(0,J), Jset).astype(int)
    dsp = -ismember(np.arange(K, K + L), Kset).astype(int)
    ds = np.hstack((dsq, dsp))
    return simplex_procedures(DD, pn, dn, ps, ds, tmp_matrix, tolerance)