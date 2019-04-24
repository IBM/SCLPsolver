import numpy as np
from .matlab_utils import *


def calc_timecollide(TAU, DTAU, pivots, lastN1, lastN2, last_case, tolerance, tol_coeff):
# calculate time collisions, and performs tests
# problem    result = 0  Ok
#            result = 1  negative interval length       data = negative intervals
#            result = 2  zero length interval shrinks   data = zero intervals
#            result = 3  immediate collision            data = shrinking intervals
#            result = 4  multiple location shrinks      data = shrinking intervals
#            result = 5  zero interval does not expand  data = non-expanding interval

    problem = {'result': 0, 'data': [], 'had_resolution': False, 'resolved_types':[]}

    tol2 = 10 * tolerance
    tol1 = tol2 * tol_coeff
    max_neg_coeff = 100000

    pflag = tol_coeff >1

    NN = len(TAU)
    iposTAU = TAU > tol2
    izerTAU = np.fabs(TAU) <= tol2
    inegTAU = TAU < -tol2
    d = 1

    while np.any(inegTAU):
        print('negative interval length...')
        problem['had_resolution'] = True
        problem['resolved_types'].append(1)
        d = d * 10
        if d > max_neg_coeff:
            print('fail!')
            problem['result'] = 1
            problem['data'] = find(inegTAU)
            return [], problem
        else:
            print('resolving * ', d)
            tol2 = 10 * tolerance * d
            iposTAU = TAU > tol2
            izerTAU = np.fabs(TAU) <= tol2
            inegTAU = TAU < -tol2


    #iposDTAU = DTAU > tolerance
    izerDTAU = np.fabs(DTAU) <= tol2
    inegDTAU = DTAU < -tol2

    test1 = np.logical_and(izerTAU, inegDTAU)
    zflag = np.any(test1)
    ztau_ind = np.asarray([])
    last_col_int= np.arange(lastN1+1,lastN2, dtype=int)
    if zflag:
        problem['had_resolution'] = True
        problem['resolved_types'].append(2)
        ztau_ind = find(test1)
        zmin = np.min(ztau_ind)
        zmax = np.max(ztau_ind)
        print('zero length interval shrinks:', ztau_ind, 'last N1:', lastN1, ' N2:', lastN2, 'case:', last_case)
        print('tau: ', TAU[zmin: zmax+1])
        print('dtau: ', DTAU[zmin: zmax + 1])
        ind1 = len(np.intersect1d(ztau_ind, last_col_int, assume_unique=True)) == 0
        ind2 = len(np.intersect1d(np.arange(zmin, zmax + 1, dtype=int),
                                  last_col_int, assume_unique=True)) != 0 and len(ztau_ind) / (zmax - zmin + 1) >= 0.79
        if np.sum(izerTAU) == NN - 1:
            locposTAU = find(iposTAU)[0]
            if locposTAU > 0 and locposTAU < NN - 1:
                if np.sum(DTAU[np.arange(0,locposTAU)]) < 0:
                    return [0, 1, locposTAU], problem
                elif np.sum(DTAU[np.arange(locposTAU + 1,NN)]) < 0:
                    return [0, locposTAU + 1, locposTAU], problem
        #elif ind1 and not (not ind2 and len(ztau_ind)/(zmax-zmin+1) >= 0.7):
        elif ind1:
            tol_coeff = 0.1
            while tol_coeff >= 0.0001 and zflag:
                print('trying to resolve * ', tol_coeff, ' ...')
                iposTAU = TAU > tol2 * tol_coeff
                izerTAU = TAU <= tol2 * tol_coeff
                test1 = np.logical_and(izerTAU, inegDTAU)
                zflag = np.any(test1)
                if zflag:
                    ztau_ind = find(test1)
                    print('zero length interval shrinks:', ztau_ind)
                    zmin = np.min(ztau_ind)
                    zmax = np.max(ztau_ind)
                    if np.sum(izerTAU) == NN - 1:
                        locposTAU = find(iposTAU)[0]
                        if locposTAU > 0 and locposTAU < NN - 1:
                            if np.sum(DTAU[np.arange(0, locposTAU)]) < 0:
                                return [0, 1, locposTAU], problem
                            elif np.sum(DTAU[np.arange(locposTAU + 1, NN)]) < 0:
                                return [0, locposTAU + 1, locposTAU], problem
                else:
                    break
                tol_coeff = tol_coeff * 0.1
            if zflag:
                if ind2:
                    print('trying to ignore... ')
                    iposTAU = TAU > 0
                    inegTAU = TAU < 0
                    test = np.logical_and(inegTAU, inegDTAU)
                    if np.any(test):
                        ishrink0 = find(test)
                        nn1 = np.min(ishrink0)
                        nn2 = np.max(ishrink0)
                        if len(ishrink0) < nn2 - nn1:
                            print('multiple negative intervals shrinks...')
                        else:
                            vlist = pivots.get_difference(nn1, nn2)
                            if len(vlist) <= 2:
                                return [tolerance, nn1, nn2], problem
                            else:
                                print('More than two variables leave in time shrink ....')
                        test3 = np.logical_and(iposTAU, inegDTAU)
                        if not np.any(test3):
                            print('no shrinking tau...')
                            problem['result'] = 8
                            return [], problem
                        rz = np.divide(-DTAU, TAU, where=test3, out=np.zeros_like(TAU))
                        zz_ind = np.argmax(rz)
                        zz = rz[zz_ind]
                        test = np.fabs(rz / zz - 1)
                        d = 1
                        while tol1 * d <= 0.01/tolerance:
                            ishrink = np.concatenate(find(test < tol1 * d), ishrink0)
                            nn1 = np.min(ishrink)
                            nn2 = np.max(ishrink)
                            if len(ishrink) < nn2 - nn1:
                                print('Multiple locations shrinks...')
                            else:
                                vlist = pivots.get_difference(nn1, nn2)
                                if len(vlist) <= 2:
                                    return [tolerance, nn1, nn2], problem
                                else:
                                    print('More than two variables leave in time shrink ....')
                            d = d * 10
                        problem['result'] = 7
                        problem['data'] = ishrink0
                        print('Failed to resolve!')
                        return [], problem
                    problem['result'] = 6
                else:
                    print('zero length interval shrinks\n ')
                    problem['result'] = 2
                    problem['data'] = find(test1)
                    return [], problem
        else:
            print('zero length interval shrinks\n ')
            problem['result'] = 2
            problem['data'] = find(test1)
            return [], problem

    test2 = np.logical_and(izerTAU, izerDTAU)
    zflag = np.any(test2)
    if zflag:
        problem['had_resolution'] = True
        problem['resolved_types'].append(5)
        if len(np.intersect1d(find(test1), np.arange(lastN1 + 1, lastN2, dtype=int), assume_unique=True)) == 0:
            print('zero length interval does not expand')
            tol_coeff = 0.1
            while tol_coeff >= 0.001 and zflag:
                print('trying to resolve * ', tol_coeff, ' ...')
                iposTAU = TAU > tol2 * tol_coeff
                izerTAU = np.fabs(TAU) <= tol2 * tol_coeff
                test2 = np.logical_and(izerTAU, izerDTAU)
                zflag = np.any(test2)
                tol_coeff = tol_coeff * 0.1
            if zflag:
                if last_case != 'Case ii_':
                    print('zero length interval does not expand... but rewind impossible')
                else:
                    print('zero length interval does not expand... trying to ignore')
                    # problem['result'] = 5
                    # problem['data'] = find(test2)
                    # return [], problem
        else:
            problem['data'] = find(test2)
            problem['result'] = 5
            print('zero length interval does not expand\n')
            return [], problem

    test3 = np.logical_and(iposTAU, inegDTAU)
    if not np.any(test3):
        return [], problem

    rz = np.divide(-DTAU, TAU, where=test3, out=np.zeros_like(TAU))
    zz_ind = np.argmax(rz)
    zz = rz[zz_ind]
    if abs(1 / zz) < tol2:
        zz_ztau_ind = np.intersect1d(ztau_ind, zz_ind, assume_unique=True)
        if len(zz_ztau_ind) > 0:
            print('immediate collision in zero length interval...', zz_ztau_ind)
            if last_case == 'Case ii_':
                problem['result'] = 6
                problem['data'] = zz_ztau_ind
                problem['had_resolution'] = True
                problem['resolved_types'].append(6)
                #return [], problem
        if tol_coeff >= 1:
            tol_coeff = 0.1
        print('immediate collision ... resolving * ', tol_coeff)
        if abs(1 / zz) < tol2 * tol_coeff:
            if problem['result'] == 6:
                print("trying to ignore...")
                test = np.fabs(rz / zz - 1)
                ishrink = find(test < tol1)
                nn1 = np.min(ishrink)
                nn2 = np.max(ishrink)
                if len(ishrink) < nn2 - nn1:
                    print('multiple location shrinks...')
                    problem['result'] = 4
                    problem['data'] = ishrink
                    return [], problem
                else:
                    return [1 / zz, nn1, nn2], problem
            else:
                problem['result'] = 3
                problem['data'] = find(rz == zz)
                return [], problem
        elif 1 / zz <= -tol2 * tol_coeff:
            return [], problem
        elif 1 / zz >= tol2 * tol_coeff:
            test = np.fabs(rz / zz - 1)
            ishrink = find(test < tol1)
            nn1 = np.min(ishrink)
            nn2 = np.max(ishrink)
            if len(ishrink) < nn2 - nn1:
                print('multiple location shrinks...')
                problem['result'] = 4
                problem['data'] = ishrink
                return [], problem
            else:
                return [1 / zz, nn1, nn2], problem
    elif 1 / zz <= -tol2:
        return [], problem
    elif 1 / zz >= tol2:
        test = np.fabs(rz/zz - 1)
        ishrink = find( test < tol1)
        nn1 = np.min(ishrink)
        nn2 = np.max(ishrink)
        if len(ishrink) < nn2 - nn1:
            problem['had_resolution'] = True
            problem['resolved_types'].append(4)
            print('multiple location shrinks\n')
            print('resolving * 0.1... ')
            ishrink = find(test < tol1/10)
            nn1 = np.min(ishrink)
            nn2 = np.max(ishrink)
            if len(ishrink) < nn2 - nn1:
                print('fail!\n ')
                print('resolving * 10... ')
                ishrink = find(test < tol1 * 10)
                nn1 = np.min(ishrink)
                nn2 = np.max(ishrink)
                if len(ishrink) < nn2 - nn1:
                    print('fail!\n ')
                    problem['result'] = 4
                    problem['data'] = ishrink
                    return [], problem
            print('ok!\n')
            print(ishrink)
            return[1 / zz, nn1, nn2], problem
        else:
            if pflag:
                print(ishrink)
            return [1 / zz, nn1, nn2], problem