import numpy as np
from .lp_tools.pivot import pivot_mn

#'#@profile
def get_new_dict(oldDict, oldPlace, newPlace, pivots):
    if isinstance(oldPlace, list):
        oldPlace = oldPlace[0]
        oldDict = oldDict[0]
    # assert(newPlace >=0 and newPlace < L, 'new dictionary place is out of a base sequence')
    # assert(oldPlace >=0 and oldPlace < L, 'old dictionary place is out of a base sequence')
    newDict = oldDict.copy()
    if oldPlace < newPlace:
        for i in range(oldPlace,newPlace):
            newDict = pivot_mn(newDict, pivots[i][0], pivots[i][1])
    if newPlace < oldPlace:
        for i in range(oldPlace-1, newPlace-1, -1):
            newDict = pivot_mn(newDict, pivots[i][1], pivots[i][0])
    return newDict

def calc_nearby_bases(N1, N2, pivots, bases, places):
    vec_places = np.asarray(places)
    NN = len(pivots)
    if N1 >= 0:
        test1 = np.fabs(vec_places - N1)
        ind1 = np.argmin(test1)
        if N2 <= NN:
            test2 = np.fabs(vec_places - N2)
            ind2 = np.argmin(test2)
            if test1[ind1] < test2[ind2]:
                return get_new_dict(bases[ind1], places[ind1], N1, pivots), N1
            else:
                return get_new_dict(bases[ind2], places[ind2], N2, pivots), N2
        else:
            return get_new_dict(bases[ind1], places[ind1], N1, pivots), N1
    else:
        test2 = np.fabs(vec_places - N2)
        ind2 = np.argmin(test2)
        return get_new_dict(bases[ind2], places[ind2], N2, pivots), N2