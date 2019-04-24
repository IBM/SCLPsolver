import numpy as np


class parametric_line():

    def __init__(self, x_0, q_N, klist, jlist, T=0, del_T =1, del_x_0=None, del_q_N=None):
        self._x_0 = x_0
        self._q_N = q_N
        self._klist = klist
        self._jlist = jlist
        self._T = T
        self._del_T = del_T
        self._del_x_0 = del_x_0
        self._del_q_N = del_q_N
        if self._del_x_0 is None:
            self._Kset_0 = self._klist[np.hstack(self._x_0 > 0)]
        else:
            self._Kset_0 = self._klist[np.hstack(np.logical_or(self._x_0 > 0, self._del_x_0 > 0))]
        if self._del_q_N is None:
            self._Jset_N = self._jlist[np.hstack(self._q_N > 0)]
        else:
            self._Jset_N = self._jlist[np.hstack(np.logical_or(self._q_N > 0, self._del_q_N > 0))]


    @property
    def x_0(self):
        return self._x_0

    @property
    def q_N(self):
        return self._q_N

    @property
    def del_x_0(self):
        return self._del_x_0

    @property
    def del_q_N(self):
        return self._del_q_N

    @property
    def T(self):
        return self._T

    @property
    def del_T(self):
        return self._del_T

    @property
    def klist(self):
        return self._klist

    @property
    def jlist(self):
        return self._jlist

    @property
    def Kset_0(self):
        return self._Kset_0

    @property
    def Jset_N(self):
        return self._Jset_N

    def forward_to(self, delta):
        if self._del_x_0 is not None:
            self._x_0 += self._del_x_0 * delta
        if self._del_q_N is not None:
            self._q_N += self._del_q_N * delta
        self._T += self._del_T * delta

    def backward_to(self, delta):
        if self._del_x_0 is not None:
            self._x_0 -= self._del_x_0 * delta
        if self._del_q_N is not None:
            self._q_N -= self._del_q_N * delta
        self._T -= self._del_T * delta

    @staticmethod
    def get_subproblem_parametric_line(DD, pbaseDD, dbaseDD, jlist, klist, lj, lk, v1, v2, AAN1, AAN2):
        x_0 = np.zeros((lk, 1))
        q_N = np.zeros((lj, 1))
        del_x_0 = np.zeros((lk, 1))
        del_q_N = np.zeros((lj, 1))
        # Boundary values for one sided subproblem, collision at t=0
        if AAN1 is None:
            # The case of v1 > 0, collision case iv_a
            if not isinstance(v1, list) and v1 > 0:
                dx_DD_v1 = DD[1:, 0][pbaseDD == v1][0]
                lk1 = klist == v1
                x_0[lk1] = -dx_DD_v1
                del_x_0[lk1] = dx_DD_v1
            # The case of v1 < 0, collision case iii_a
            if not isinstance(v1, list) and v1 < 0:
                dq_B2_v1 = AAN2['A'][0, 1:][AAN2['dual_name'] == v1][0]
                lj1 = jlist == -v1
                del_q_N[lj1] = -dq_B2_v1
        #
        #
        # Boundary values for one sided subproblem, collision at t=T
        elif AAN2 is None:
            # The case of v2 > 0, collision case iii_b
            if not isinstance(v2, list) and v2 > 0:
                dx_B1_v2 = AAN1['A'][1:, 0][AAN1['prim_name'] == v2][0]
                lk2 = klist == v2
                del_x_0[lk2] = -dx_B1_v2
            # The case of v2 < 0, collision case iv_b
            if not isinstance(v2, list) and v2 < 0:
                dq_DD_v2 = DD[0, 1:][dbaseDD == v2][0]
                lj2 = jlist == -v2
                q_N[lj2] = -dq_DD_v2
                del_q_N[lj2] = dq_DD_v2
        #
        #
        # Boundary values for two sided subproblem, collision at 0<t<T
        #  setting boundaries for the second exiting variable v1
        else:
            if not isinstance(v1, list) and v1 > 0:
                dx_DD_v1 = DD[1:, 0][pbaseDD == v1][0]
                lk1 = klist == v1
                x_0[lk1] = -dx_DD_v1
                dx_B1_v1 = AAN1['A'][1:, 0][AAN1['prim_name'] == v1][0]
                del_x_0[lk1] = -0.5 * dx_B1_v1 + dx_DD_v1
            if not isinstance(v1, list) and v1 < 0:
                dq_B2_v1 = AAN2['A'][0, 1:][AAN2['dual_name'] == v1][0]
                lj1 = jlist == -v1
                del_q_N[lj1] = -0.5 * dq_B2_v1
            #  setting boundaries for the first exiting variable v2
            if not isinstance(v2, list) and v2 > 0:
                dx_B1_v2 = AAN1['A'][1:, 0][AAN1['prim_name'] == v2][0]
                lk2 = klist == v2
                del_x_0[lk2] = -0.5 * dx_B1_v2
            if not isinstance(v2, list) and v2 < 0:
                dq_DD_v2 = DD[0, 1:][dbaseDD == v2][0]
                lj2 = jlist == -v2
                q_N[lj2] = -dq_DD_v2
                dq_B2_v2 = AAN2['A'][0, 1:][AAN2['dual_name'] == v2][0]
                del_q_N[lj2] = -0.5 * dq_B2_v2 + dq_DD_v2
        return parametric_line(x_0, q_N, klist, jlist, 1, 0, del_x_0, del_q_N)