import scipy.sparse as sp
from .matlab_utils import *
from .calc_dict import calc_dict
from .get_new_dict import get_new_dict
from scipy.sparse import coo_matrix


def calc_controls(base_sequence, pivots, JJ, KK):
    NN = len(base_sequence['dx'])
    new_dict, xxx = calc_dict(base_sequence, 0, 0, pivots)
    u = []
    p = []
    for place in range(NN):
        klist2 = find(new_dict['dual_name'] > 0)
        jlist1 = find(new_dict['prim_name'] < 0)
        kn2 =  new_dict['dual_name'][klist2]
        jn1 = -new_dict['prim_name'][jlist1]
        u.append(coo_matrix((new_dict['A'][jlist1+1,0], (jn1-1, np.zeros(len(jn1)))), shape=(JJ, 1)))
        p.append(coo_matrix((new_dict['A'][0,klist2+1], (kn2-1, np.zeros(len(kn2)))), shape=(KK, 1)))
        if place < NN - 1:
            new_dict = get_new_dict(new_dict, place, place+1, pivots)
    return sp.hstack(u), sp.hstack(p)