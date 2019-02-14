from .matlab_utils import *
from .pivot import dict_pivot


def get_new_dict(oldDict, oldPlace, newPlace, pivots):
    L = len(pivots)
    if isinstance(oldPlace, list):
        oldPlace = oldPlace[0]
        oldDict = oldDict[0]
    assert(newPlace >=0 and newPlace < L, 'new dictionary place is out of a base sequence')
    assert(oldPlace >=0 and oldPlace < L, 'old dictionary place is out of a base sequence')
    newDict={'A':oldDict['A'].copy(), 'prim_name':oldDict['prim_name'].copy(), 'dual_name':oldDict['dual_name'].copy()}
    if oldPlace < newPlace:
        for i in range(oldPlace,newPlace):
            out_v = find(newDict['prim_name'] == pivots[i][0])
            in_v = find(newDict['dual_name'] == pivots[i][1])
            newDict = dict_pivot(newDict, out_v, in_v)
    if newPlace < oldPlace:
        for i in range(oldPlace-1, newPlace-1, -1):
            out_v = find(newDict['prim_name'] == pivots[i][1])
            in_v = find(newDict['dual_name'] == pivots[i][0])
            newDict = dict_pivot(newDict, out_v, in_v)
    return newDict