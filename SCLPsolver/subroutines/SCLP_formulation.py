import numpy as np
from enum import Enum
from .matlab_utils import find, ismember
from .LP_formulation import LP_formulation
from .simplex_procedures import unsigned_simplex
from .piecewise_data import piecewise_data


class SCLP_formulation_type(Enum):
    primal_classic = 0
    dual_classic = 1
    weiss = 2
    not_bounded = 3
    primal_MCLP = 4
    dual_MCLP = 5
    both_MCLP = 6
    primal_infeasible = 7
    dual_infeasible = 8
    both_infeasible = 9

class SCLP_data_type(Enum):
    linear = 0
    primal_piecewise_linear = 1
    dual_piecewise_linear = 2
    piecewise_linear = 3


# We are going to extend this class
# Assume that a,b,c,d are matrix
class SCLP_formulation():

    __slots__ = ["G", "F", "H", "a", "b", "c", "d", "alpha", "gamma", "T", "I", "J", "K", "L", "_formulation_type", "_data_type"]

    def __init__(self, G, F, H, a, b, c, d, alpha, gamma, T):
        self.G, self.F, self.H, self.a, self.b, self.c, self.d, self.alpha, self.gamma, self.T = G, F, H, a, b, c, d, alpha, gamma, T
        self.K = G.shape[0]
        self.J = G.shape[1]
        self.I = H.shape[0]
        self.L = F.shape[1]
        if self.L == 0:
            if self.I == 0:
                if np.any(self.alpha < 0):
                    if np.any(self.gamma > 0):
                        self._formulation_type = SCLP_formulation_type.both_MCLP
                    else:
                        self._formulation_type = SCLP_formulation_type.primal_MCLP
                else:
                    if np.any(self.gamma > 0):
                        self._formulation_type = SCLP_formulation_type.dual_MCLP
                    else:
                        self._formulation_type = SCLP_formulation_type.not_bounded
            else:
                self._formulation_type = SCLP_formulation_type.primal_classic
                if np.any(self.alpha < 0):
                    self._formulation_type = SCLP_formulation_type.primal_MCLP
        else:
            if self.I == 0:
                self._formulation_type = SCLP_formulation_type.dual_classic
                if np.any(self.gamma > 0):
                    self._formulation_type = SCLP_formulation_type.dual_MCLP
            else:
                self._formulation_type = SCLP_formulation_type.weiss
        if isinstance(a, piecewise_data):
            if isinstance(c, piecewise_data):
                self._data_type = SCLP_data_type.piecewise_linear
            else:
                self._data_type = SCLP_data_type.primal_piecewise_linear
        else:
            if isinstance(c, piecewise_data):
                self._data_type = SCLP_data_type.dual_piecewise_linear
            else:
                self._data_type = SCLP_data_type.linear

    @property
    def data_type(self):
        return self._data_type

    @property
    def formulation_type(self):
        return self._formulation_type

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

    def get_generalBoundaryLP(self):
        DD0 = np.vstack((np.hstack((0, -self.gamma, np.zeros((1, self.L)), self.d)), np.hstack((self.alpha, self.G, self.F)),
                         np.hstack((np.zeros((self.I, 1)), self.H, np.zeros((self.I, self.L))))))
        pn = np.concatenate((np.arange(1, self.K + 1), -np.arange(self.J + 1, self.J + self.I + 1)))
        dn = np.concatenate((-np.arange(1, self.J + 1), np.arange(self.K + 1, self.K + self.L + 1)))
        return LP_formulation(DD0, pn, dn)

    def get_dualBoundaryLP_solution(self, tolerance = 0):
        if self._formulation_type == SCLP_formulation_type.not_bounded or self._formulation_type == SCLP_formulation_type.dual_classic:
            return -self.gamma
        elif self._formulation_type == SCLP_formulation_type.primal_classic or self._formulation_type == SCLP_formulation_type.weiss:
            LP_form = self.get_dualBoundaryLP()
            LP_form, err = unsigned_simplex(LP_form, None, tolerance)
            if err['result'] == 0:
                q_N = np.zeros(self.J + self.I)
                q_N[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
                return q_N
        # MCLP not supported yet
        return None

    def get_primalBoundaryLP_solution(self, tolerance = 0):
        if self._formulation_type == SCLP_formulation_type.not_bounded or self._formulation_type == SCLP_formulation_type.primal_classic:
            return self.alpha
        elif self._formulation_type == SCLP_formulation_type.dual_classic or self._formulation_type == SCLP_formulation_type.weiss:
            LP_form = self.get_primalBoundaryLP()
            LP_form, err = unsigned_simplex(LP_form, None, tolerance)
            if err['result'] == 0:
                x_0 = np.zeros(self.K + self.L)
                x_0[LP_form.prim_name - 1] = LP_form.simplex_dict[1:, 0]
                return x_0
        # MCLP not supported yet
        return None
