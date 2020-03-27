import numpy as np
from subroutines.lp_tools.LP_formulation import LP_formulation
from subroutines.lp_tools.simplex_procedures import unsigned_simplex


#'#@profile
def calc_boundaries(formulation, tolerance = 0, solve_gen_LP = False):
    G, F, H, b, d, alpha, gamma = formulation.G, formulation.F, formulation.H, formulation.b, formulation.d, formulation.alpha, formulation.gamma
    K, J, L, I = formulation.K, formulation.J, formulation.L, formulation.I
    if I == 0 & L == 0:
        x_0 = alpha
        q_N = -gamma
        if np.any(x_0 < 0):
            raise Exception('***  Problem not primal feasible')
        if np.any(q_N < 0):
            raise Exception('***  Problem not dual feasible')
        return x_0, q_N
    if solve_gen_LP:
        DD0 = np.vstack((-np.hstack((0, gamma, np.zeros((1,L)))), np.hstack((alpha, G, F)), np.hstack((np.zeros((I,1)), H, np.zeros((I, L))))))
        pn = np.concatenate((np.arange(1,K+1), -np.arange(J + 1, J + I + 1)))
        dn = np.concatenate((-np.arange(1,J+1), np.arange(K + 1, K + L + 1)))
        lp_form = LP_formulation(DD0, pn, dn)
        lp_form, err = unsigned_simplex(lp_form, np.zeros_like(DD0), tolerance)
        if lp_form.simplex_dict[0, 0] != 0:
            raise Exception('*** Problem requires impulse controls')
    if np.size(F) > 0:
        DD1 = np.vstack((-np.hstack((0, d)), np.hstack((np.vstack(alpha), F))))
        pn1 = np.arange(1,K+1)
        dn1 = np.arange(K + 1, K + L + 1)
        lp_form = LP_formulation(DD1, pn1, dn1)
        lp_form, err = unsigned_simplex(lp_form, np.zeros_like(DD1), tolerance)
        x_0 = np.zeros(K + L, 1)
        x_0[lp_form.prim_name-1] = lp_form.simplex_dict[1:, 0]
    else:
        x_0 = alpha

    if np.size(H) > 0:
        DD2 = np.vstack((np.hstack((0, np.hstack(b))), np.hstack((np.vstack(-gamma), -H.transpose()))))
        pn2 = np.arange(1,J+1)
        dn2 = np.arange(J + 1,J + I+1)
        lp_form = LP_formulation(DD2, pn2, dn2)
        lp_form, err = unsigned_simplex(lp_form, np.zeros_like(DD2), tolerance)
        q_N = np.zeros(J + I)
        q_N[lp_form.prim_name-1] = lp_form.simplex_dict[1:, 0]
    else:
        q_N = -gamma

    return x_0, q_N