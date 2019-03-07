

class rewind_info():

    def __init__(self, solution, N1, N2):
        cor_N1 = N1 + 1
        if N1 > -1:
            self._pivots = solution.pivots[N1:N2 + 1].copy()
        else:
            self._pivots = solution.pivots[N1 + 1:N2 + 1].copy()
        self._dx = solution.dx.get_sub_matrix(cor_N1, N2)
        self._dq = solution.dq.get_sub_matrix(cor_N1, N2)

    @property
    def pivots(self):
        return self._pivots

    @property
    def dx(self):
        return self._dx

    @property
    def dq(self):
        return self._dq