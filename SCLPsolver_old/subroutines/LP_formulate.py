import numpy as np
from .matlab_utils import *
from .simplex_procedures import *


###@profile
def LP_formulate(AA, prim_name, dual_name,  Kset, Jset, tolerance = 0):
    nJset = [-v for v in Jset]
    prim_sign = np.zeros((len(prim_name),1), dtype = int)
    prim_sign[ismember(prim_name,Kset)] = 1
    prim_sign[ismember(prim_name,nJset)] = -1
    dual_sign = np.zeros((len(dual_name),1), dtype = int)
    dual_sign[ismember(dual_name,nJset)] = 1
    dual_sign[ismember(dual_name,Kset)] = -1
    A, pn, dn, ps, ds, err = simplex_procedures(AA.copy(), prim_name.copy(), dual_name.copy(), np.hstack(prim_sign), np.hstack(dual_sign), tolerance)
    return pn, dn, A