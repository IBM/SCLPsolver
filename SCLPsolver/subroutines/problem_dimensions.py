

class problem_dimensions():

    def __init__(self, KK, JJ, totalK=None, totalJ=None):
        self._j = JJ
        self._k = KK
        self._totalJ = totalJ
        self._totalK = totalK

    @property
    def JJ(self):
        return self._j

    @property
    def KK(self):
        return self._k

    @property
    def totalJ(self):
        if self._totalJ is None:
            return self._j
        else:
            return self._totalJ

    @property
    def totalK(self):
        if self._totalK is None:
            return self._k
        else:
            return self._totalK