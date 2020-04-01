import numpy as np


def load_data(path):
    G = np.load(path + '/G.dat', allow_pickle=True)
    F = np.load(path + '/F.dat', allow_pickle=True)
    H = np.load(path + '/H.dat', allow_pickle=True)
    a = np.hstack(np.load(path + '/a.dat', allow_pickle=True))
    b = np.hstack(np.load(path + '/b.dat', allow_pickle=True))
    c = np.hstack(np.load(path + '/c.dat', allow_pickle=True))
    d = np.load(path + '/d.dat', allow_pickle=True)
    if np.size(d) ==0:
        d = np.empty(shape=(0))
    if np.size(F) ==0:
        F = np.empty(shape=(G.shape[0], 0))
    alpha = np.hstack(np.load(path + '/alpha.dat', allow_pickle=True))
    gamma = np.hstack(np.load(path + '/gamma.dat', allow_pickle=True))
    return G, H, F, gamma, c, d, alpha, a, b, None