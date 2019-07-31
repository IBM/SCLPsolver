import numpy as np
from .matlab_utils import ismember
from .simplex_procedures import simplex_procedures


class LP_formulation():

    __slots__ = ["simplex_dict", "prim_name", "dual_name", "prim_sign", "dual_sign"]

    def __init__(self, simplex_dict, prim_name, dual_name, prim_sign=None, dual_sign=None):
        self.simplex_dict, self.prim_name, self.dual_name, self.prim_sign, self.dual_sign =\
            simplex_dict, prim_name, dual_name, prim_sign, dual_sign
        
def solve_ratesLP(LP_form, Kset, nJset, tmp_matrix, tolerance=0):
    prim_sign = np.zeros((len(LP_form.prim_name)), dtype=int)
    prim_sign[ismember(LP_form.prim_name, Kset)] = 1
    prim_sign[ismember(LP_form.prim_name, nJset)] = -1
    dual_sign = np.zeros((len(LP_form.dual_name)), dtype=int)
    dual_sign[ismember(LP_form.dual_name, nJset)] = 1
    dual_sign[ismember(LP_form.dual_name, Kset)] = -1
    A, pn, dn, ps, ds, err = simplex_procedures(LP_form.simplex_dict.copy(), LP_form.prim_name.copy(), LP_form.dual_name.copy(),
                                                prim_sign, dual_sign, tmp_matrix, tolerance)
    return LP_formulation(A, pn, dn), err

def solve_LP(LP_form, tmp_matrix, tolerance=0):
    A, pn, dn, ps, ds, err = simplex_procedures(LP_form.simplex_dict.copy(), LP_form.prim_name.copy(), LP_form.dual_name.copy(),
                                                LP_form.prim_sign, LP_form.dual_sign, tmp_matrix, tolerance)
    return LP_formulation(A, pn, dn, ps, ds), err

def solve_LP_in_place(LP_form, tmp_matrix, tolerance=0):
    LP_form.simplex_dict, LP_form.prim_name, LP_form.dual_name, LP_form.prim_sign, LP_form.dual_sign, err =\
        simplex_procedures(LP_form.simplex_dict, LP_form.prim_name, LP_form.dual_name, LP_form.prim_sign, LP_form.dual_sign, tmp_matrix, tolerance)
    return err




