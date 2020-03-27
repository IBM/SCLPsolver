import numpy as np
from subroutines.matlab_utils import find, ismember
from subroutines.lp_tools.simplex_procedures import simplex_procedures

#'#@profile
def calc_init_basis(formulation, x_0, q_N, tolerance = 0):

    K, J, L, I = formulation.K, formulation.J, formulation.L, formulation.I
    Kset = find(x_0)
    Jset = find(q_N)
    DD = formulation.get_ratesLP_basis()
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