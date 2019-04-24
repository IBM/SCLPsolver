import numpy as np
from .matlab_utils import find
from .calc_equations6 import calc_equations
from .calc_states6 import calc_states, check_sd
from .classification6 import classification
from .SCLP_pivot6 import SCLP_pivot
from .collision_info import collision_info

#'#@profile
def SCLP_solver(solution, param_line, ThetaBar, cases, B1, B2, totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    ITERATION[DEPTH] = 0

    KK = len(param_line.klist)
    JJ = len(param_line.jlist)

    theta = 0
    tol_coeff = 1  # tolerance multiplier
    prevProblem = 0
    col_info = collision_info(cases)
    lastCollision = None
    pivot_problem = {'result': 0}
    print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, solution.NN, 0, 0, cases)
    rewind_required = False
    dx, dq, sdx, sdq = solution.get_state_slopes()
    if not check_sd(sdx[:, 1:-1], True) or not check_sd(sdq[:, 1:-1], False):
        return solution, STEPCOUNT, {'result': 1}

    while col_info.case != 'complete' and col_info.case != 'solved__':

        if not solution.base_sequence.check_places():
            raise Exception('Bases placement failure!')

        if not rewind_required:
            if lastCollision is None:
                lastN1 = -1
                lastN2 = solution.NN
                last_case =  col_info.case
            else:
                lastN1 =lastCollision.N1
                lastN2 = lastCollision.N2 + lastCollision.Nnew
                last_case = lastCollision.case
            tau, dtau = calc_equations(param_line, solution.pivots, dx, dq)
            x, del_x, q, del_q = calc_states(dx, dq, param_line, tau, dtau, sdx, sdq)
            col_info, problem = classification(tau, dtau, param_line.klist, param_line.jlist, dx, dq, x, del_x, q, del_q,
                                                                       solution, B1, B2, sdx, sdq, lastN1, lastN2, last_case, tolerance, 1)
            if problem['result'] == 5:
                tol_coeff = 10
                while tol_coeff <= 0.01 / tolerance:
                    print('trying to resolve * ', tol_coeff, ' ...')
                    new_col_info, problem = classification(tau, dtau, param_line.klist, param_line.jlist, dx, dq, x, del_x,
                                                       q, del_q,
                                                       solution, B1, B2, sdx, sdq, lastN1, lastN2, last_case, tolerance,
                                                       tol_coeff)
                    tol_coeff = 10 * tol_coeff
                    if new_col_info != col_info:
                        col_info = new_col_info
                    if problem['result'] == 0:
                        break
                if problem['result'] > 0:
                    if last_case != 'Case ii_':
                        tol_coeff = 0.001
                        while tol_coeff <= 1:
                            print('trying to resolve * ', tol_coeff, ' ...')
                            col_info, problem = classification(tau, dtau, param_line.klist, param_line.jlist, dx, dq, x,
                                                                   del_x,
                                                                   q, del_q,
                                                                   solution, B1, B2, sdx, sdq, lastN1, lastN2, last_case,
                                                                   tolerance,
                                                                   tol_coeff)
                            tol_coeff = 10 * tol_coeff
                            if problem['result'] == 0:
                                break
            if problem['result'] > 0 and problem['result'] != 4:
                if last_case == 'Case ii_':
                    tol_coeff = 10
                    prevProblem = problem['result']
                    rewind_required = True
                else:
                    print('Trying to ignore the problem....')
            elif problem['result'] == 4:
                while tol_coeff <= 10000 and problem['result'] > 0:
                    if tol_coeff < 10 and prevProblem !=2:
                        if col_info.N2 - col_info.N1 == 2 or tol_coeff <= 0.001:
                            tol_coeff = 10
                        else:
                            tol_coeff = 0.1 * tol_coeff
                    else:
                        tol_coeff = 10 * tol_coeff
                    print('trying to resolve * ', tol_coeff, ' ...')
                    col_info, problem = classification(tau, dtau, param_line.klist, param_line.jlist, dx, dq, x, del_x, q,
                                                        del_q, solution, B1, B2, sdx, sdq, lastN1, lastN2,last_case,
                                                       tolerance,  tol_coeff)
                if problem['result'] == 0:
                    tol_coeff = 1
                    rewind_required = False
                    print('ok!')
                else:
                    print('fail!')
                    tol_coeff = 10
                    rewind_required = True
                prevProblem = 4
            else:
                rewind_required = False
                tol_coeff = 1
                prevProblem = problem['result']

        if rewind_required:
            if DEPTH == 0:
                if lastCollision.case == 'Case ii_':
                    # rewinding to previous iteration
                    print('rewind... ')
                    last_case = 'rewind'
                    param_line.backward_to(lastCollision.delta)
                    theta = theta - lastCollision.delta
                    solution.update_rewind(lastCollision)
                    lastN1 = lastCollision.lastN1
                    lastN2 = lastCollision.lastN2
                    dx, dq, sdx, sdq = solution.get_state_slopes()

                    tau, dtau = calc_equations(param_line, solution.pivots, dx, dq)
                    x, del_x, q, del_q = calc_states(dx, dq, param_line, tau, dtau, sdx, sdq)
                    resolved = False
                    while tol_coeff <= 0.01/tolerance:
                        print('trying to resolve * ', tol_coeff, ' ...')
                        col_info, problem = classification(tau, dtau, param_line.klist, param_line.jlist, dx, dq, x, del_x,
                                                       q, del_q, solution, B1, B2, sdx, sdq, lastN1, lastN2, last_case, tolerance,tol_coeff)
                        if problem['result'] > 0:
                            tol_coeff = tol_coeff * 10
                        else:
                            if col_info == lastCollision:
                                tol_coeff = tol_coeff * 10
                            else:
                                resolved = True
                                break

                    if not resolved:
                        if problem['result'] == 6: #no such type
                            print('Trying to ignore!')
                        else:
                            print('Unable to go forward!')
                            return solution, STEPCOUNT, pivot_problem
                else:
                    raise Exception('Rewind on case I or III not supported yet!')
            else:
                pivot_problem = {'result':1}
                print('Rewind in subproblem not supported. Returning to main problem!')
                return solution, STEPCOUNT, pivot_problem

        if col_info.case == 'complete' and DEPTH > 0:
            col_info.delta = min(0.1 * theta, (1 - theta) / 2)

        if DEPTH == 0 and theta + col_info.delta > ThetaBar:
            col_info.case = 'solved__'
            col_info.delta = ThetaBar - theta

        if col_info.case == 'complete' and DEPTH == 0:
            col_info.delta = 0.1 * theta

        NN = len(tau)
        STEPCOUNT = STEPCOUNT + 1

        ITERATION[DEPTH] = ITERATION[DEPTH] + 1
        theta1 = theta + col_info.delta

        print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, NN, theta, theta1, col_info.case, col_info.N1, col_info.N2,
              col_info.v1, col_info.v2, len(solution.base_sequence.places))

        if theta1 >= 1 and DEPTH > 0 and col_info.case != 'complete':
            print("Theta > 1....")
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, pivot_problem

        thisCollision = col_info
        thisCollision.theta = theta
        thisCollision.lastN1 = lastN1
        thisCollision.lastN2 = lastN2

        if col_info.case == 'Case i__':
            solution.update_caseI(col_info.N1, col_info.N2)
            dx, dq, sdx, sdq = solution.get_state_slopes()
            rewind_required = False
        elif col_info.case == 'Case ii_' or col_info.case == 'Case iii':
            if col_info.case == 'Case ii_':
                col_info.store_rewind_info(solution)

            solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(param_line.Kset_0, param_line.Jset_N, solution,
                                                                       col_info.N1, col_info.N2, col_info.v1,
                                                                     col_info.v2, KK, JJ, NN, totalK, totalJ, DEPTH,
                                                                     STEPCOUNT, ITERATION, settings, tolerance)

            start_tol_coeff = tol_coeff
            while pivot_problem['result'] == 1 and tol_coeff <= 0.01/tolerance: # theta > 1
                tol_coeff = tol_coeff * 10
                print('trying to resolve * ', tol_coeff, '...')
                new_col_info, problem = classification(tau, dtau, param_line.klist, param_line.jlist, dx, dq, x,
                                                        del_x, q, del_q, solution, B1, B2, sdx, sdq, lastN1, lastN2,
                                                       last_case, tolerance, tol_coeff)
                if new_col_info == col_info or problem['result'] == 5 or problem['result'] == 4:
                    continue

                col_info = new_col_info
                print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, NN, theta, theta1, col_info.case, col_info.N1, col_info.N2, col_info.v1, col_info.v2,
                      len(solution.base_sequence.places))

                thisCollision = col_info
                thisCollision.theta = theta
                thisCollision.lastN1 = lastN1
                thisCollision.lastN2 = lastN2

                if col_info.case == 'Case i__':
                    solution.update_caseI(col_info.N1, col_info.N2)
                    pivot_problem['result'] = 0
                elif col_info.case == 'Case ii_' or cases == 'Case iii':
                    if col_info.case == 'Case ii_':
                        thisCollision.store_rewind_info(solution)
                    solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(param_line.Kset_0, param_line.Jset_N, solution,
                                                                       col_info.N1, col_info.N2, col_info.v1,
                                                                     col_info.v2, KK, JJ, NN, totalK, totalJ, DEPTH,
                                                                     STEPCOUNT, ITERATION, settings, tolerance)


            if pivot_problem['result'] == 1:
                if DEPTH > 0:
                    return solution, STEPCOUNT, pivot_problem
                else:
                    tol_coeff = start_tol_coeff * 10
                    rewind_required = True
            else:
                rewind_required = False

        if not rewind_required:
            thisCollision.Nnew = solution.NN - NN
            dx, dq, sdx, sdq = solution.get_state_slopes()
            check_sd(sdx[:, 1:-1], True)  ###
            check_sd(sdq[:, 1:-1], False)  ###
            lastCollision = thisCollision
            param_line.forward_to(col_info.delta)
            theta = theta1
            #statData = {'cases': cases, 'N1': N1, 'N2': N2, 'minBases': settings['minBases'],
            #            'maxBases': settings['maxBases'], 'basesRate': settings['basesRate']}
            #base_sequence = clearBaseSequence(base_sequence, statData)

    return solution, STEPCOUNT, pivot_problem

