from .lp_tools.pivot import pivot_mn

#'#@profile
def get_new_dict(oldDict, oldPlace, newPlace, pivots):
    L = len(pivots)
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