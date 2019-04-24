import numpy as np


#function[Obj, Err] =
def calc_objective(alpha, a, b, gamma, c, d, u, x, p, q, tau):

    J = len(gamma)
    K = len(alpha)

    NN = len(tau)
    t = np.cumsum(np.hstack((0., tau)))
    TT = t[NN]
    part1 = np.dot(np.dot(gamma, u[:J,:]), tau)
    ddtau = tau*(t[:-1] + t[1:])/2
    part2 = np.dot(np.dot(c, u[:J,:]), tau * TT - ddtau)
    if d.size == 0:
        part3 = 0
    else:
        part3 = np.dot(np.dot(d,  ((x[K:, :-1]+x[K:, 1:])/ 2)),tau)
    primobjective = part1 + part2 + part3
    part4 = np.dot(np.dot(alpha,p[:K,:]),tau)
    part5 = np.dot(np.dot(a,p[:K,:]), ddtau)
    if b.size == 0:
        part6 = 0
    else:
        part6 = np.dot(np.dot(b,  ((q[J:, :-1]+q[J:, 1:])/ 2)),tau)
    dualobjective = part4 + part5 + part6
    obj = (primobjective + dualobjective) / 2
    err = abs(dualobjective - primobjective)
    return obj, err