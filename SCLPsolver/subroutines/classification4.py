import numpy as np
from .calc_statecollide4 import calc_statecollide
from .calc_timecollide4 import calc_timecollide
from .calc_order_ratio import calc_order_ratio

#function [ cases, Delta, N1, N2, v1,v2, problem ] =


def classification(tau,dtau,klist,jlist,dx,dq,x,del_x,q,del_q,prim_name,B1,B2, sdx, sdq, tolerance, tol_coeff):
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
    tflag = False
    if len(B1) > 0:
        test1 = np.setdiff1d(prim_name[:,0],B1, assume_unique=True).size
        tflag = True
    if len(B2) > 0:
        test2 = np.setdiff1d(prim_name[:,-1:],B2, assume_unique=True).size
        tflag = True
    if tflag:
        if test1 == 0 and test2 ==0:
            case = 'complete'
            return case, Delta, N1, N2, v1, v2, problem

    CC1, prob = calc_statecollide(klist,jlist,x,del_x,q,del_q, sdx, sdq, tolerance)
    problem['stateProblem'] = prob
    if prob['result'] != 0:
        problem['result'] = 1
        return '', Delta, N1, N2, v1, v2, problem

    CC2, prob = calc_timecollide(tau,dtau,tolerance,tol_coeff)
    problem['timeProblem'] = prob
    if prob['result'] != 0:
        problem['result'] = problem['result'] + 2
        return '', Delta, N1, N2, v1, v2, problem

    if 	len(CC1) == 0 and len(CC2) == 0:
        case = 'complete'
        Delta = np.inf
        return case, Delta, N1, N2, v1, v2, problem

    Didle = 0
    if	len(CC1) > 0 and len(CC2) > 0:
        Didle = CC1[0] - CC2[0]
        if abs(Didle) <= tolerance:
            Didle = 0
        if Didle == 0 and not (CC2[1] - 1 <= CC1[1] and CC1[1] <= CC2[2]+1):
            print('time shrink as well as state hits zero elsewhere\n')
            problem['result'] = problem['result'] + 4
            problem['compoundProblem']['result'] = 1
            return '', Delta, N1, N2, v1, v2, problem
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
            base1 = prim_name[:,N1]
            base2 = prim_name[:,N2]
            vlist = np.setdiff1d(base1, base2, assume_unique=True)
            if vlist.size > 2:
                problem['result'] = problem['result'] + 4
                problem['compoundProblem']['result'] = 2
                return '', Delta, N1, N2, v1, v2, problem
            elif vlist.size == 1:
                case = 'Case i__'
                return case, Delta, N1, N2, v1, v2, problem
            elif vlist.size == 2:
                case = 'Case ii_'
                order_ratio = calc_order_ratio(vlist[0],vlist[1],N1,N2,klist,jlist,dx,dq,x,del_x,q,del_q,tau,dtau,Delta/2)
                if abs(order_ratio) < 1: #the strange case when R < 0 should be perferctly reviewed
                    v1 = vlist[0]
                    v2 = vlist[1]
                else:
                    v1 = vlist[1]
                    v2 = vlist[0]
                return case, Delta, N1, N2, v1, v2, problem
    return case, Delta, N1, N2, v1, v2, problem