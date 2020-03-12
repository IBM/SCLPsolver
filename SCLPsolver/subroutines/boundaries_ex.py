



class boundaries():
    __slots__ = ['x0', 'u0', 'uN', 'xN', 'q0', 'qN', 'p0', 'pN']

    def __init__(self, x0=None, u0=None, uN=None, xN=None, q0=None, p0=None, qN=None, pN=None):
        self.x0 = x0
        self.u0 = u0
        self.uN = uN
        self.xN = xN
        self.q0 = q0
        self.p0 = p0
        self.qN = qN
        self.pN = pN