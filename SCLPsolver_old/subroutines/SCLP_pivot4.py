import numpy as np
from .matlab_utils import find
from .calc_dict import calc_dict
from .LP_formulate import LP_formulate
from .extract_rates import extract_rates
from .SCLP_subproblem4 import SCLP_subproblem
from .utils import  relative_to_project


def insertMatrix(base_sequence, newDict, newPlace):
    if newPlace not in base_sequence['places']:
        base_sequence['places'].append(newPlace)
        base_sequence['bases'].append(newDict)
    return base_sequence


#function [pn_new ,dn_new ,pivots_new, MatrixAA_new] =
def SCLP_pivot(Kset_0, Jset_N, prim_name, dual_name, N1, N2, v1, v2, pivots, base_sequence, KK, JJ, NN, totalK, totalJ,
               DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    if N1 == -1:
        pbaseB1 = np.array([])
        newDict, newPlace = calc_dict(base_sequence, N1, N2, pivots)
        base_sequence = insertMatrix(base_sequence, newDict, newPlace)
        AAN1 = None
        AAN2 = newDict
        BB2 = newDict['A'].copy()
        pbaseB2 = newDict['prim_name']
        dbaseB2 = newDict['dual_name']
        Jset = -dbaseB2[dbaseB2 < 0]
        Kset = Kset_0
        if  not isinstance(v1, list):
            Jset = Jset[Jset!=-v1]
            if v1 > 0:
                Kset = np.append(Kset, v1)
        else:
            print('v1',v1)
        # np.savetxt(relative_to_project('tests/subproblem/BB2.csv'), BB2)
        # np.savetxt(relative_to_project('tests/subproblem/pbaseB2.csv'), pbaseB2)
        # np.savetxt(relative_to_project('tests/subproblem/dbaseB2.csv'), dbaseB2)
        # np.savetxt(relative_to_project('tests/subproblem/Kset.csv'), Kset)
        # np.savetxt(relative_to_project('tests/subproblem/Jset.csv'), Jset)
        pbaseDD, dbaseDD, DD = LP_formulate(BB2, pbaseB2, dbaseB2, Kset, Jset, tolerance)
        if np.size(np.setdiff1d(pbaseDD, pbaseB2, assume_unique=True)) == 0 and \
                np.size(np.setdiff1d(dbaseDD, dbaseB2, assume_unique=True)) == 0:
            print('Basis B2 is optimal')
            return prim_name, dual_name, pivots, base_sequence, STEPCOUNT, ITERATION
    elif N2 == NN:
        pbaseB2 = np.array([])
        newDict, newPlace = calc_dict(base_sequence, N1, N2, pivots)
        AAN1 = newDict
        base_sequence = insertMatrix(base_sequence, newDict, newPlace)
        AAN2 = None
        BB1 = newDict['A'].copy()
        pbaseB1 = newDict['prim_name']
        dbaseB1 = newDict['dual_name']
        dbaseB2 = np.array([])
        Kset = pbaseB1[pbaseB1 > 0]
        Jset = Jset_N
        if not isinstance(v2, list):
            Kset = Kset[Kset!=v2]
            if v2 < 0:
                Jset = np.append(Jset, -v2)
        else:
            print('v2', v2)
        pbaseDD, dbaseDD, DD = LP_formulate(BB1, pbaseB1, dbaseB1, Kset, Jset, tolerance)
        if np.size(np.setdiff1d(pbaseB1, pbaseDD, assume_unique=True)) == 0 and \
                np.size(np.setdiff1d(dbaseB1, dbaseDD, assume_unique=True)) == 0:
            print('Basis B1 is optimal')
            return prim_name, dual_name, pivots, base_sequence, STEPCOUNT, ITERATION
    else:
        # BB1 = AA(:,:,N1)
        # BB2 = AA(:,:,N2)
        N1Dict, N1Place = calc_dict(base_sequence, N1, N1, pivots)
        AAN1 = N1Dict
        # MatrixAA = insertMatrix( MatrixAA, newDict, newPlace )
        N2Dict, N2Place = calc_dict(base_sequence, N2, N2, pivots)
        AAN2 = N2Dict
        # MatrixAA = insertMatrix( MatrixAA, newDict1, newPlace1 )
        BB2 = N2Dict['A'].copy()
        pbaseB1 = N1Dict['prim_name']
        dbaseB1 = N1Dict['dual_name']
        pbaseB2 = N2Dict['prim_name']
        dbaseB2 = N2Dict['dual_name']

        if isinstance(v1, list) or isinstance(v2, list):
            vv =np.setdiff1d(pbaseB1, pbaseB2, assume_unique=True)
            if isinstance(v2, list):
                v2 = vv
            else:
                v1 = vv
        Kset = pbaseB1[pbaseB1 > 0]
        Kset = Kset[Kset != v2]
        Jset = -dbaseB2[dbaseB2 < 0]
        Jset = Jset[Jset != -v1]
        pbaseDD, dbaseDD, DD = LP_formulate(BB2, pbaseB2, dbaseB2, Kset, Jset, tolerance)

    objective = DD[0, 0]

    if objective == np.inf or objective == -np.inf:
        if N1 == -1:
            print('***  beyond this primal problem is unbounded, dual is infeasible')
            cases = 'unbound_'
        elif N2 == NN:
            print('***  beyond this primal problem is infeasible, dual is unbounded')
            cases = 'infeas__'
        else:
            raise Exception('*** infeasibility in middle of base sequence')
        return prim_name, dual_name, pivots, base_sequence, STEPCOUNT, ITERATION

    i1 = 1
    i2 = 1
    if N1 >= 0:
        i1 = np.size(np.setdiff1d(pbaseB1, pbaseDD, assume_unique=True))
    if N2 < NN:
        i2 = np.size(np.setdiff1d(pbaseDD, pbaseB2, assume_unique=True))
    if i1 == 1 and i2 == 1:
        pn_new = np.vstack(pbaseDD)
        dn_new = np.vstack(dbaseDD)
        dx, dq = extract_rates(pbaseDD, dbaseDD, DD, KK, JJ, totalK, totalJ)
        sub_base_seq = {'dq': [dq], 'dx': [dx], 'bases': [DD], 'places': [0]}
    else:
        if N1 == -1:
            Kex1 =  np.intersect1d(pbaseDD[pbaseDD > 0], Kset_0, assume_unique=True)
            Kexclude =  np.intersect1d(Kex1, pbaseB2[pbaseB2 > 0], assume_unique=True)
            Jexclude = -np.intersect1d(dbaseDD[dbaseDD < 0], dbaseB2[dbaseB2 < 0], assume_unique=True)
        elif N2 == NN:
            Kexclude =  np.intersect1d(pbaseDD[pbaseDD > 0], pbaseB1[pbaseB1 > 0], assume_unique=True)
            Jex1 =  np.intersect1d(dbaseDD[dbaseDD < 0], [-v for v in Jset_N], assume_unique=True)
            Jexclude = -np.intersect1d(Jex1, dbaseB1[dbaseB1 < 0], assume_unique=True)
        else:
            Kexclude =  np.intersect1d(pbaseB1[pbaseB1 > 0], pbaseB2[pbaseB2 > 0], assume_unique=True)
            Jexclude = -np.intersect1d(dbaseB1[dbaseB1 < 0], dbaseB2[dbaseB2 < 0], assume_unique=True)
            if not isinstance(v1, list):
                Kexclude = Kexclude[Kexclude != v1]
                Jexclude = Jexclude[Jexclude != -v1]
            if not isinstance(v2, list):
                Kexclude = Kexclude[Kexclude != v2]
                Jexclude = Jexclude[Jexclude != -v2]
        pn_new, dn_new, sub_base_seq,\
        STEPCOUNT, ITERATION = SCLP_subproblem(pbaseDD, dbaseDD, DD, N1, N2, v1, v2, Kexclude, Jexclude, pbaseB1, pbaseB2,
                                                AAN1, AAN2, KK, JJ, NN, totalK, totalJ, DEPTH+1, STEPCOUNT, ITERATION, settings, tolerance)
    Nnew = len(sub_base_seq['dx'])
    NNold = NN
    pivots_new = pivots[0:N1 + 1]
    if N1 >= 0:
        if len(pivots_new) > N1:
            pivots_new[N1] = np.setdiff1d(prim_name[:, N1],  pn_new[:, 0], assume_unique=True).tolist() +\
                             np.setdiff1d(dual_name[:, N1], dn_new[:, 0], assume_unique=True).tolist()
        else:
            pivots_new.append(np.setdiff1d(prim_name[:, N1],  pn_new[:, 0], assume_unique=True).tolist()
                          + np.setdiff1d(dual_name[:, N1], dn_new[:, 0], assume_unique=True).tolist())
    for nn in range(Nnew - 1):
        pivots_new.append(np.setdiff1d(pn_new[:, nn], pn_new[:, nn+1], assume_unique=True).tolist()
                      + np.setdiff1d(dn_new[:, nn], dn_new[:, nn+1], assume_unique=True).tolist())
    if N2 < NNold:
        pivots_new.append(np.setdiff1d(pn_new[:, -1], prim_name[:, N2], assume_unique=True).tolist()
                      + np.setdiff1d(dn_new[:, -1], dual_name[:, N2], assume_unique=True).tolist())
        if len(pivots[N2:]) > 0:
            pivots_new+=(pivots[N2:])
    pn_new = np.hstack((prim_name[:, 0:N1+1],  pn_new,  prim_name[:, N2:]))
    dn_new = np.hstack((dual_name[:, 0:N1+1],  dn_new,  dual_name[:, N2:]))

    lplaces = np.logical_or(np.array(base_sequence['places']) <= N1, np.array(base_sequence['places']) >= N2)
    places = find(lplaces)
    #print(N1, N2, Nnew)
    if len(places) == 0:
        if AAN1 is not None:
            newPlace = [N1]
            newMat = [AAN1]
        else:
            newPlace = [N1 + Nnew + 1]
            newMat = [AAN2]
    else:
        newMat = [base_sequence['bases'][i] for i in places]
        newPlace = [base_sequence['places'][i] for i in places]
        newPlace = [v if v < N2 else v - (N2 - N1 - 1) + Nnew for v in newPlace]
    new_base_sequence = {'dx': base_sequence['dx'][0:N1+1] + sub_base_seq['dx'] + base_sequence['dx'][N2:],
                         'dq': base_sequence['dq'][0:N1+1] + sub_base_seq['dq'] + base_sequence['dq'][N2:],
                         'bases': newMat, 'places': newPlace}
    if N2 < NN and DEPTH == 0:
        new_base_sequence = insertMatrix(new_base_sequence, AAN2, N1+Nnew+1)
    # elif N1 == NN and DEPTH == 0:
    #     new_base_sequence = insertMatrix(new_base_sequence, AAN2, N1+1)
    if Nnew == 1 and DEPTH == 0:
        new_base_sequence = insertMatrix(new_base_sequence, {'prim_name': pbaseDD, 'dual_name': dbaseDD, 'A': DD}, N1+Nnew)
    return pn_new, dn_new, pivots_new, new_base_sequence, STEPCOUNT, ITERATION

