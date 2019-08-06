class eta_matrix():

    __slots__= ['_v','_p']

    def __init__(self, v, p):
        self._v = v
        self._p = p

    @property
    def v(self):
        return self._v

    @property
    def p(self):
        return self._p

    # standard ftran operation on vector
    def ftran(self, vec):
        if vec[self._p] == 0:
            return vec
        else:
            ap = vec[self._p] * self._v[self._p]
            vv = vec + vec[self._p] * self._v
            vv[self._p] = ap
            return vv

    # inverse ftran operation on vector
    def inv_ftran(self, vec):
        if vec[self._p] == 0:
            return vec
        else:
            ap = vec[self._p] / self._v[self._p]
            vp = vec - self._v * ap
            vp[self._p] = ap
            return vp

    # standard ftran changing vector itself
    def fftran(self, vec):
        if vec[self._p] == 0:
            return vec
        else:
            ap = vec[self._p] * self._v[self._p]
            vec += vec[self._p] * self._v
            vec[self._p] = ap
            return vec

    # inverse ftran changing vector itself
    def inv_fftran(self, vec):
        if vec[self._p] == 0:
            return vec
        else:
            ap = vec[self._p] / self._v[self._p]
            vec -= self._v * ap
            vec[self._p] = ap
            return vec

    # produce eta matrix representation from vector
    @staticmethod
    def get_from_vector(vec, p):
        ap = -vec[p]
        vp = vec/ap
        vp[p] = -1/ap
        return eta_matrix(vp, p)

    # produce eta matrix representation using vectors before and after ftran
    @staticmethod
    def get_from_ftran(v2, v1, p):
        if v1[p] == 0:
            return None
        else:
            vp = (v2 - v1) / v1[p]
            vp[p] = v2[p]/v1[p]
            return eta_matrix(vp, p)

    # perform in place ftran without creation of eta matrix
    @staticmethod
    def get_fftran(vec, eta, p):
        if vec[p] == 0:
            return vec
        ap = vec[p]/eta[p]
        vec -= eta * ap
        vec[p] = ap
        return vec
