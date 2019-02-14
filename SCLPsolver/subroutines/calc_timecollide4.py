import numpy as np
from .matlab_utils import *


def calc_timecollide(TAU, DTAU, tolerance, tol_coeff):
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
    max_neg_coeff = 100

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
    if np.any(test1):
        if np.sum(izerTAU) == NN - 1:
            locposTAU = find(iposTAU)[0]
            if locposTAU > 0 and locposTAU < NN - 1:
                if np.sum(DTAU[np.arange(0,locposTAU)]) < 0:
                    return [0, 1, locposTAU], problem
                elif np.sum(DTAU[np.arange(locposTAU + 1,NN)]) < 0:
                    return [0, locposTAU + 1, locposTAU], problem
        print('zero length interval shrinks\n ')
        problem['result'] = 2
        problem['data'] = find(test1)
        return [], problem

    test2 = np.logical_and(izerTAU, izerDTAU)
    if np.any(test2):
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
        print('immediate collision\n')
        problem['result'] = 3
        problem['data'] = find(rz == zz)
        return [], problem
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