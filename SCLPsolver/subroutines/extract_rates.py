import numpy as np
from .matlab_utils import find
from .matrix_constructor import matrix_constructor
from .pivot import base_pivot


#'#@profile
def extract_rates_from_basis(prim_name, dual_name, dct, problem_dims):
    klist1 = find(prim_name > 0)
    jlist2 = find(dual_name < 0)
    kn1 =  prim_name[klist1]
    jn2 = -dual_name[jlist2]
    if problem_dims.KK < problem_dims.totalK:
        kn2 =  dual_name[dual_name > 0]
        kord = np.argsort(np.argsort(np.hstack((kn1, kn2))))[:len(kn1)]
        dx = (dct[klist1+1,0], kord)
    else:
        dx = (dct[klist1+1,0], kn1-1)
    if problem_dims.JJ < problem_dims.totalJ:
        jn1 = -prim_name[prim_name < 0]
        jord = np.argsort(np.argsort(np.hstack((jn1, jn2))))[len(jn1):]
        dq = (dct[0,jlist2+1], jord)
    else:
        dq = (dct[0,jlist2+1], jn2-1)
    return dx, dq

def extract_rates_from_subproblem(pivots, AAN1, AAN2, problem_dims, tmp_matrix):
    # Warning this based on assumption that first basis in new_base_sequence is equal to the AAN1 and/or last basis is equal to the AAN2
    if len(pivots) > 0:
        if AAN1 is not None:
            pm1 = AAN1['prim_name'].copy()
            dm1 = AAN1['dual_name'].copy()
            DD1 = AAN1['A'].copy()
            if AAN2 is not None:
                ran = enumerate(pivots[:-1])
                dx = matrix_constructor(None, None, problem_dims.KK, -1, len(pivots))
                dq = matrix_constructor(None, None, problem_dims.JJ, -1, len(pivots))
            else:
                ran = enumerate(pivots)
                dx = matrix_constructor(None, None, problem_dims.KK, -1, len(pivots)+1)
                dq = matrix_constructor(None, None, problem_dims.JJ, -1, len(pivots)+1)
            for i, piv1 in ran:
                DD1, pm1, dm1 = base_pivot(DD1, find(pm1 == piv1[0])[0], find(dm1 == piv1[1])[0], pm1, dm1, tmp_matrix)
                ndx, ndq = extract_rates_from_basis(pm1, dm1, DD1, problem_dims)
                dx.append(ndx)
                dq.append(ndq)
        else:
            dx = matrix_constructor(None, None, problem_dims.KK, 1, len(pivots) + 1)
            dq = matrix_constructor(None, None, problem_dims.JJ, 1, len(pivots) + 1)
            pm1 = AAN2['prim_name'].copy()
            dm1 = AAN2['dual_name'].copy()
            DD1 = AAN2['A'].copy()
            for i, piv1 in enumerate(reversed(pivots)):
                DD1, pm1, dm1 = base_pivot(DD1, find(pm1 == piv1[1]), find(dm1 == piv1[0]), pm1, dm1, tmp_matrix)
                ndx, ndq = extract_rates_from_basis(pm1, dm1, DD1, problem_dims)
                dx.prepend(ndx)
                dq.prepend(ndq)
    else:
        dx = matrix_constructor(None, None, problem_dims.KK, -1, 1)
        dq = matrix_constructor(None, None, problem_dims.JJ, -1, 1)
    return dx.get_matrix(), dq.get_matrix()