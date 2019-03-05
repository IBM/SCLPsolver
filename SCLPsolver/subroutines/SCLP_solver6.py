import numpy as np
from .matlab_utils import find
from .calc_equations import calc_equations
from .calc_states4 import calc_states, check_sd
from .classification6 import classification
from .SCLP_pivot6 import SCLP_pivot

#'#@profile
def SCLP_solver(solution, x_0, del_x_0, q_N, del_q_N, T, del_T, ThetaBar, cases, B1, B2, klist, jlist, totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    ITERATION[DEPTH] = 0

    KK = len(klist)
    JJ = len(jlist)

    theta = 0
    tol_coeff = 1  # tolerance multiplier
    prevProblem = 0
    lastCollision = {'N1': -1, 'N2': 1, 'Nnew': 1}
    pivot_problem = {'result': 0}
    print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, solution.NN, 0, 0, cases)
    Kset_0 = klist[np.hstack(np.logical_or(x_0 > 0, np.logical_and(x_0 == 0, del_x_0 > 0)))]
    Jset_N = jlist[np.hstack(np.logical_or(q_N > 0, np.logical_and(q_N == 0, del_q_N > 0)))]

    while cases != 'complete' and cases != 'solved__':

        if not solution.base_sequence.check_places():
            raise Exception('Bases placement failure!')

        dx = solution.dx.get_matrix()
        dq = solution.dq.get_matrix()
        sdx = np.ones((dx.shape[0], dx.shape[1] + 2))
        sdq = np.ones((dq.shape[0], dq.shape[1] + 2))
        np.sign(dx, out=sdx[:,1:-1])
        np.sign(dq, out=sdq[:,1:-1])
        check_sd(sdx[:,1:-1], True)
        check_sd(sdq[:,1:-1], False)

        lastN1 =lastCollision['N1']
        lastN2 = lastCollision['N2'] + lastCollision['Nnew']
        tau, dtau = calc_equations(klist, jlist, solution.pivots, x_0, del_x_0, q_N, del_q_N, T, del_T, dx, dq)
        x, del_x, q, del_q = calc_states(dx, dq, x_0, del_x_0, q_N, del_q_N, tau, dtau, sdx, sdq, tolerance)
        cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q, del_q,
                                                                   solution, B1, B2, sdx, sdq, lastN1, lastN2, tolerance, 1)
        if problem['result'] == 1 or problem['result'] == 2 or problem['result'] == 3:
            tol_coeff = 10 * tol_coeff
            prevProblem = problem['result']
            if 'data' in problem.keys():
                print('Problem data: ',str(problem['data']))
        elif problem['result'] == 4:
            print('More than two variables leave in time shrink ....')
            while tol_coeff <= 10000 and problem['result'] == 4:
                if tol_coeff < 10 and prevProblem !=2:
                    if N2 - N1 == 2 or tol_coeff <= 0.001:
                        tol_coeff = 10
                    else:
                        tol_coeff = 0.1 * tol_coeff
                else:
                    tol_coeff = 10 * tol_coeff
                print('trying to resolve * ', tol_coeff, ' ...')
                cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q,
                                                                           del_q, solution, B1, B2, sdx, sdq, lastN1, lastN2, tolerance,
                                                                           tol_coeff)
            if problem['result'] == 0:
                tol_coeff = 1
                print('ok!')
            else:
                print('fail!')
            prevProblem = 4
        else:
            tol_coeff = 1
            prevProblem = problem['result']

        if problem['result'] > 0 and DEPTH == 0:
            if lastCollision['cases'] == 'Case ii_':
                # rewinding to previous iteration
                print('rewind... trying to resolve * ', tol_coeff, ' ...')
                Delta = lastCollision['Delta']
                x_0 = x_0 - del_x_0 * Delta
                q_N = q_N - del_q_N * Delta
                T = T - del_T * Delta
                theta = theta - Delta
                #             v1 = lastCollision.v2 #change varible order
                #             v2 = lastCollision.v1 #change varible order
                solution.update_rewind(lastCollision['N1'], lastCollision['N2'], lastCollision['Nnew'],
                                       lastCollision['old_dx'], lastCollision['old_dq'], lastCollision['old_pivots'])
                lastN1 = lastCollision['lastN1']
                lastN2 = lastCollision['lastN2']
                dx = solution.dx.get_matrix()
                dq = solution.dq.get_matrix()
                sdx = np.ones((dx.shape[0], dx.shape[1] + 2))
                sdq = np.ones((dq.shape[0], dq.shape[1] + 2))
                np.sign(dx, out=sdx[:, 1:-1])
                np.sign(dq, out=sdq[:, 1:-1])

                tau, dtau = calc_equations(klist, jlist, solution.pivots, x_0, del_x_0, q_N, del_q_N, T, del_T, dx, dq)
                x, del_x, q, del_q = calc_states(dx, dq, x_0, del_x_0, q_N, del_q_N, tau, dtau, sdx, sdq, tolerance)
                cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q,
                                                                           del_q, solution, B1, B2, sdx, sdq, lastN1, lastN2,
                                                                           tolerance, tol_coeff)
                if problem['result'] == 4:
                    while tol_coeff >= 0.001 and problem['result'] == 4:
                        if tol_coeff >= 10:
                            if tol_coeff <= 1000:
                                tol_coeff = 10 * tol_coeff
                            else:
                                tol_coeff = 0.1
                        else:
                            tol_coeff = 0.1 * tol_coeff
                        print('trying to resolve * ', tol_coeff, ' ...')
                        cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x,
                                                                                   del_x, q, del_q, solution, B1,
                                                                                   B2, sdx, sdq, lastN1, lastN2, tolerance, tol_coeff)
                        if problem['result'] == 0:
                            tol_coeff = 1
                            print('ok!')
                        else:
                            print('fail!')

        if cases == 'complete' and DEPTH > 0:
            Delta = min(0.1 * theta, (1 - theta) / 2)

        if DEPTH == 0 and theta + Delta > ThetaBar:
            cases = 'solved__'
            Delta = ThetaBar - theta

        if cases == 'complete' and DEPTH == 0:
            Delta = 0.1 * theta

        NN = len(tau)
        STEPCOUNT = STEPCOUNT + 1

        ITERATION[DEPTH] = ITERATION[DEPTH] + 1
        theta1 = theta + Delta

        if theta1 >= 1 and DEPTH > 0 and cases != 'complete':
            print("Theta > 1....")
            pivot_problem['result'] = 1
            return solution, x_0, q_N, T, STEPCOUNT, pivot_problem


        print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, NN, theta, theta1, cases, N1, N2, v1, v2, len(solution.base_sequence.places))
        lastCollision = {'cases': cases, 'theta': theta, 'Delta': Delta,
                                 'N1': N1, 'N2': N2, 'v1': v1, 'v2': v2, 'lastN1': lastN1, 'lastN2':lastN2}
        if cases == 'Case i__':
            solution.update_caseI(N1, N2)
        elif cases == 'Case ii_' or cases == 'Case iii':
            if cases == 'Case ii_':
                store_collision_info(N1, N2, lastCollision, solution)

            solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(Kset_0, Jset_N, solution, N1, N2, v1,
                                                                     v2, KK, JJ, NN, totalK, totalJ, DEPTH,
                                                                     STEPCOUNT, ITERATION, settings, tolerance)


            while pivot_problem['result'] == 1 and tol_coeff < 0.0001/tolerance: # theta > 1
                tol_coeff = tol_coeff * 10
                print('trying to resolve * ', tol_coeff, '...')
                cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x,
                                                                           del_x, q, del_q, solution, B1,
                                                                           B2, sdx, sdq, lastN1, lastN2, tolerance, tol_coeff)
                print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, NN, theta, theta1, cases, N1, N2, v1, v2,
                      len(solution.base_sequence.places))
                lastCollision = {'cases': cases, 'theta': theta, 'Delta': Delta,
                                 'N1': N1, 'N2': N2, 'v1': v1, 'v2': v2, 'lastN1': lastN1, 'lastN2': lastN2}
                if cases == 'Case i__':
                    solution.update_caseI(N1, N2)
                    pivot_problem['result'] = 0
                elif cases == 'Case ii_' or cases == 'Case iii':
                    if cases == 'Case ii_':
                        store_collision_info(N1, N2, lastCollision, solution)
                    solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(Kset_0, Jset_N, solution, N1, N2, v1,
                                                                           v2, KK, JJ, NN, totalK, totalJ, DEPTH,
                                                                           STEPCOUNT, ITERATION, settings,
                                                                           tolerance)
                if DEPTH > 1:
                    break

            if pivot_problem['result'] == 1:
                if DEPTH > 0:
                    return solution, x_0, q_N, T, STEPCOUNT, pivot_problem
                else:
                    print('Changing variables order...')
                    lastCollision['v1'] = v2
                    lastCollision['v2'] = v1
                    tol_coeff = 1
                    solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(Kset_0, Jset_N, solution, N1, N2, v2,
                                                                               v1, KK, JJ, NN, totalK, totalJ, DEPTH,
                                                                               STEPCOUNT, ITERATION, settings,
                                                                               tolerance)

            #statData = {'cases': cases, 'N1': N1, 'N2': N2, 'minBases': settings['minBases'],
            #            'maxBases': settings['maxBases'], 'basesRate': settings['basesRate']}
            #base_sequence = clearBaseSequence(base_sequence, statData)
        lastCollision['Nnew'] = solution.NN - NN
        x_0 = x_0 + del_x_0 * Delta
        q_N = q_N + del_q_N * Delta
        T = T + del_T * Delta
        theta = theta1

    return solution, x_0, q_N, T, STEPCOUNT, pivot_problem


def store_collision_info(N1, N2, lastCollision, solution):
    cor_N1 = N1 + 1
    if N1 > -1:
        lastCollision['old_pivots'] = solution.pivots[N1:N2 + 1].copy()
    else:
        lastCollision['old_pivots'] = solution.pivots[N1 + 1:N2 + 1].copy()
    lastCollision['old_dx'] = solution.dx.get_sub_matrix(cor_N1, N2)
    lastCollision['old_dq'] = solution.dq.get_sub_matrix(cor_N1, N2)
