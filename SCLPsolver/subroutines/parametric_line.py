import numpy as np
from enum import Enum
from .calc_boundaries import calc_boundaries
from .LP_formulation import get_value_by_name


class line_type(Enum):
    SCLP_x0 = -1
    SCLP_main = 0
    SCLP_sub = 1
    SCLP_orthogonal = 2


class parametric_line():

    def __init__(self, x_0, q_N, theta_bar, T=0, del_T =1, del_x_0=None, del_q_N=None, Kset_0=None, Jset_N=None, B1=None, B2=None, ltype = line_type.SCLP_main):
        self._x_0 = x_0
        self._q_N = q_N
        self._theta_bar = theta_bar
        self._T = T
        self._del_T = del_T
        self._del_x_0 = del_x_0
        self._del_q_N = del_q_N
        self._Kset_0 = Kset_0
        self._Jset_N = Jset_N
        self._B1 = B1
        self._B2 = B2
        self._ltype = ltype
        self._theta = 0
        self._back_direction = False

    def build_boundary_sets(self, klist, jlist):
        if self._del_x_0 is None:
            self._Kset_0 = klist[self._x_0 > 0]
        else:
            self._Kset_0 = klist[np.logical_or(self._x_0 > 0, self._del_x_0 > 0)]
        if self._del_q_N is None:
            self._Jset_N = jlist[self._q_N > 0]
        else:
            self._Jset_N = jlist[np.logical_or(self._q_N > 0, self._del_q_N > 0)]

    def scale(self, factor):
        self._theta_bar *= factor
        self._theta *= factor
        self._del_T /= factor
        if self._del_x_0 is not None:
            self._del_x_0 /= factor
        if self._del_q_N is not None:
            self._del_q_N /= factor

    @property
    def x_0(self):
        return self._x_0

    @property
    def q_N(self):
        return self._q_N

    @property
    def del_x_0(self):
        if self._back_direction and self._del_x_0 is not None:
            return -self._del_x_0
        else:
            return self._del_x_0

    @property
    def del_q_N(self):
        if self._back_direction and self._del_q_N is not None:
            return -self._del_q_N
        else:
            return self._del_q_N

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value):
        self._T = value

    @property
    def del_T(self):
        if self._back_direction:
            return -self._del_T
        else:
            return self._del_T

    @property
    def Kset_0(self):
        return self._Kset_0

    @property
    def Jset_N(self):
        return self._Jset_N

    @property
    def theta_bar(self):
        return self._theta_bar

    @theta_bar.setter
    def theta_bar(self, value):
        if value < self._theta:
            self._back_direction = True
        else:
            self._back_direction = False
        self._theta_bar = value

    @property
    def B1(self):
        return self._B1

    @property
    def B2(self):
        return self._B2

    @property
    def theta(self):
        return self._theta

    def is_main(self):
        return self._ltype == line_type.SCLP_main

    def is_sub(self):
        return self._ltype == line_type.SCLP_sub

    def is_orthogonal(self):
        return self._ltype == line_type.SCLP_orthogonal

    def is_end(self, delta):
        if self._back_direction:
            return self._theta - delta <= self._theta_bar
        else:
            return self._theta + delta >= self._theta_bar

    def forward_to_end(self):
        self._forward_to(self._theta_bar - self._theta)

    def _forward_to(self, delta):
        if self._del_x_0 is not None:
            self._x_0 += self._del_x_0 * delta
        if self._del_q_N is not None:
            self._q_N += self._del_q_N * delta
        self._T += self._del_T * delta
        self._theta += delta

    def forward_to(self, delta):
        if self._back_direction:
            self._backward_to(delta)
        else:
            self._forward_to(delta)

    def backward_to(self, delta):
        if self._back_direction:
            self._forward_to(delta)
        else:
            self._backward_to(delta)

    def _backward_to(self, delta):
        if self._del_x_0 is not None:
            self._x_0 -= self._del_x_0 * delta
        if self._del_q_N is not None:
            self._q_N -= self._del_q_N * delta
        self._T -= self._del_T * delta
        self._theta -= delta

    def get_orthogonal_line(self, theta_bar= 1, type=1):
        del_x = None
        del_q = None
        if type == 1 or type == 3:
            del_x = np.zeros_like(self._x_0)
            del_x[self._Kset_0-1] = np.random.rand(len(self._Kset_0)) - 0.5
            theta_bar =min(theta_bar, 1/np.max(np.divide(-del_x, self._x_0, where = np.logical_and(del_x < 0, self._Kset_0))))
        if type == 2 or type == 3:
            del_q = np.zeros_like(self._q_N)
            del_q[self._Jset_N-1] = np.random.rand(len(self._Jset_N)) - 0.5
            theta_bar = min(theta_bar, 1/np.max(np.divide(-del_q, self._q_N, where=np.logical_and(del_q < 0, self._Jset_N))))
        return parametric_line(self._x_0, self._q_N, theta_bar, self._theta, 0, del_x, del_q,
                               self._Kset_0, self._Jset_N, None, None, line_type.SCLP_orthogonal)

    def get_x0_parline(self, solution, v1, v_x0):
        lk1 = solution.klist == v1
        del_x_0 = np.zeros_like(self._x_0)
        del_x_0[lk1] = v_x0
        return parametric_line(self._x_0, self._q_N, self._T, self._T, 0, del_x_0, np.zeros_like(self._q_N),
                               self._Kset_0, self._Jset_N, None, None, line_type.SCLP_x0)

    @staticmethod
    def get_subproblem_parametric_line(basis, solution, v1, v2, AAN1, AAN2, pbaseB1red, pbaseB2red):
        x_0 = np.zeros(solution.KK)
        q_N = np.zeros(solution.JJ)
        del_x_0 = np.zeros(solution.KK)
        del_q_N = np.zeros(solution.JJ)
        # Boundary values for one sided subproblem, collision at t=0
        if AAN1 is None:
            if not isinstance(v1, list):
                # The case of v1 > 0, collision case iv_a
                if v1 > 0:
                    dx_DD_v1 = get_value_by_name(basis, v1, True)
                    lk1 = solution.klist == v1
                    x_0[lk1] = -dx_DD_v1
                    del_x_0[lk1] = dx_DD_v1
                # The case of v1 < 0, collision case iii_a
                elif v1 < 0:
                    dq_B2_v1 = get_value_by_name(AAN2, v1, False)
                    lj1 = solution.jlist == -v1
                    del_q_N[lj1] = -dq_B2_v1
        #
        # Boundary values for one sided subproblem, collision at t=T
        elif AAN2 is None:
            if not isinstance(v2, list):
                # The case of v2 > 0, collision case iii_b
                if v2 > 0:
                    dx_B1_v2 = get_value_by_name(AAN1, v2, True)
                    lk2 = solution.klist == v2
                    del_x_0[lk2] = -dx_B1_v2
                # The case of v2 < 0, collision case iv_b
                elif v2 < 0:
                    dq_DD_v2 = get_value_by_name(basis, v2, False)
                    lj2 = solution.jlist == -v2
                    q_N[lj2] = -dq_DD_v2
                    del_q_N[lj2] = dq_DD_v2
        #
        # Boundary values for two sided subproblem, collision at 0<t<T
        #  setting boundaries for the second exiting variable v1
        else:
            if not isinstance(v1, list):
                if v1 > 0:
                    dx_DD_v1 = get_value_by_name(basis, v1, True)
                    lk1 = solution.klist == v1
                    x_0[lk1] = -dx_DD_v1
                    dx_B1_v1 = get_value_by_name(AAN1, v1, True)
                    del_x_0[lk1] = -0.5 * dx_B1_v1 + dx_DD_v1
                elif v1 < 0:
                    dq_B2_v1 = get_value_by_name(AAN2, v1, False)
                    lj1 = solution.jlist == -v1
                    del_q_N[lj1] = -0.5 * dq_B2_v1
            #  setting boundaries for the first exiting variable v2
            if not isinstance(v2, list):
                if v2 > 0:
                    dx_B1_v2 = get_value_by_name(AAN1, v2, True)
                    lk2 = solution.klist == v2
                    del_x_0[lk2] = -0.5 * dx_B1_v2
                elif v2 < 0:
                    dq_DD_v2 = get_value_by_name(basis, v2, False)
                    lj2 = solution.jlist == -v2
                    q_N[lj2] = -dq_DD_v2
                    dq_B2_v2 = get_value_by_name(AAN2, v2, False)
                    del_q_N[lj2] = -0.5 * dq_B2_v2 + dq_DD_v2
        par_line = parametric_line(x_0, q_N, 1, 1, 0, del_x_0, del_q_N, None, None, pbaseB1red, pbaseB2red, line_type.SCLP_sub)
        par_line.build_boundary_sets(solution.klist, solution.jlist)
        return par_line

    @staticmethod
    def get_SCLP_parametric_line(formulation, tolerance):
        x_0, q_N = calc_boundaries(formulation, tolerance)
        return parametric_line(x_0, q_N, formulation.T)