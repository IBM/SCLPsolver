import numpy as np
from .matlab_utils import find
from .LP_formulation import LP_formulation, get_dx_names, get_dq_names

#'#@profile
def prepare_subproblem_basis(basis, Kset_0, Jset_N, v1, v2, AAN1, AAN2):

    pbaseB1red = None
    pbaseB2red = None

    if AAN1 is None:
        Kex1 = np.intersect1d(get_dx_names(basis), Kset_0, assume_unique=True)
        Kexclude = np.intersect1d(Kex1, get_dx_names(AAN2), assume_unique=True)
        Jexclude = -np.intersect1d(get_dq_names(basis), get_dq_names(AAN2), assume_unique=True)
    elif AAN2 is None:
        Kexclude = np.intersect1d(get_dx_names(basis), get_dx_names(AAN1), assume_unique=True)
        Jex1 = np.intersect1d(get_dq_names(basis), np.asarray([-v for v in Jset_N]), assume_unique=True)
        Jexclude = -np.intersect1d(Jex1, get_dq_names(AAN1), assume_unique=True)
    else:
        Kexclude = np.intersect1d(get_dx_names(AAN1), get_dx_names(AAN2), assume_unique=True)
        Jexclude = -np.intersect1d(get_dq_names(AAN1), get_dq_names(AAN2), assume_unique=True)
        if not isinstance(v1, list):
            Kexclude = Kexclude[Kexclude != v1]
            Jexclude = Jexclude[Jexclude != -v1]
        if not isinstance(v2, list):
            Kexclude = Kexclude[Kexclude != v2]
            Jexclude = Jexclude[Jexclude != -v2]

    if AAN1 is not None:
        pbaseB1red = AAN1.prim_name[np.logical_not(np.in1d(AAN1.prim_name, Kexclude, assume_unique=True))]
    if AAN2 is not None:
        pbaseB2red = AAN2.prim_name[np.logical_not(np.in1d(AAN2.prim_name, Kexclude, assume_unique=True))]

    lKDDin = np.logical_not(np.in1d(basis.prim_name, Kexclude, assume_unique=True))
    lJDDin = np.logical_not(np.in1d(basis.dual_name, -Jexclude, assume_unique=True))
    DDred = basis.simplex_dict[find(np.hstack(([True], lKDDin)))[:, None], find(np.hstack(([True], lJDDin)))]
    return LP_formulation(DDred, basis.prim_name[lKDDin], basis.dual_name[lJDDin]), pbaseB1red, pbaseB2red

