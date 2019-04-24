import numpy as np
from .matlab_utils import ismember
from .simplex_procedures import simplex_procedures


#'#@profile
def LP_formulate(AA, prim_name, dual_name,  Kset, nJset, tolerance = 0):
    prim_sign = np.zeros((len(prim_name)), dtype = int)
    prim_sign[ismember(prim_name,Kset)] = 1
    prim_sign[ismember(prim_name,nJset)] = -1
    dual_sign = np.zeros((len(dual_name)), dtype = int)
    dual_sign[ismember(dual_name,nJset)] = 1
    dual_sign[ismember(dual_name,Kset)] = -1
    A, pn, dn, ps, ds, err = simplex_procedures(AA.copy(), prim_name.copy(), dual_name.copy(), prim_sign, dual_sign, tolerance)
    return pn, dn, A