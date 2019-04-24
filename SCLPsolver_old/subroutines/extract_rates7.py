import numpy as np
from .matlab_utils import find
from .sparse_matrix_constructor import sparse_matrix_constructor
from .pivot import base_pivot


#'#@profile
def extract_rates_from_basis(prim_name, dual_name, dct, KK, JJ, totalK = None, totalJ = None):
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
        dx = sparse_matrix_constructor(dct[klist1+1,0], kord, KK)
    else:
        dx = sparse_matrix_constructor(dct[klist1+1,0], kn1-1, KK)
    if JJ < totalJ:
        jn1 = -prim_name[prim_name < 0]
        jord = np.argsort(np.argsort(np.hstack((jn1, jn2))))[len(jn1):]
        dq = sparse_matrix_constructor(dct[0,jlist2+1], jord, JJ)
    else:
        dq = sparse_matrix_constructor(dct[0,jlist2+1], jn2-1, JJ)
    return dx, dq

def extract_rates_from_subproblem(pivots, AAN1, AAN2, JJ, KK, totalJ, totalK):
    Npivots = len(pivots)
    # Warning this based on assumption that first basis in new_base_sequence is equal to the AAN1 and/or last basis is equal to the AAN2
    dx = sparse_matrix_constructor(None, None, KK)
    dq = sparse_matrix_constructor(None, None, JJ)
    if Npivots > 0:
        if AAN1 is not None:
            pm1 = AAN1['prim_name'].copy()
            dm1 = AAN1['dual_name'].copy()
            DD1 = AAN1['A'].copy()
            if AAN2 is not None:
                Npivots -= 1
                ran = enumerate(pivots[:-1])
            else:
                ran = enumerate(pivots)
            for i, piv1 in ran:
                DD1, pm1, dm1 = base_pivot(DD1, find(pm1 == piv1[0])[0], find(dm1 == piv1[1])[0], pm1, dm1)
                ndx, ndq = extract_rates_from_basis(pm1, dm1, DD1, KK, JJ, totalK, totalJ)
                dx.append(ndx)
                dq.append(ndq)
        else:
            pm1 = AAN2['prim_name'].copy()
            dm1 = AAN2['dual_name'].copy()
            DD1 = AAN2['A'].copy()
            for i, piv1 in enumerate(reversed(pivots)):
                DD1, pm1, dm1 = base_pivot(DD1, find(pm1 == piv1[1]), find(dm1 == piv1[0]), pm1, dm1)
                ndx, ndq = extract_rates_from_basis(pm1, dm1, DD1, KK, JJ, totalK, totalJ)
                dx.prepend(ndx)
                dq.prepend(ndq)
    return dx, dq