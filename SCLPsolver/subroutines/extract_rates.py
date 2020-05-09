import numpy as np
from .matlab_utils import find
from .matrix_constructor import matrix_constructor
from .lp_tools.pivot import pivot_mn


#'#@profile
def extract_rates_from_basis(dct, problem_dims):
    klist1 = find(dct.prim_name > 0)
    jlist2 = find(dct.dual_name < 0)
    kn1 =  dct.prim_name[klist1]
    jn2 = -dct.dual_name[jlist2]
    if problem_dims.KK < problem_dims.totalK:
        kn2 =  dct.dual_name[dct.dual_name > 0]
        kord = np.argsort(np.argsort(np.hstack((kn1, kn2))))[:len(kn1)]
        dx = (dct.simplex_dict[klist1+1,0], kord)
    else:
        dx = (dct.simplex_dict[klist1+1,0], kn1-1)
    if problem_dims.JJ < problem_dims.totalJ:
        jn1 = -dct.prim_name[dct.prim_name < 0]
        jord = np.argsort(np.argsort(np.hstack((jn1, jn2))))[len(jn1):]
        dq = (dct.simplex_dict[0,jlist2+1], jord)
    else:
        dq = (dct.simplex_dict[0,jlist2+1], jn2-1)
    return dx, dq

def extract_rates_from_partial(prim_vars, dual_vars, prim_name, dual_name, problem_dims):
    klist1 = find(prim_name > 0)
    jlist2 = find(dual_name < 0)
    kn1 =  prim_name[klist1]
    jn2 = -dual_name[jlist2]
    if problem_dims.KK < problem_dims.totalK:
        kn2 =  dual_name[dual_name > 0]
        kord = np.argsort(np.argsort(np.hstack((kn1, kn2))))[:len(kn1)]
        dx = (prim_vars[klist1+1], kord)
    else:
        dx = (prim_vars[klist1+1], kn1-1)
    if problem_dims.JJ < problem_dims.totalJ:
        jn1 = -prim_name[prim_name < 0]
        jord = np.argsort(np.argsort(np.hstack((jn1, jn2))))[len(jn1):]
        dq = (dual_vars[jlist2+1], jord)
    else:
        dq = (dual_vars[jlist2+1], jn2-1)
    return dx, dq

def extract_rates_from_subproblem(pivots, AAN1, AAN2, problem_dims):
    # Warning this based on assumption that first basis in new_base_sequence is equal to the AAN1 and/or last basis is equal to the AAN2
    if len(pivots) > 0:
        if AAN1 is not None:
            AAN1 = AAN1.copy()
            if AAN2 is not None:
                ran = enumerate(pivots[:-1])
                dx = matrix_constructor(None, None, problem_dims.KK, -1, len(pivots))
                dq = matrix_constructor(None, None, problem_dims.JJ, -1, len(pivots))
            else:
                ran = enumerate(pivots)
                dx = matrix_constructor(None, None, problem_dims.KK, -1, len(pivots)+1)
                dq = matrix_constructor(None, None, problem_dims.JJ, -1, len(pivots)+1)
            for i, piv1 in ran:
                AAN1 = pivot_mn(AAN1, piv1[0], piv1[1])
                ndx, ndq = extract_rates_from_basis(AAN1, problem_dims)
                dx.append(ndx)
                dq.append(ndq)
        else:
            dx = matrix_constructor(None, None, problem_dims.KK, 1, len(pivots) + 1)
            dq = matrix_constructor(None, None, problem_dims.JJ, 1, len(pivots) + 1)
            AAN2 = AAN2.copy()
            for i, piv1 in enumerate(reversed(pivots)):
                AAN2 = pivot_mn(AAN2, piv1[1], piv1[0])
                ndx, ndq = extract_rates_from_basis(AAN2, problem_dims)
                dx.prepend(ndx)
                dq.prepend(ndq)
    else:
        dx = matrix_constructor(None, None, problem_dims.KK, -1, 1)
        dq = matrix_constructor(None, None, problem_dims.JJ, -1, 1)
    return dx.get_matrix(), dq.get_matrix()