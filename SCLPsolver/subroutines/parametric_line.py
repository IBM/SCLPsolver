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