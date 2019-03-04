import numpy as np
import scipy.sparse as sp
from .matlab_utils import find
from .calc_equations import calc_equations
from .calc_states4 import calc_states, check_sd
from .classification4 import classification
from .calc_dict import calc_dict
from .SCLP_pivot_caseI import SCLP_pivot_caseI
from .SCLP_pivot4 import SCLP_pivot


def SCLP_solver(x_0, del_x_0, q_N, del_q_N, T, del_T, prim_name, dual_name, ThetaBar, cases, B1, B2, pivots,
                  base_sequence, totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    ITERATION[DEPTH] = 0
    if  len(prim_name.shape) > 1:
        pn = prim_name[:, 0]
    else:
        pn = prim_name
    if len(dual_name.shape) > 1:
        dn = dual_name[:, 0]
    else:
        dn = dual_name
    klist = np.sort(np.append(pn[pn > 0], dn[dn > 0]))
    jlist = np.sort(-np.append(pn[pn < 0], dn[dn < 0]))

    KK = len(klist)
    JJ = len(jlist)

    theta = 0
    tol_coeff = 1  # tolerance multiplier
    prevProblem = 0
    lastCollision = dict()

    Kset_0 = klist[np.hstack(np.logical_or(x_0 > 0, np.logical_and(x_0 == 0, del_x_0 > 0)))]
    Jset_N = jlist[np.hstack(np.logical_or(q_N > 0, np.logical_and(q_N == 0, del_q_N > 0)))]

    while cases != 'complete' and cases != 'solved__':

        # Kset_0 = klist[np.logical_or(np.hstack(x_0) > 0, np.logical_and(np.hstack(x_0) == 0, np.hstack(del_x_0) > 0))]
        # Jset_N = jlist[np.logical_or(np.hstack(q_N) > 0, np.logical_and(np.hstack(q_N) == 0, np.hstack(del_q_N) > 0))]

        spdx = sp.bmat([base_sequence['dx']])
        spdq = sp.bmat([base_sequence['dq']])

        if(len(set(base_sequence['places'])) < len(base_sequence['places'])):
            print('hwew')

        dx = spdx.toarray()
        dq = spdq.toarray()
        sdx = np.sign(dx)
        sdq = np.sign(dq)
        check_sd(sdx, True)
        check_sd(sdq, False)
        if STEPCOUNT == 11370:
            print('bbb')

        tau, dtau = calc_equations(klist, jlist, pivots, x_0, del_x_0, q_N, del_q_N, T, del_T, dx, dq)
        x, del_x, q, del_q = calc_states(dx, dq, x_0, del_x_0, q_N, del_q_N, tau, dtau, sdx, sdq, tolerance)
        cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q, del_q,
                                                               prim_name, B1, B2, sdx, sdq, tolerance, 1)
        if problem['result'] == 1 or problem['result'] == 2 or problem['result'] == 3:
            #TODO: review next if for bugs
            if problem['result'] == 2 and problem['timeProblem']['result'] == 2 and tol_coeff > 10000 and\
                    len(np.intersect1d(problem['timeProblem']['data'], np.arange(lastCollision['N1']+1, lastCollision['N2']), assume_unique=True))==0:
                tol_coeff = 0.1
                while problem['result'] == 2 and tol_coeff > 0.0001:
                    print('trying to resolve * ', tol_coeff, ' ...')
                    cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q,
                                                                       del_q,
                                                                       prim_name, B1, B2, sdx, sdq, tolerance, tol_coeff)
                    tol_coeff = 0.1 * tol_coeff
                tol_coeff = 1
            else:
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
                cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q, del_q,
                                                                   prim_name, B1, B2, sdx, sdq, tolerance, tol_coeff)
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
                N1 = lastCollision['N1']
                N2 = lastCollision['N2']
                #             v1 = lastCollision.v2 #change varible order
                #             v2 = lastCollision.v1 #change varible order
                Nnew = lastCollision['Nnew']
                N2_cor = N2+Nnew
                N2b = max(N2, N2_cor)
                lplaces = np.logical_or(np.array(base_sequence['places']) <= N1,
                                        np.array(base_sequence['places']) >= N2b)
                places = find(lplaces)
                if len(places) == 0:
                    newMat, newPlace = calc_dict(base_sequence, N1, N2b, pivots)
                    base_sequence['bases'] = [newMat]
                    base_sequence['places'] = [newPlace]
                else:
                    base_sequence['bases'] = [base_sequence['bases'][i] for i in places]
                    newPlace = [base_sequence['places'][i] for i in places]
                    base_sequence['places'] = [v if v < N2b else v - Nnew for v in newPlace]
                Npivots = len(lastCollision['old_pivots'])
                if N1 > 0:
                    if N2_cor - 1 == len(base_sequence['dx']):
                            pivots = pivots[0:N1] + lastCollision['old_pivots']
                    else:
                        pivots = pivots[0:N1] + lastCollision['old_pivots'] + pivots[N1 + Nnew + Npivots:]
                else:
                    pivots = lastCollision['old_pivots'] + pivots[(N1 + Nnew + Npivots):]
                prim_name = np.hstack((prim_name[:, 0:N1+1], lastCollision['old_pn'], prim_name[:, N2_cor:]))
                dual_name = np.hstack((dual_name[:, 0:N1+1], lastCollision['old_dn'], dual_name[:, N2_cor:]))
                base_sequence['dx'] = base_sequence['dx'][0:N1+1] + lastCollision['old_dx'] + base_sequence['dx'][N2_cor:]
                base_sequence['dq'] = base_sequence['dq'][0:N1+1] + lastCollision['old_dq'] + base_sequence['dq'][N2_cor:]
                # Kset_0 = klist[np.logical_or(x_0 > 0, np.logical_and(x_0 == 0, del_x_0 > 0))]
                # Jset_N = jlist[np.logical_or(q_N > 0, np.logical_and(q_N == 0, del_q_N > 0))]
                # flag = True
                #             if problem.result == 2
                #                 nn1 = min(problem.timeProblem.data)
                #                 nn2 = max(problem.timeProblem.data)
                #                 if length(problem.timeProblem.data) == length(nn1:nn2)
                #                     if nn1 <= N1
                #                         N1 = nn1 - 1
                #                     end
                #                     N2 = nn2 - Nnew + Nold + 1
                #                     v1 = lastCollision.v1
                #                     v2 = lastCollision.v2
                #                     cases = lastCollision.cases
                #                 else
                #                     flag= true
                #                 end
                #             else
                #                 flag = true
                #             end
                spdx = sp.hstack(base_sequence['dx'])
                spdq = sp.hstack(base_sequence['dq'])
                dx = spdx.toarray()
                dq = spdq.toarray()
                sdx = np.sign(dx)
                sdq = np.sign(dq)

                tau, dtau = calc_equations(klist, jlist, pivots, x_0, del_x_0, q_N, del_q_N, T, del_T, dx, dq)
                x, del_x, q, del_q = calc_states(dx, dq, x_0, del_x_0, q_N, del_q_N, tau, dtau, sdx, sdq, tolerance)
                cases, Delta, N1, N2, v1, v2, problem = classification(tau, dtau, klist, jlist, dx, dq, x, del_x, q,
                                                                       del_q,
                                                                       prim_name, B1, B2, sdx, sdq, tolerance, tol_coeff)
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
                                                                               del_x, q, del_q, prim_name, B1, B2,
                                                                               sdx, sdq, tolerance, tol_coeff)
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

        if theta1 > 1 and DEPTH > 0:
            print("Theta > 1....")
            #cases = 'theta>1_'

        print(STEPCOUNT, DEPTH, ITERATION[DEPTH], JJ, 'x', KK, NN, theta, theta1, cases, N1, N2, v1, v2, len(base_sequence['places']))
        lastCollision = {'cases': cases, 'theta': theta, 'Delta': Delta,
                                 'N1': N1, 'N2': N2, 'v1': v1, 'v2': v2}
        if cases == 'Case i__':
            base_sequence, pivots, prim_name, dual_name = SCLP_pivot_caseI(base_sequence, pivots, prim_name, dual_name, N1, N2, NN)

        elif cases == 'Case ii_' or cases == 'Case iii':
            if cases == 'Case ii_':
                cor_N1 = N1+1
                if N1 > -1:
                    lastCollision['old_pivots'] = pivots[N1:N2+1].copy()
                else:
                    lastCollision['old_pivots'] = pivots[N1+1:N2+1].copy()
                lastCollision['old_dx'] = base_sequence['dx'][cor_N1: N2].copy()
                lastCollision['old_dq'] = base_sequence['dq'][cor_N1: N2].copy()
                lastCollision['old_pn'] = prim_name[:, cor_N1: N2].copy()
                lastCollision['old_dn'] = dual_name[:, cor_N1: N2].copy()

            prim_name, dual_name, pivots, base_sequence, STEPCOUNT, ITERATION = SCLP_pivot(Kset_0, Jset_N, prim_name, dual_name, N1, N2, v1,
                                                                     v2, pivots, base_sequence, KK, JJ, NN, totalK, totalJ, DEPTH,
                                                                     STEPCOUNT, ITERATION, settings, tolerance)

            #statData = {'cases': cases, 'N1': N1, 'N2': N2, 'minBases': settings['minBases'],
            #            'maxBases': settings['maxBases'], 'basesRate': settings['basesRate']}
            #base_sequence = clearBaseSequence(base_sequence, statData)

        lastCollision['Nnew'] = len(base_sequence['dx'])-NN
        #print(STEPCOUNT, base_sequence['places'], [sum(EE['A'][0,:]) for EE in base_sequence['bases']])
        x_0 = x_0 + del_x_0 * Delta
        q_N = q_N + del_q_N * Delta
        T = T + del_T * Delta
        theta = theta1

    return prim_name, dual_name, x_0, q_N, T, pivots, base_sequence, STEPCOUNT



