import numpy as np
from .matlab_utils import find


def prepare_subproblem_basis(DD, pbaseDD, dbaseDD, Kset_0, Jset_N, v1, v2, AAN1, AAN2):

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
    else:
        pbaseB1red = []
    if AAN2 is not None:
        pbaseB2red = pbaseB2[np.logical_not(np.in1d(pbaseB2, Kexclude, assume_unique=True))]
    else:
        pbaseB2red = []

    return DDred, pbaseDDred, dbaseDDred, pbaseB1red, pbaseB2red


def prepare_subproblem_boundaries(DD, pbaseDD, dbaseDD, jlist, klist, lj, lk, v1, v2, AAN1, AAN2):
    x_0 = np.zeros((lk, 1))
    q_N = np.zeros((lj, 1))
    del_x_0 = np.zeros((lk, 1))
    del_q_N = np.zeros((lj, 1))
    # Boundary values for one sided subproblem, collision at t=0
    if AAN1 is None:
        # The case of v1 > 0, collision case iv_a
        if not isinstance(v1, list) and v1 > 0:
            dx_DD_v1 = DD[1:, 0][pbaseDD == v1][0]
            lk1 = klist == v1
            x_0[lk1] = -dx_DD_v1
            del_x_0[lk1] = dx_DD_v1
        # The case of v1 < 0, collision case iii_a
        if not isinstance(v1, list) and v1 < 0:
            dq_B2_v1 = AAN2['A'][0, 1:][AAN2['dual_name'] == v1][0]
            lj1 = jlist == -v1
            del_q_N[lj1] = -dq_B2_v1
    #
    #
    # Boundary values for one sided subproblem, collision at t=T
    elif AAN2 is None:
        # The case of v2 > 0, collision case iii_b
        if not isinstance(v2, list) and v2 > 0:
            dx_B1_v2 = AAN1['A'][1:, 0][AAN1['prim_name'] == v2][0]
            lk2 = klist == v2
            del_x_0[lk2] = -dx_B1_v2
        # The case of v2 < 0, collision case iv_b
        if not isinstance(v2, list) and v2 < 0:
            dq_DD_v2 = DD[0, 1:][dbaseDD == v2][0]
            lj2 = jlist == -v2
            q_N[lj2] = -dq_DD_v2
            del_q_N[lj2] = dq_DD_v2
    #
    #
    # Boundary values for two sided subproblem, collision at 0<t<T
    #  setting boundaries for the second exiting variable v1
    else:
        if not isinstance(v1, list) and v1 > 0:
            dx_DD_v1 = DD[1:, 0][pbaseDD == v1][0]
            lk1 = klist == v1
            x_0[lk1] = -dx_DD_v1
            dx_B1_v1 = AAN1['A'][1:, 0][AAN1['prim_name'] == v1][0]
            del_x_0[lk1] = -0.5 * dx_B1_v1 + dx_DD_v1
        if not isinstance(v1, list) and v1 < 0:
            dq_B2_v1 = AAN2['A'][0, 1:][AAN2['dual_name'] == v1][0]
            lj1 = jlist == -v1
            del_q_N[lj1] = -0.5 * dq_B2_v1
        #  setting boundaries for the first exiting variable v2
        if not isinstance(v2, list) and v2 > 0:
            dx_B1_v2 = AAN1['A'][1:, 0][AAN1['prim_name'] == v2][0]
            lk2 = klist == v2
            del_x_0[lk2] = -0.5 * dx_B1_v2
        if not isinstance(v2, list) and v2 < 0:
            dq_DD_v2 = DD[0, 1:][dbaseDD == v2][0]
            lj2 = jlist == -v2
            q_N[lj2] = -dq_DD_v2
            dq_B2_v2 = AAN2['A'][0, 1:][AAN2['dual_name'] == v2][0]
            del_q_N[lj2] = -0.5 * dq_B2_v2 + dq_DD_v2
    return del_q_N, del_x_0, q_N, x_0
