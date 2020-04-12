from .matlab_utils import find
from .cy_lp_tools import cy_pivot, copy_pivot
#from scipy.linalg.blas import dger

def pivot_ij(dct, i, j, tmp_dict = None):
    if tmp_dict is None:
        in_, out_ = cy_pivot(dct.simplex_dict, dct.prim_name, dct.dual_name, i, j)
        return dct, in_, out_
    else:
        tmp_dict.prim_name = dct.prim_name.copy()
        tmp_dict.dual_name = dct.dual_name.copy()
        in_, out_ = copy_pivot(dct.simplex_dict, tmp_dict.prim_name, tmp_dict.dual_name, i, j, tmp_dict.simplex_dict)
        return tmp_dict, in_, out_

def pivot_mn(dct, m, n, tmp_dict = None):
    i = find(dct.prim_name == m)
    j = find(dct.dual_name == n)
    if i.size != 1 or j.size != 1:
        raise Exception('Bad pivot names!')
    return pivot_ij(dct, i, j, tmp_dict)[0]

def signed_pivot_ij(dct, ps, ds, i, j, tmp_dict = None):
    sam = ps[i]
    ps[i] = - ds[j]
    ds[j] = - sam
    return pivot_ij(dct, i, j, tmp_dict), ps, ds

def signed_pivot_mn(dct, ps, ds, m, n, tmp_dict = None):
    i = find(dct.prim_name == m)
    j = find(dct.dual_name == n)
    if i.size != 1 or j.size != 1:
        raise Exception('Bad pivot names!')
    return signed_pivot_ij(dct, ps, ds, i, j, tmp_dict)