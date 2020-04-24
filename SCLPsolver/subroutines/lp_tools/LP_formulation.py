import numpy as np
from .simplex_procedures import simplex_procedures
from .cy_lp_tools import get_sign


class LP_formulation():

    __slots__ = ["simplex_dict", "prim_name", "dual_name", "prim_sign", "dual_sign"]

    def __init__(self, simplex_dict, prim_name, dual_name, prim_sign=None, dual_sign=None):
        self.simplex_dict, self.prim_name, self.dual_name, self.prim_sign, self.dual_sign =\
            simplex_dict, prim_name, dual_name, prim_sign, dual_sign

    def __copy__(self):
        if self.prim_sign is None:
            return LP_formulation(self.simplex_dict.copy(), self.prim_name.copy(), self.dual_name.copy())
        else:
            return LP_formulation(self.simplex_dict.copy(), self.prim_name.copy(), self.dual_name.copy(), self.prim_sign.copy(), self.dual_sign.copy())

    def copy(self):
        return self.__copy__()
        
def solve_ratesLP(LP_form, Kset, nJset, bases_mm, tolerance=0):
    prim_sign = get_sign(LP_form.prim_name, Kset, nJset, 1)
    dual_sign = get_sign(LP_form.dual_name, Kset, nJset, -1)
    tmp_dict = bases_mm.pop()
    if tmp_dict is None:
        tmp_dict = LP_formulation(np.empty_like(LP_form.simplex_dict), None, None)
        #LP_form, ps, ds, pivots, err = simplex_procedures(LP_form.copy(), prim_sign, dual_sign, tolerance)
    #else:
    LP_form, ps, ds, pivots, err = simplex_procedures(LP_form, prim_sign, dual_sign, tolerance, tmp_dict)
    return LP_form, pivots, err

def solve_LP(LP_form, ps, ds, tolerance=0):
    LP_form, ps, ds, pivots, err = simplex_procedures(LP_form.copy(), ps, ds, tolerance)
    return LP_form, err

def solve_LP_in_place(LP_form, ps, ds, tolerance=0):
    LP_form, ps, ds, pivots, err = simplex_procedures(LP_form, ps, ds, tolerance)
    return LP_form, err


def get_pivot(b1, b2, prim):
    if prim:
        return np.setdiff1d(b1.prim_name, b2.prim_name, assume_unique=True)
    else:
        return np.setdiff1d(b1.dual_name, b2.dual_name, assume_unique=True)


def get_value_by_name(basis, name, prim):
    if prim:
        return basis.simplex_dict[1:, 0][basis.prim_name == name][0]
    else:
        return basis.simplex_dict[0, 1:][basis.dual_name == name][0]

def get_dx_names(basis):
    return basis.prim_name[basis.prim_name > 0]

def get_dq_names(basis):
    return basis.dual_name[basis.dual_name < 0]




