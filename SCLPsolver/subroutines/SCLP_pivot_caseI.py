import numpy as np
from .matlab_utils import find
from .calc_dict import calc_dict

####'#@profile
def SCLP_pivot_caseI(base_sequence, pivots, prim_name, dual_name, N1, N2, NN):
    lplaces = np.logical_or(np.array(base_sequence['places']) <= N1, np.array(base_sequence['places']) >= N2)
    places = find(lplaces)
    # print(N1, N2, Nnew)
    if len(places) == 0:
        newMat, newPlace = calc_dict(base_sequence, N1, N2, pivots)
        base_sequence['bases'] = [newMat]
        base_sequence['places'] = [newPlace]
    else:
        base_sequence['bases'] = [base_sequence['bases'][i] for i in places]
        newPlace = [base_sequence['places'][i] for i in places]
        base_sequence['places'] = [v if v < N2 else v - (N2 - N1 - 1) for v in newPlace]

    base_sequence['dx'] = base_sequence['dx'][0: N1+1] + base_sequence['dx'][N2:]
    base_sequence['dq'] = base_sequence['dq'][0: N1+1] + base_sequence['dq'][N2:]

    if N1>=0:
        pivots_new = pivots[0:N1]
    else:
        pivots_new = []
    if N1 >=0 and N2 < NN:
        pivots_new.append(np.setdiff1d(prim_name[:,N1],prim_name[:,N2], assume_unique =True).tolist()
                          + np.setdiff1d(dual_name[:,N1],dual_name[:,N2], assume_unique =True).tolist())
    pivots_new = pivots_new + pivots[N2:]
    prim_name = np.hstack((prim_name[:,0:N1+1], prim_name[:,N2:]))
    dual_name = np.hstack((dual_name[:,0:N1+1], dual_name[:,N2:]))
    return base_sequence, pivots_new, prim_name, dual_name

