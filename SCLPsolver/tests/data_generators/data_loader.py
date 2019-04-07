import numpy as np


def load_data(K, I, seed, path):
    path = path +'/K' + str(K) + '/I' + str(I) + '/seed' + str(seed) + '/'
    G = np.load(path + 'G.dat')
    F = np.load(path + 'F.dat')
    H = np.load(path + 'H.dat')
    a = np.hstack(np.load(path + 'a.dat'))
    b = np.hstack(np.load(path + 'b.dat'))
    c = np.hstack(np.load(path + 'c.dat'))
    d = np.load(path + 'd.dat')
    if np.size(d) ==0:
        d = np.empty(shape=(0))
    if np.size(F) ==0:
        F = np.empty(shape=(G.shape[0], 0))
    alpha = np.hstack(np.load(path + 'alpha.dat'))
    gamma = np.hstack(np.load(path + 'gamma.dat'))
    return G, H, F, gamma, c, d, alpha, a, b, None