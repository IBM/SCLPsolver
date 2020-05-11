import numpy as np
from .state_tools.calc_statecollide import calc_statecollide
from .collision_info import collision_info
from .time_collision_resolver import calc_timecollide, resolve_and_classify, reclassify
from .matlab_utils import find


#'#@profile
def classification(solution, param_line, tolerance, time_only=False):
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

    #CC1, prob = calc_statecollide(solution.klist,solution.jlist, solution.state,  tolerance)
    if not time_only:
        CC1, prob = calc_statecollide(solution.klist,solution.jlist, solution.state, solution.get_raw_dx(),
                                      solution.get_raw_dq(), param_line, solution.loc_min_storage, solution.partial_states, tolerance)
        #
        problem['stateProblem'] = prob
    else:
        CC1 =[]

    if solution.last_collision is None:
        lastN1 = 0
        lastN2 = 0
    else:
        lastN1 = solution.last_collision.N1
        lastN2 = solution.last_collision.N2 + solution.last_collision.Nnew
    CC2, prob = calc_timecollide(solution.state.tau, solution.state.dtau, lastN1, lastN2, tolerance)
    problem['timeProblem'] = prob

    if 	len(CC1) == 0 and len(CC2) == 0:
        if problem['stateProblem']['result'] == 0 and problem['timeProblem']['result'] == 0:
            case = 'complete'
            Delta = np.inf
            return collision_info(case, Delta, N1, N2, v1, v2), problem
        else:
            return collision_info('', Delta, N1, N2, v1, v2), problem

    Didle = 0
    if	len(CC1) > 0 and len(CC2) > 0:
        Didle = CC1[0] - CC2[0]
        if abs(Didle) <= tolerance and abs(Didle) < CC1[0] and abs(Didle) < CC2[0]:
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
                col_info1, prob1 = resolve_and_classify(CC2[0], CC2[1], solution, param_line, 1, tolerance)
                if prob1['result'] == 0:
                    col_info.alternative = col_info1
                    col_info.alternative.had_resolution = True
        return col_info, problem
    elif (len(CC1) == 0 and len(CC2) > 0) or Didle >= 0:
        if problem['timeProblem']['result'] != 0:
            problem['result'] = problem['result'] + 2
            if problem['timeProblem']['result'] == 2:
                tol2 = 10 * tolerance
                inegDTAU = solution.state.dtau < -tol2
                izerTAU = np.fabs(solution.state.tau) <= tol2
                solution.store_ztau_ind(find(np.logical_and(izerTAU, inegDTAU)))
            col_info = collision_info('', Delta, N1, N2, v1, v2)
        else:
            if CC2[0] == 0:
                N1 = CC2[1][0] - 1
                N2 = CC2[1][1] + 1
                col_info = collision_info('Case i__', 0, N1, N2, [], [], None, 1)
            else:
                col_info, prob1 = resolve_and_classify(CC2[0], CC2[1], solution, param_line, 1, tolerance)
                tol2 = 10 * tolerance
                inegDTAU = solution.state.dtau < -tol2
                izerTAU = np.fabs(solution.state.tau) <= tol2
                solution.store_ztau_ind(find(np.logical_and(izerTAU, inegDTAU)))
                problem['timeProblem'] = prob1
                if prob1['result'] != 0:
                    problem['result'] = 2
                    col_info = collision_info('', Delta, N1, N2, v1, v2)
                else:
                    col_info.had_resolution = col_info.had_resolution or prob['had_resolution']
                    if Didle == 0 and len(CC1) >1:
                        if not (col_info.N1 <= CC1[1] and CC1[1] <= col_info.N2):
                            print('time shrink as well as state hits zero elsewhere...')
                            col_info, resolved = reclassify(col_info, solution, tolerance, CC1[1])
                            # if not resolved:
                            #     print('time shrink as well as state hits zero elsewhere...\n')
                            #     problem['result'] = problem['result'] + 4
                            #     problem['compoundProblem']['result'] = 1
                            #     col_info = collision_info('', Delta, N1, N2, v1, v2)
        if abs(Didle) <= 1000 * tolerance:
            if len(CC1) > 1:
                if col_info.case != '':
                    col_info.alternative = collision_info('Case iii', CC1[0], CC1[1], CC1[1] + 1,
                                                      *((CC1[2], None) if CC1[2] < 0 else (None, CC1[2])))
                    col_info.alternative.had_resolution = True
                else:
                    col_info = collision_info('Case iii', CC1[0], CC1[1], CC1[1] + 1,
                                                      *((CC1[2], None) if CC1[2] < 0 else (None, CC1[2])))
                    col_info.had_resolution = True
                    return  col_info, {'result': 0, 'stateProblem': [], 'timeProblem': [], 'compoundProblem': {'result':0, 'data': []}}
        return col_info, problem
    problem['result'] = 8
    return None, problem
