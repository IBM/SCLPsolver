import numpy as np


#this function should get original matrix H, degrees of perturbation (d), i.e. \tau_gal = d \tau and uncertainty budget
# and return two matricies - one eith coefficients related to u_j and one with coefficients related to \alpha and \beta
def do_server_robust_reformulation(H, degree, budget, separate = True):
    if separate:
        H0_alpha = np.divide(H, H, where=H != 0, out=np.zeros_like(H))
        H0_beta = np.diag(budget)
        H1 = -np.diag(np.sum(H, axis=0) * degree)
        H1_alpha = np.eye(H.shape[1])
        H1_beta = H0_alpha.T
        return H0_alpha, H0_beta, H1, H1_alpha, H1_beta
    else:
        ab_dim = np.sum(H.shape)
        Hnew = np.zeros((ab_dim, ab_dim+ H.shape[1]))
        Hnew[:H.shape[0],:H.shape[1]] = H
        np.divide(H, H, where=H != 0, out=Hnew[:H.shape[0], H.shape[1]:2*H.shape[1]])
        Hnew[:H.shape[0], 2*H.shape[1]:] = np.diag(budget)
        Hnew[H.shape[0]:,:H.shape[1]] = -np.diag(np.sum(H, axis=0) * degree)
        Hnew[H.shape[0]:, H.shape[1]:2 * H.shape[1]] = np.eye(H.shape[1])
        Hnew[H.shape[0]:, 2*H.shape[1]:] = Hnew[:H.shape[0], H.shape[1]:2*H.shape[1]].T
        return Hnew