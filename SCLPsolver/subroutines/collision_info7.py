from .rewind_info import rewind_info


class collision_info():

    def __init__(self, case, delta=None, N1=None, N2=None, v1=None, v2=None, had_resolution=False):
        self._N1 = N1
        self._N2 = N2
        if v1 is None:
            self._v1 = []
        else:
            self._v1 = v1
        if v2 is None:
            self._v2 = []
        else:
            self._v2 = v2
        self._case = case
        self._delta = delta
        self._lastN1 = None
        self._lastN2 = None
        self._Nnew = None
        self._rewind_info = None
        self._had_resolution = had_resolution

    @property
    def N1(self):
        return self._N1

    @property
    def N2(self):
        return self._N2

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def case(self):
        return self._case

    @case.setter
    def case(self, value):
        self._case = value

    def __eq__(self, other):
        return self._N1 == other.N1 and self._N2 == other.N2 and self._v1 == other.v1 and self._v2 == other.v2 and self._case == other.case

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self, value):
        self._delta = value

    @property
    def lastN1(self):
        return self._lastN1

    @property
    def lastN2(self):
        return self._lastN2

    @property
    def Nnew(self):
        return self._Nnew

    @lastN1.setter
    def lastN1(self, value):
        self._lastN1 = value

    @lastN2.setter
    def lastN2(self, value):
        self._lastN2 = value

    @Nnew.setter
    def Nnew(self, value):
        self._Nnew = value

    @property
    def rewind_info(self):
        return self._rewind_info

    @rewind_info.setter
    def rewind_info(self, value):
        self._rewind_info = value

    @property
    def had_resolution(self):
        return self._had_resolution
