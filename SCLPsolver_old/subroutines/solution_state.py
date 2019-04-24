import numpy as np
from .calc_equations6 import calc_equations
from .calc_states6 import calc_states


class solution_state():

    def __init__(self, sol_dx, sol_dq, pivots, param_line):
        self._dx = sol_dx.get_matrix()
        self._dq = sol_dq.get_matrix()
        self._sdx = np.ones((self._dx.shape[0], self._dx.shape[1] + 2))
        self._sdq = np.ones((self._dq.shape[0], self._dq.shape[1] + 2))
        np.sign(self._dx, out=self._sdx[:, 1:-1])
        np.sign(self._dq, out=self._sdq[:, 1:-1])
        self._tau, self._dtau = calc_equations(param_line, pivots, self._dx, self._dq)
        self._x, self._del_x, self._q, self._del_q = calc_states(self._dx, self._dq, param_line, self._tau, self._dtau, self._sdx, self._sdq)

    @property
    def dx(self):
        return self._dx

    @property
    def dq(self):
        return self._dq

    @property
    def sdx(self):
        return self._sdx

    @property
    def sdq(self):
        return self._sdq

    @property
    def x(self):
        return self._x

    @property
    def q(self):
        return self._q

    @property
    def del_x(self):
        return self._del_x

    @property
    def del_q(self):
        return self._del_q

    @property
    def tau(self):
        return self._tau

    @property
    def dtau(self):
        return self._dtau