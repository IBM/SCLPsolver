import numpy as np
from .matlab_utils import find, ismember
from .LP_formulation import LP_formulation
from .simplex_procedures import unsigned_simplex


# We are going to extend this class
# Assume that a,b,c,d are matrix
class SCLP_formulation():

    __slots__ = ["G", "F", "H", "a", "b", "c", "d", "alpha", "gamma", "T", "I", "J", "K", "L"]

    def __init__(self, G, F, H, a, b, c, d, alpha, gamma, T):
        self.G, self.F, self.H, self.a, self.b, self.c, self.d, self.alpha, self.gamma, self.T = G, F, H, a, b, c, d, alpha, gamma, T
        self.K = G.shape[0]
        self.J = G.shape[1]
        self.I = H.shape[0]
        self.L = F.shape[1]

    def formulate_ratesLP(self, x_0, q_N):
        Kset = find(x_0)
        Jset = find(q_N)
        DD = np.vstack((-np.hstack((0, self.c, self.d)), np.hstack((np.vstack(self.a), self.G, self.F)),
                          np.hstack((np.vstack(self.b), self.H, np.zeros((self.I, self.L))))))
        DD = np.ascontiguousarray(DD)
        pn = np.hstack((np.arange(1, self.K + 1), -np.arange(self.J + 1, self.J + self.I + 1)))
        psx = ismember(np.arange(0, self.K), Kset).astype(int)
        psu = -ismember(np.arange(self.J, self.J + self.I), Jset).astype(int)
        ps = np.hstack((psx, psu))

        dn = np.hstack((-np.arange(1, self.J + 1), np.arange(self.K + 1, self.K + self.L + 1)))
        dsq = ismember(np.arange(0, self.J), Jset).astype(int)
        dsp = -ismember(np.arange(self.K, self.K + self.L), Kset).astype(int)
        ds = np.hstack((dsq, dsp))
        return LP_formulation(DD, pn, dn, ps, ds)

    def get_primalBoundaryLP(self):
        DD1 = np.vstack((-np.hstack((0, self.d)), np.hstack((np.vstack(self.alpha), self.F))))
        pn1 = np.arange(1, self.K + 1)
        dn1 = np.arange(self.K + 1, self.K + self.L + 1)
        return LP_formulation(DD1, pn1, dn1)

    def get_dualBoundaryLP(self):
        DD1 = np.vstack((np.hstack((0, np.hstack(self.b))), np.hstack((np.vstack(-self.gamma), -self.H.transpose()))))
        pn1 = np.arange(1, self.J + 1)
        dn1 = np.arange(self.J + 1, self.J + self.I + 1)
        return LP_formulation(DD1, pn1, dn1)

    def get_dualBoundaryLP_solution(self, tolerance = 0):
        if self.I > 0:
            LP_form = self.get_dualBoundaryLP()
            LP_form, err = unsigned_simplex(LP_form, None, tolerance)
            q_N = np.zeros(self.J + self.I)
            q_N[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
        else:
            q_N = -self.gamma
        return q_N

    def get_primalBoundaryLP_solution(self, tolerance = 0):
        if self.L > 0:
            LP_form = self.get_primalBoundaryLP()
            LP_form, err = unsigned_simplex(LP_form, None, tolerance)
            x_0 = np.zeros(self.K + self.L)
            x_0[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
        else:
            x_0 = self.alpha
        return x_0
