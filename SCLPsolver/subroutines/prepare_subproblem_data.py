import numpy as np
from .matlab_utils import find
from .LP_formulation import LP_formulation

#'#@profile
def prepare_subproblem_basis(DD, pbaseDD, dbaseDD, Kset_0, Jset_N, v1, v2, AAN1, AAN2):

    pbaseB1red = None
    pbaseB2red = None

    if AAN1 is None:
        pbaseB2 = AAN2['prim_name']
        dbaseB2 = AAN2['dual_name']
        Kex1 = np.intersect1d(pbaseDD[pbaseDD > 0], Kset_0, assume_unique=True)
        Kexclude = np.intersect1d(Kex1, pbaseB2[pbaseB2 > 0], assume_unique=True)
        Jexclude = -np.intersect1d(dbaseDD[dbaseDD < 0], dbaseB2[dbaseB2 < 0], assume_unique=True)
    elif AAN2 is None:
        pbaseB1 = AAN1['prim_name']
        dbaseB1 = AAN1['dual_name']
        Kexclude = np.intersect1d(pbaseDD[pbaseDD > 0], pbaseB1[pbaseB1 > 0], assume_unique=True)
        Jex1 = np.intersect1d(dbaseDD[dbaseDD < 0], np.asarray([-v for v in Jset_N]), assume_unique=True)
        Jexclude = -np.intersect1d(Jex1, dbaseB1[dbaseB1 < 0], assume_unique=True)
    else:
        pbaseB1 = AAN1['prim_name']
        dbaseB1 = AAN1['dual_name']
        pbaseB2 = AAN2['prim_name']
        dbaseB2 = AAN2['dual_name']
        Kexclude = np.intersect1d(pbaseB1[pbaseB1 > 0], pbaseB2[pbaseB2 > 0], assume_unique=True)
        Jexclude = -np.intersect1d(dbaseB1[dbaseB1 < 0], dbaseB2[dbaseB2 < 0], assume_unique=True)
        if not isinstance(v1, list):
            Kexclude = Kexclude[Kexclude != v1]
            Jexclude = Jexclude[Jexclude != -v1]
        if not isinstance(v2, list):
            Kexclude = Kexclude[Kexclude != v2]
            Jexclude = Jexclude[Jexclude != -v2]

    lKDDin = np.logical_not(np.in1d(pbaseDD, Kexclude, assume_unique=True))
    lJDDin = np.logical_not(np.in1d(dbaseDD, -Jexclude, assume_unique=True))
    pbaseDDred = pbaseDD[lKDDin]
    dbaseDDred = dbaseDD[lJDDin]
    DDred = DD[find(np.hstack(([True], lKDDin)))[:, None], find(np.hstack(([True], lJDDin)))]
    if AAN1 is not None:
        pbaseB1red = pbaseB1[np.logical_not(np.in1d(pbaseB1, Kexclude, assume_unique=True))]
    if AAN2 is not None:
        pbaseB2red = pbaseB2[np.logical_not(np.in1d(pbaseB2, Kexclude, assume_unique=True))]

    return LP_formulation(DDred, pbaseDDred, dbaseDDred), pbaseB1red, pbaseB2red

