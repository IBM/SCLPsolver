import numpy as np

class SCLP_formulation():

    __slots__ = ["G", "F", "H", "a", "b", "c", "d", "alpha", "gamma", "T", "I", "J", "K", "L"]

    def __init__(self, G, F, H, a, b, c, d, alpha, gamma, T):
        self.G, self.F, self.H, self.a, self.b, self.c, self.d, self.alpha, self.gamma, self.T = G, F, H, a, b, c, d, alpha, gamma, T
        self.K = G.shape[0]
        self.J = G.shape[1]
        self.I = H.shape[0]
        self.L = F.shape[1]

    def get_ratesLP_basis(self):
        return np.vstack((-np.hstack((0, self.c, self.d)), np.hstack((np.vstack(self.a), self.G, self.F)),
                          np.hstack((np.vstack(self.b), self.H, np.zeros((self.I, self.L))))))
