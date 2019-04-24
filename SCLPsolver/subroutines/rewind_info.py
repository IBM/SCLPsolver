

class rewind_info():

    def __init__(self, pivots, dx, dq):
        self._pivots = pivots
        self._dx = dx
        self._dq = dq

    @property
    def pivots(self):
        return self._pivots

    @property
    def dx(self):
        return self._dx

    @property
    def dq(self):
        return self._dq