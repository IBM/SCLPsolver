import numpy as np
from .lp_tools.pivot import pivot_mn
from .lp_tools.LP_formulation import LP_formulation

def get_new_dict(dct, oldPlace, newPlace, pivots, preserve = True):
    if isinstance(oldPlace, list):
        oldPlace = oldPlace[0]
        dct = dct[0]
    if preserve:
        tmp_dict = LP_formulation(np.empty_like(dct.simplex_dict), None, None)
    else:
        tmp_dict = None
    if oldPlace < newPlace:
        for i in range(oldPlace,newPlace):
            dct = pivot_mn(dct, pivots[i][0], pivots[i][1], tmp_dict)
            tmp_dict= None
    elif newPlace < oldPlace:
        for i in range(oldPlace-1, newPlace-1, -1):
            dct = pivot_mn(dct, pivots[i][1], pivots[i][0], tmp_dict)
            tmp_dict = None
    return dct
