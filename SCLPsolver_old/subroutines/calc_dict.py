import numpy as np
from .get_new_dict import get_new_dict


#@profile
def calc_dict(base_sequence, N1, N2, pivots):
    NN = len(pivots)
    if N1 >= 0:
        test1 = np.fabs(np.asarray(base_sequence['places']) - N1)
        ind1 = np.argmin(test1)
        if N2 <= NN:
            test2 = np.fabs(np.asarray(base_sequence['places']) - N2)
            ind2 = np.argmin(test2)
            if test1[ind1] < test2[ind2]:
                return get_new_dict(base_sequence['bases'][ind2], base_sequence['places'][ind2], N2, pivots), N2
            else:
                return get_new_dict(base_sequence['bases'][ind1], base_sequence['places'][ind1], N1, pivots), N1
        else:
            return get_new_dict(base_sequence['bases'][ind1], base_sequence['places'][ind1], N1, pivots), N1
    else:
        test2 = np.fabs(np.array(base_sequence['places']) - N2)
        ind2 = np.argmin(test2)
        return get_new_dict(base_sequence['bases'][ind2], base_sequence['places'][ind2], N2, pivots), N2