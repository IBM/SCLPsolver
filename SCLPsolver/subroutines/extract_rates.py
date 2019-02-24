import numpy as np
from .matlab_utils import *
from scipy.sparse import coo_matrix

def extract_rates(prim_name, dual_name, dct, KK, JJ, totalK = None, totalJ = None):
    if totalK is None:
        totalK = KK
    if totalJ is None:
        totalJ = JJ
    klist1 = find(prim_name > 0)
    jlist2 = find(dual_name < 0)
    kn1 =  prim_name[klist1]
    jn2 = -dual_name[jlist2]
    if KK < totalK:
        kn2 =  dual_name[dual_name > 0]
        kord = np.argsort(np.argsort(np.hstack((kn1, kn2))))[:len(kn1)]
        dx = coo_matrix((dct[klist1+1,0], (kord, np.zeros(len(kord)))), shape=(KK, 1))
    else:
        dx = coo_matrix((dct[klist1+1,0], (kn1-1, np.zeros(len(kn1)))), shape=(KK, 1))
    if JJ < totalJ:
        jn1 = -prim_name[prim_name < 0]
        jord = np.argsort(np.argsort(np.hstack((jn1, jn2))))[len(jn1):]
        dq = coo_matrix((dct[0,jlist2+1],(jord,np.zeros(len(jord)))),shape=(JJ,1))
    else:
        dq = coo_matrix((dct[0,jlist2+1],(jn2-1,np.zeros(len(jn2)))),shape=(JJ,1))
    return dx, dq