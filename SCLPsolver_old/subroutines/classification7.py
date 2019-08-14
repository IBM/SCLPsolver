import numpy as np
from .calc_statecollide5 import calc_statecollide
from .calc_timecollide7a import calc_timecollide
from .calc_order_ratio6 import calc_order_ratio
from .collision_info7 import collision_info

#function [ cases, Delta, N1, N2, v1,v2, problem ] =

#'#@profile
def classification(tau,dtau,klist,jlist,dx,dq,x,del_x,q,del_q,solution,B1,B2, sdx, sdq, lastN1, lastN2, last_case, tolerance, tol_coeff):
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

    max_tol_coeff = 0.01/tolerance
    min_tol_coeff = 0.01
    if tol_coeff == max_tol_coeff:
        print("Maximum tolerance coefficient reached")
        raise Exception()
    NN = dx.shape[1]
    problem = {'result': 0, 'stateProblem': [], 'timeProblem': [], 'compoundProblem': {'result':0, 'data': []}}
    Delta = 0
    N1 = -1
    N2 = NN
    v1 = []
    v2 = []
    case = ''

    test1 = 0
    test2 = 0
    if len(B1) > 0 or len(B2) > 0:
        if len(B1) > 0:
            test1 = solution.get_name_diff_with0(B1).size
        if len(B2) > 0:
            test2 = solution.get_name_diff_withN(B2).size
    if (len(B1) > 0 or len(B2) > 0) and test1 == 0 and test2 == 0:
        return collision_info('complete', 0, -1, NN, [], []), problem


    CC1, prob = calc_statecollide(klist,jlist,x,del_x,q,del_q, sdx, sdq, tolerance)
    problem['stateProblem'] = prob
    if prob['result'] != 0:
        problem['result'] = 1
        return collision_info('', Delta, N1, N2, v1, v2), problem

    CC2, prob = calc_timecollide(tau,dtau, solution.pivots, lastN1, lastN2, last_case, tolerance, tol_coeff)
    problem['timeProblem'] = prob
    if prob['result'] != 0 and prob['result'] != 6:
        problem['result'] = problem['result'] + 2
        return collision_info('', Delta, N1, N2, v1, v2), problem

    if 	len(CC1) == 0 and len(CC2) == 0:
        case = 'complete'
        Delta = np.inf
        return collision_info(case, Delta, N1, N2, v1, v2), problem

    Didle = 0
    if	len(CC1) > 0 and len(CC2) > 0:
        Didle = CC1[0] - CC2[0]
        if abs(Didle) <= tolerance:
            Didle = 0
        if Didle == 0 and not (CC2[1] - 1 <= CC1[1] and CC1[1] <= CC2[2]+1):
            print('time shrink as well as state hits zero elsewhere\n')
            problem['result'] = problem['result'] + 4
            problem['compoundProblem']['result'] = 1
            return collision_info('', Delta, N1, N2, v1, v2), problem
    if	(len(CC1) > 0 and len(CC2) == 0) or Didle < 0:
        case = 'Case iii'
        Delta = CC1[0]
        N1 = CC1[1]
        N2 = CC1[1] + 1
        if CC1[2] < 0:
            v1 = CC1[2]
        else:
            v2 = CC1[2]
    elif (len(CC1) == 0 and len(CC2) > 0) or Didle >= 0:
        Delta = CC2[0]
        N1 = CC2[1] - 1
        N2 = CC2[2] + 1
        if N1 == -1 or N2 == NN:
            case = 'Case i__'
        else:
            vlist = solution.pivots.get_out_difference(N1, N2)
            if len(vlist) > 2:
                print('More than two variables leave in time shrink ....')
                problem['result'] = problem['result'] + 4
                problem['compoundProblem']['result'] = 2
                return collision_info('', Delta, N1, N2, v1, v2), problem
            elif len(vlist) == 1:
                case = 'Case i__'
                return collision_info(case, Delta, N1, N2, v1, v2), problem
            elif len(vlist) == 2:
                case = 'Case ii_'
                order_ratio, correct = calc_order_ratio(vlist[0],vlist[1],N1,N2,klist,jlist,dx,dq,x,del_x,q,del_q,tau,dtau,Delta/2)
                if abs(abs(order_ratio)-1) < tolerance * tol_coeff:
                    print('Value of R unclear...')
                if abs(order_ratio) < 1: #the strange case when R < 0 should be perferctly reviewed
                    v1 = vlist[0]
                    v2 = vlist[1]
                else:
                    v1 = vlist[1]
                    v2 = vlist[0]
                if correct:
                    return collision_info(case, Delta, N1, N2, v1, v2, prob['had_resolution']), problem
                else:
                    problem['result'] = 5
                    return collision_info(case, Delta, N1, N2, v1, v2), problem
    return collision_info(case, Delta, N1, N2, v1, v2), problem
