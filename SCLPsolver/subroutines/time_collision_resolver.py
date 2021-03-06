# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from .calc_order_ratio import calc_order_ratio
from .collision_info import collision_info
from .matlab_utils import find
from .equation_tools.eq_tools import get_time_ratio
import math


def get_shrinking_intervals(delta, rz, inegDTAU, tol1, tol2, tol_coeff, tol_coeff2, tolerance, shrinking_ind = None):
    if abs(delta) < tol2 * tol_coeff2:
        if delta <= 0:
            print("Negative delta:", delta)
        tol_coeff2 = 0.1
        resolved = False
        while tol_coeff2 >= 0.001 and tol_coeff <= 0.01 / tolerance:
            print('immediate collision ... resolving * ', tol_coeff2, 'delta:', delta)
            if abs(delta) < tol2 * tol_coeff2:
                print('... fail!')
                tol_coeff2 = tol_coeff2 * 0.1
                continue
            elif delta <= -tol2 * tol_coeff2:
                problem = 1
                return None, problem, tol_coeff, True
            elif delta >= tol2 * tol_coeff2:
                test = np.fabs(rz * delta - 1)
                ind1 = np.logical_and(test < tol1 * tol_coeff, inegDTAU)
                if shrinking_ind is not None:
                    ind1 = np.logical_or(ind1,shrinking_ind)
                ishrink = find(ind1)
                nn1 = np.min(ishrink)
                nn2 = np.max(ishrink)
                if len(ishrink) < nn2 - nn1:
                    if tol_coeff <= 0.01 / tolerance:
                        print('multiple location shrinks...', ishrink)
                        tol_coeff = 10 * tol_coeff
                        continue
                    else:
                        break
                else:
                    problem = 0
                    return [nn1, nn2], problem, tol_coeff, True
        if not resolved:
            ct = 0.1
            while ct >= tol_coeff2:
                test = rz * delta - 1
                ishrink = find(np.logical_and(test < tol1 * tol_coeff/ct, inegDTAU))
                nn1 = np.min(ishrink)
                nn2 = np.max(ishrink)
                if len(ishrink) < nn2 - nn1:
                    print('multiple location shrinks!...', ishrink)
                    ct = 0.1 * ct
                    continue
                else:
                    problem = 0
                    return [nn1, nn2], problem, tol_coeff, True
            problem = 3
            return None, problem, tol_coeff, True
    elif delta <= -tol2 * tol_coeff2:
        problem = 4
        return None, problem, tol_coeff, True
    elif delta >= tol2 * tol_coeff2:
        test = np.fabs(rz * delta - 1)
        ind1 = np.logical_and(test < tol1 * tol_coeff, inegDTAU)
        if shrinking_ind is not None:
            ind1 = np.logical_or(ind1, shrinking_ind)
        ishrink = find(ind1)
        if (ishrink.shape[0] == 0):
            print('here!')
        nn1 = np.min(ishrink)
        nn2 = np.max(ishrink)
        if len(ishrink) < nn2 - nn1:
            print('multiple location shrinks...', ishrink)
            tol_coeff = 10 * tol_coeff
            problem = -1
            return None, problem, tol_coeff, True
        else:
            problem = 0
            return [nn1, nn2], problem, tol_coeff, False

def resolve_and_classify(delta, rz, solution, param_line, tol_coeff0, tolerance, shrinking_ind = None):
    problem = {'result': 0}
    tol2 = 10 * tolerance
    tol1 = tol2
    tol_coeff = tol_coeff0
    tol_coeff2 = 1
    had_resolution = False
    inegDTAU = solution.state.dtau < -tol2
    while tol_coeff <= 0.01/tolerance:
        if tol_coeff > 1:
            print('trying to resolve * ',tol_coeff)
        intervals, prob, tol_coeff, res = get_shrinking_intervals(delta, rz, inegDTAU, tol1, tol2, tol_coeff, tol_coeff2, tolerance, shrinking_ind)
        if prob > 0:
            problem['result'] = prob
            return None, problem
        else:
            had_resolution = had_resolution or res
            if prob == 0:
                N1 = intervals[0] - 1
                N2 = intervals[1] + 1
            if prob == -1:
                continue
        if N1 == -1 and N2 == solution.NN:
            problem['result'] = 5
            print('Max tolerance coefficient reached ....')
            return None, problem
        col_info = classify_time_collision(delta, rz, tol_coeff, N1, N2, solution, param_line, tolerance)
        if col_info is None:
            had_resolution = True
        else:
            col_info.had_resolution = had_resolution
            return col_info, problem
        tol_coeff = 10 * tol_coeff
    problem['result'] = 5
    return None, problem

def reclassify(col_info, solution, param_line, tolerance, stateN=None):
    if col_info.from_ztau:
        res = solution.pivots.find_N1_N2_around(col_info.ztau_ind, col_info.N1-1)
        if res is not None:
            col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                          solution, param_line, tolerance)
            if col is not None:
                if col != col_info:
                    col.from_ztau = True
                    col.ztau_ind = col_info.ztau_ind
                    return col, True
        res = solution.pivots.find_N1_N2_around(col_info.ztau_ind, col_info.N1, col_info.N2 + 1)
        if res is not None:
            col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                          solution, param_line, tolerance)
            if col is not None:
                if col != col_info:
                    col.from_ztau = True
                    col.ztau_ind = col_info.ztau_ind
                    return col, True
        else:
            if col_info.alternative is not None:
                return col_info.alternative, True
        return col_info, False
    else:
        tol_coeff = col_info.tol_coeff * 10
        resolved = False
        if col_info.case == 'Case iii':
            if col_info.alternative is not None:
                stateN = col_info.N1
                col_info = col_info.alternative
                new_col_info, problem = resolve_and_classify(col_info.delta, col_info.rz, solution, param_line, tol_coeff, tolerance)
                if problem['result'] > 0:
                    return col_info, False
                elif new_col_info.N1 <= stateN and stateN <= new_col_info.N2:
                    resolved = True
                    return new_col_info, resolved
                else:
                    col_info = new_col_info
            else:
                return col_info, resolved
        while tol_coeff <= 0.01/tolerance:
            new_col_info, problem = resolve_and_classify(col_info.delta, col_info.rz, solution, param_line, tol_coeff, tolerance)
            tol_coeff = tol_coeff * 10
            if problem['result'] > 0:
                break
            if new_col_info != col_info:
                col_info = new_col_info
                if stateN is None:
                    resolved = True
                    break
                elif col_info.N1 <= stateN and stateN <= col_info.N2:
                    resolved = True
                    break
        if not resolved:
            if col_info.alternative is not None:
                return col_info.alternative, True
        return col_info, resolved

def reclassify_ztau(col_info, solution, param_line, ztau_ind, tolerance, hard_find=False):
    if len(ztau_ind) >= 3:
        if ztau_ind[1] - ztau_ind[0] > 2:
            if  ztau_ind[-1] - ztau_ind[-2] > 2:
                res = solution.pivots.find_N1_N2_around(ztau_ind[1:-1])
                if res is not None:
                    col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                                  solution, param_line, tolerance)
                    if col is not None:
                        col.from_ztau = True
                        col.ztau_ind = ztau_ind
                        return col
            res = solution.pivots.find_N1_N2_around(ztau_ind[1:])
            if res is not None:
                col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                              solution, param_line, tolerance)
                if col is not None:
                    col.from_ztau = True
                    col.ztau_ind = ztau_ind
                    return col
        elif ztau_ind[-1] - ztau_ind[-2] > 2:
            res = solution.pivots.find_N1_N2_around(ztau_ind[:-1])
            if res is not None:
                col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                              solution, param_line, tolerance)
                if col is not None:
                    col.from_ztau = True
                    col.ztau_ind = ztau_ind
                    return col
    if (len(ztau_ind) > 3 and (max(ztau_ind) - min(ztau_ind) + 1)/len(ztau_ind) > 0.9) or hard_find:
        for n in range(len(ztau_ind)):
            res = solution.pivots.find_N1_N2_around(ztau_ind[n:])
            if res is not None:
                col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                              solution, param_line, tolerance)
                if col is not None:
                    col.from_ztau = True
                    col.ztau_ind = ztau_ind[n:]
                    return col
        for n in range(1, len(ztau_ind)-1):
            res = solution.pivots.find_N1_N2_around(ztau_ind[:-n])
            if res is not None:
                col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, res[0], res[1],
                                              solution, param_line, tolerance)
                if col is not None:
                    col.from_ztau = True
                    col.ztau_ind = ztau_ind[:-n]
                    return col
    return None

def classify_time_collision(delta, rz, tol_coeff, N1, N2, solution, param_line, tolerance):
    if N1 == -1 or N2 == solution.NN:
        return collision_info('Case i__', delta, N1, N2, [], [], rz, tol_coeff)
    else:
        vlist = solution.pivots.get_out_difference(N1, N2)
        if len(vlist) > 2:
            print('More than two variables leave in time shrink ....')
            return None
        elif len(vlist) == 1:
            return collision_info('Case i__', delta, N1, N2, [], [], rz, tol_coeff)
        elif len(vlist) == 2:
            case = 'Case ii_'
            if N2 - N1 == 2:
                return collision_info(case, delta, N1, N2, solution.pivots.outpivots[N1], solution.pivots.outpivots[N1+1], rz, tol_coeff)
            else:
                order_ratio, correct = calc_order_ratio(vlist[0], vlist[1], N1, N2, solution, param_line, delta / 2)
                if abs(abs(order_ratio) - 1) < tolerance:
                    print('Tolerance in R unclear...')
                if abs(order_ratio) < 1:
                    v1 = vlist[0]
                    v2 = vlist[1]
                else:
                    v1 = vlist[1]
                    v2 = vlist[0]
                if correct:
                    return collision_info(case, delta, N1, N2, v1, v2, rz, tol_coeff)
                else:
                    return None

def calc_timecollide(TAU, DTAU, lastN1, lastN2, tolerance):

    problem = {'result': 0, 'data': [], 'had_resolution': False, 'resolved_types':[]}

    tol2 = 10 * tolerance
    max_neg_coeff = 100000
    tol_coeff = 1

    min_tau = np.min(TAU)
    if min_tau < -tol2:
        print('negative interval length...', min_tau)
        problem['had_resolution'] = True
        tol2 = 10**math.ceil(math.log10(-min_tau))
        if tol2 > tolerance * max_neg_coeff:
            print('fail!')
            problem['result'] = 1
            problem['data'] = find(min_tau)
            return [0], problem
        print('resolved!')
    # while np.any(inegTAU):
    #     print('negative interval length...', np.min(TAU))
    #     problem['had_resolution'] = True
    #     problem['resolved_types'].append(1)
    #     d = d * 10
    #     if d > max_neg_coeff:
    #         print('fail!')
    #         problem['result'] = 1
    #         problem['data'] = find(inegTAU)
    #         return [0], problem
    #     else:
    #         print('resolving * ', d)
    #         tol2 = 10 * tolerance * d
    #         iposTAU = TAU > tol2
    #         izerTAU = np.fabs(TAU) <= tol2
    #         inegTAU = TAU < -tol2

    NN = TAU.shape[0]
    iposTAU = TAU > tol2
    izerTAU = np.fabs(TAU) <= tol2
    inegTAU = TAU < -tol2
    #iposDTAU = DTAU > tolerance
    izerDTAU = np.fabs(DTAU) <= tol2
    inegDTAU = DTAU < -tol2

    # TODO: take this to cython
    test1 = np.logical_and(izerTAU, inegDTAU)
    zflag = np.any(test1)
    if zflag:
        problem['had_resolution'] = True
        problem['resolved_types'].append(2)
        ztau_ind = find(test1)
        print('zero length interval shrinks:', ztau_ind, 'last N1:', lastN1, ' N2:', lastN2)
        last_col_int = np.arange(lastN1 + 1, lastN2, dtype=int)
        ind1 = len(np.intersect1d(ztau_ind, last_col_int, assume_unique=True)) == 0
        # zmin = np.min(ztau_ind)
        # zmax = np.max(ztau_ind)
        # ztau_int= np.arange(zmin,zmax+1, dtype=int)
        # ind2 = len(np.intersect1d(last_col_int, ztau_int , assume_unique=True)) != 0
        # ind3 = (len(ztau_ind) + lastN2 - lastN1 - 1)/(zmax - zmin + 1) >= 1
        if np.sum(izerTAU) == NN - 1:
            locposTAU = find(iposTAU)[0]
            if locposTAU > 0 and locposTAU < NN - 1:
                if np.sum(DTAU[np.arange(0,locposTAU)]) < 0:
                    return [0, [0, locposTAU-1]], problem
                elif np.sum(DTAU[np.arange(locposTAU + 1,NN)]) < 0:
                    return [0, [locposTAU + 1, NN-1]], problem
        elif ind1:
            # if last_case == 'rewind':
            #     zmin = np.min(ztau_ind)
            #     zmax = np.max(ztau_ind)
            #     if len(ztau_ind) / (zmax - zmin + 1) >= 0.75 and len(ztau_ind) > 3:
            #         if np.all(izerTAU[zmin: zmax+1]):
            #             print('trying to remove zero intervals...')
            #             rz = np.divide(-DTAU, TAU, where=inegDTAU, out=np.zeros_like(TAU))
            #             zz_ind = np.argmax(rz)
            #             zz = rz[zz_ind]
            #             return [1 / zz, zmin, zmax], problem
            tol_coeff = 0.1
            while tol_coeff >= 0.001 and zflag:
                print('trying to resolve * ', tol_coeff, ' ...')
                iposTAU = TAU > tol2 * tol_coeff
                inegTAU = TAU < tol2 * tol_coeff
                izerTAU = np.fabs(TAU) <= tol2 * tol_coeff
                test1 = np.logical_and(izerTAU, inegDTAU)
                zflag = np.any(test1)
                if zflag:
                    if np.sum(izerTAU) == NN - 1:
                        locposTAU = find(iposTAU)[0]
                        if locposTAU > 0 and locposTAU < NN - 1:
                            if np.sum(DTAU[np.arange(0, locposTAU)]) < 0:
                                return [0, [0, locposTAU-1]], problem
                            elif np.sum(DTAU[np.arange(locposTAU + 1, NN)]) < 0:
                                return [0, [locposTAU + 1, NN-1]], problem
                else:
                    break
                tol_coeff = tol_coeff * 0.1
            if zflag:
                if lastN1 !=0 or lastN2 !=0:
                    print('zero length interval shrinks\n ')
                    problem['result'] = 2
                    problem['data'] = find(test1)
                    return [0], problem
                else:
                    delta, rz = get_time_ratio(TAU, DTAU, inegTAU, inegDTAU, tol2 * tol_coeff)
                    if delta < 0:
                        return [], problem
                    else:
                        return [delta, rz], problem
                    # test3 = inegDTAU
                    # if not np.any(test3):
                    #     return [], problem
                    # xTAU = TAU.copy()
                    # xTAU[inegTAU] = tol2 * tol_coeff
                    # rz = np.divide(-DTAU, xTAU, where=test3, out=np.zeros_like(TAU))
                    # zz_ind = np.argmax(rz)
                    # zz = rz[zz_ind]
                    # rz[ztau_ind] = zz
                    # return [1 / zz, rz], problem
        else:
            print('zero length interval shrinks\n ')
            problem['result'] = 2
            problem['data'] = find(test1)
            return [0], problem

    # TODO: take this to cython
    test2 = np.logical_and(izerTAU, izerDTAU)
    zflag = np.any(test2)
    if zflag:
        problem['had_resolution'] = True
        problem['resolved_types'].append(5)
        #this should be test2 - othervise this true
        if len(np.intersect1d(find(test1), np.arange(lastN1 + 1, lastN2, dtype=int), assume_unique=True)) == 0:
            print('zero length interval does not expand')
            tol_coeff = 0.1
            while tol_coeff >= 0.001 and zflag:
                print('trying to resolve * ', tol_coeff, ' ...')
                inegTAU = TAU < tol2 * tol_coeff
                iposTAU = TAU > tol2 * tol_coeff
                izerTAU = np.fabs(TAU) <= tol2 * tol_coeff
                test2 = np.logical_and(izerTAU, izerDTAU)
                zflag = np.any(test2)
                tol_coeff = tol_coeff * 0.1
            if zflag:
                print('zero length interval does not expand... trying to ignore')
                    # problem['result'] = 5
                    # problem['data'] = find(test2)
                    # return [], problem
        else:
            problem['data'] = find(test2)
            problem['result'] = 5
            print('zero length interval does not expand\n')
            #TODO: here is the source of potential bug!!!
            return [0], problem

    delta, rz = get_time_ratio(TAU, DTAU, inegTAU, inegDTAU, tol2 * tol_coeff)
    if delta < 0:
        return [], problem
    else:
        return [delta, rz], problem
    # #test3 = np.logical_and(iposTAU, inegDTAU)
    # #inegDTAU = DTAU < -tol2 * tol_coeff
    # test3 = inegDTAU
    # if not np.any(test3):
    #     return [], problem
    #
    # xTAU = TAU.copy()
    # xTAU[inegTAU] = tol2 * tol_coeff
    # rz = np.divide(-DTAU, xTAU, where=test3, out=np.zeros_like(TAU))
    # zz_ind = np.argmax(rz)
    # zz = rz[zz_ind]
    # return [1/zz, rz], problem