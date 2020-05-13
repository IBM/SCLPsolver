import numpy as np

from subroutines.get_new_dict import get_new_dict


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
                print('Old:', places[ind1])
                return get_new_dict(bases[ind1], places[ind1], N1, pivots), N1
            else:
                print('Old:', places[ind2])
                return get_new_dict(bases[ind2], places[ind2], N2, pivots), N2
        else:
            print('Old:', places[ind1])
            return get_new_dict(bases[ind1], places[ind1], N1, pivots), N1
    else:
        test2 = np.fabs(vec_places - N2)
        ind2 = np.argmin(test2)
        print('Old:', places[ind2])
        return get_new_dict(bases[ind2], places[ind2], N2, pivots), N2