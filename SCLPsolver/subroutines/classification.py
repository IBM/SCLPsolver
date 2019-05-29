import numpy as np
from .calc_statecollide import calc_statecollide
from .collision_info import collision_info
from .time_collision_resolver import calc_timecollide, resolve_and_classify, reclassify
from .matlab_utils import find

#function [ cases, Delta, N1, N2, v1,v2, problem ] =

#'#@profile
def classification(solution, tolerance):
#idenitfy next collision and classify it
#problem
#   result = 0 Ok
#   result = 1 state prblem
#   result = 2 time problem
#   result = 3 state problem + time problem
#   result = 4 compound problem
#   result = 5 state problem + compound problem
#   result = 6 time problem + compound problem
#   result = 7 state problem + time problem + compound problem

    NN = solution.NN
    problem = {'result': 0, 'stateProblem': [], 'timeProblem': [], 'compoundProblem': {'result':0, 'data': []}}
    Delta = 0
    N1 = -1
    N2 = NN
    v1 = []
    v2 = []
    case = ''

    CC1, prob = calc_statecollide(solution.klist,solution.jlist, solution.state, tolerance)
    problem['stateProblem'] = prob

    if solution.last_collision is None:
        lastN1 = 0
        lastN2 = 0
    else:
        lastN1 = solution.last_collision.N1
        lastN2 = solution.last_collision.N2 + solution.last_collision.Nnew
    CC2, prob = calc_timecollide(solution.state.tau, solution.state.dtau, lastN1, lastN2, tolerance)
    problem['timeProblem'] = prob

    if 	len(CC1) == 0 and len(CC2) == 0:
        if problem['stateProblem']['result']==0 and problem['timeProblem']['result'] == 0:
            case = 'complete'
            Delta = np.inf
            return collision_info(case, Delta, N1, N2, v1, v2), problem
        else:
            return collision_info('', Delta, N1, N2, v1, v2), problem

    Didle = 0
    if	len(CC1) > 0 and len(CC2) > 0:
        Didle = CC1[0] - CC2[0]
        if abs(Didle) <= tolerance:
            Didle = 0
    if	(len(CC1) > 0 and len(CC2) == 0) or Didle < 0:
        if problem['stateProblem']['result'] >1:
            problem['result'] = 1
            return collision_info('', Delta, N1, N2, v1, v2), problem
        case = 'Case iii'
        Delta = CC1[0]
        N1 = CC1[1]
        N2 = CC1[1] + 1
        if CC1[2] < 0:
            v1 = CC1[2]
        else:
            v2 = CC1[2]
        col_info = collision_info(case, Delta, N1, N2, v1, v2)
        if problem['stateProblem']['result'] > 0:
            col_info.had_resolution = True
        if abs(Didle) <= 1000 * tolerance:
            if problem['timeProblem']['result'] == 0 and len(CC2) >1:
                result, prob1 = resolve_and_classify(CC2[0], CC2[1], solution, 1, tolerance)
                if prob1['result'] == 0:
                    col_info.alternative = result
        return col_info, problem
    elif (len(CC1) == 0 and len(CC2) > 0) or Didle >= 0:
        if problem['timeProblem']['result'] != 0:
            problem['result'] = problem['result'] + 2
            if problem['timeProblem']['result'] == 2:
                tol2 = 10 * tolerance
                inegDTAU = solution.state.dtau < -tol2
                izerTAU = np.fabs(solution.state.tau) <= tol2
                solution.store_ztau_ind(find(np.logical_and(izerTAU, inegDTAU)))
            return collision_info('', Delta, N1, N2, v1, v2), problem
        if CC2[0] == 0:
            N1 = CC2[1][0] - 1
            N2 = CC2[1][1] + 1
            return collision_info('Case i__', 0, N1, N2, [], [], None, 1), problem
        else:
            result, prob1 = resolve_and_classify(CC2[0], CC2[1], solution, 1, tolerance)
            tol2 = 10 * tolerance
            inegDTAU = solution.state.dtau < -tol2
            izerTAU = np.fabs(solution.state.tau) <= tol2
            solution.store_ztau_ind(find(np.logical_and(izerTAU, inegDTAU)))
            problem['timeProblem'] = prob1
            if prob1['result'] != 0:
                problem['result'] = 2
                return collision_info('', Delta, N1, N2, v1, v2), problem
            else:
                result.had_resolution = result.had_resolution or prob['had_resolution']
                if Didle == 0 and len(CC1) >1:
                    if not (result.N1 <= CC1[1] and CC1[1] <= result.N2):
                        print('time shrink as well as state hits zero elsewhere...')
                        result, resolved = reclassify(result, solution, tolerance, CC1[1])
                        if not resolved:
                            print('time shrink as well as state hits zero elsewhere...\n')
                            problem['result'] = problem['result'] + 4
                            problem['compoundProblem']['result'] = 1
                            return collision_info('', Delta, N1, N2, v1, v2), problem
                return result, problem
    problem['result'] = 8
    return None, problem
