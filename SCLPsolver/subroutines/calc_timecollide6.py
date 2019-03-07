import numpy as np
from .matlab_utils import *


def calc_timecollide(TAU, DTAU, lastN1, lastN2, tolerance, tol_coeff):
# calculate time collisions, and performs tests
# problem    result = 0  Ok
#            result = 1  negative interval length       data = negative intervals
#            result = 2  zero length interval shrinks   data = zero intervals
#            result = 3  immediate collision            data = shrinking intervals
#            result = 4  multiple location shrinks      data = shrinking intervals
#            result = 5  zero interval does not expand  data = non-expanding interval

    problem = {'result': 0, 'data': []}

    tol2 = 10 * tolerance
    tol1 = tol2 * tol_coeff
    max_neg_coeff = 10000

    NN = len(TAU)
    iposTAU = TAU > tol2
    izerTAU = np.fabs(TAU) <= tol2
    inegTAU = TAU < -tol2
    d = 1

    while np.any(inegTAU):
        print('negative interval length...')
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
    if zflag:
        if np.sum(izerTAU) == NN - 1:
            locposTAU = find(iposTAU)[0]
            if locposTAU > 0 and locposTAU < NN - 1:
                if np.sum(DTAU[np.arange(0,locposTAU)]) < 0:
                    return [0, 1, locposTAU], problem
                elif np.sum(DTAU[np.arange(locposTAU + 1,NN)]) < 0:
                    return [0, locposTAU + 1, locposTAU], problem
        elif len(np.intersect1d(find(test1), np.arange(lastN1+1,lastN2, dtype=int), assume_unique=True)) == 0:
            print('zero length interval shrinks')
            tol_coeff = tol_coeff * 0.1
            while tol_coeff >= 0.001 and zflag:
                print('trying to resolve * ', tol_coeff, ' ...')
                iposTAU = TAU > tol2 * tol_coeff
                izerTAU = np.fabs(TAU) <= tol2 * tol_coeff
                test1 = np.logical_and(izerTAU, inegDTAU)
                zflag = np.any(test1)
                if zflag:
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
        if len(np.intersect1d(find(test1), np.arange(lastN1 + 1, lastN2, dtype=int), assume_unique=True)) == 0:
            print('zero length interval does not expand')
            tol_coeff = tol_coeff * 0.1
            while tol_coeff >= 0.001 and zflag:
                print('trying to resolve * ', tol_coeff, ' ...')
                iposTAU = TAU > tol2 * tol_coeff
                izerTAU = np.fabs(TAU) <= tol2 * tol_coeff
                test2 = np.logical_and(izerTAU, izerDTAU)
                zflag = np.any(test2)
                tol_coeff = tol_coeff * 0.1
            if zflag:
                print('zero length interval does not expand\n')
                problem['result'] = 5
                problem['data'] = find(test2)
                return [], problem
        else:
            problem['data'] = find(test2)
            problem['result'] = 5
            print('zero length interval does not expand\n')
            return [], problem

    test3 = np.logical_and(iposTAU, inegDTAU)
    if not np.any(test3):
        return [], problem

    rz = np.divide(-DTAU, TAU, where=test3, out=np.zeros_like(TAU))
    zz = np.max(rz)
    if abs(1 / zz) < tol2:
        if tol_coeff >= 1:
             tol_coeff = 0.1
        print('immediate collision ... resolving * ', tol_coeff)
        if abs(1 / zz) < tol2 * tol_coeff:
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
                problem['data'] = find(ishrink)
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
                    problem['data'] = find(ishrink)
                    return [], problem
            print('ok!\n')
            return[1 / zz, nn1, nn2], problem
        else:
            return [1 / zz, nn1, nn2], problem