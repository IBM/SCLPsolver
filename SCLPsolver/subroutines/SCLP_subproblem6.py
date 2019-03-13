import numpy as np
from .extract_rates5 import extract_rates
from .SCLP_base_sequence import SCLP_base_sequence
from .SCLP_solution6 import SCLP_solution
from .sparse_matrix_constructor import sparse_matrix_constructor
from .pivot import base_pivot
from .matlab_utils import find
from .parametric_line import parametric_line
from .prepare_subproblem_data import prepare_subproblem_basis, prepare_subproblem_boundaries


#'#@profile
def SCLP_subproblem(pbaseDD,dbaseDD,DD, v1,v2,Kset_0, Jset_N,
                     AAN1,AAN2, KK, JJ, totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    # Excluding the k's and j's which are > 0
    DDred, pbaseDDred, dbaseDDred, pbaseB1red, pbaseB2red = prepare_subproblem_basis(DD, pbaseDD, dbaseDD, Kset_0, Jset_N, v1, v2, AAN1, AAN2)

    klist = np.sort(np.append(pbaseDDred[pbaseDDred > 0], dbaseDDred[dbaseDDred > 0]))
    jlist = np.sort(-np.append(pbaseDDred[pbaseDDred < 0], dbaseDDred[dbaseDDred < 0]))

    lk = np.size(klist)
    lj = np.size(jlist)

    # The starting sequence
    new_bs = SCLP_base_sequence({'prim_name': pbaseDDred, 'dual_name': dbaseDDred,'A': DDred.copy()})
    dx, dq = extract_rates(pbaseDDred, dbaseDDred, DDred, lk, lj, totalK, totalJ)

    solution = SCLP_solution(None, new_bs, dx, dq)
    # performing the left and right first pivots
    #		the right pivot:
    K_0 = []
    J_N = []
    if np.size(pbaseB2red) > 0:
        if not isinstance(v1, list):
            if v1 > 0:
                K_0 = [v1]
            else:
                J_N = [-v1]
        if not isinstance(v2, list):
            if v2 < 0:
                J_N.append(-v2)
        from .SCLP_pivot6 import SCLP_pivot
        solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(K_0,J_N,solution,0,1,[],v1, lk, lj, 1, totalK, totalJ,
                                                    DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 1:
            print('Problem during right pivot...')
            return [], [], [], 0, STEPCOUNT, ITERATION, pivot_problem
    #		the left pivot:
    K_0 = []
    J_N = []
    if np.size(pbaseB1red) > 0:
        if not isinstance(v2, list):
            if v2 > 0:
                K_0 = [v2]
            else:
                J_N = [-v2]
        if not isinstance(v1, list):
            if v1 > 0:
                K_0.append(v1)
        from .SCLP_pivot6 import SCLP_pivot
        solution, STEPCOUNT, ITERATION, pivot_problem  = SCLP_pivot(K_0,J_N,solution,-1,0,v2,[], lk, lj, 1, totalK, totalJ,
                                                    DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 1:
            print('Problem during left pivot...')
            return [], [], [], 0,  STEPCOUNT, ITERATION, pivot_problem

    # prepare the boundaries
    del_q_N, del_x_0, q_N, x_0 = prepare_subproblem_boundaries(DD, pbaseDD, dbaseDD, jlist, klist, lj, lk, v1, v2, AAN1, AAN2)

    param_line = parametric_line(x_0, q_N, klist, jlist, 1, 0, del_x_0, del_q_N)

    #############################################
    # solving the subproblem
    from .SCLP_solver6 import SCLP_solver
    solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 1,'sub_prob', pbaseB1red, pbaseB2red,
                                                     totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
    if pivot_problem['result'] == 1:
        return [], [], [],0, STEPCOUNT, ITERATION, pivot_problem
    else:
        pivot_problem = {'result': 0}
    #############################################

    Npivots = len(solution.pivots)
    #Warning this based on assumption that first basis in new_base_sequence is equal to the AAN1 and/or last basis is equal to the AAN2
    if Npivots > 0:
        dx = sparse_matrix_constructor(None, None, KK)
        dq = sparse_matrix_constructor(None, None, JJ)
        if AAN1 is not None:
            pm1 = AAN1['prim_name'].copy()
            dm1 = AAN1['dual_name'].copy()
            DD1 = AAN1['A'].copy()
            # zz1 = np.zeros(len(pm1))
            # zz2 = np.zeros(len(dm1))
            if AAN2 is not None:
                Npivots -=1
                ran = enumerate(solution.pivots[:-1])
            else:
                ran = enumerate(solution.pivots)
            for i,piv1 in ran:
                #DD1,pm1,dm1,zz1,zz2 = full_pivot(DD1,find(pm1==piv1[0])[0],find(dm1==piv1[1])[0],pm1.copy(),dm1.copy(),zz1.copy(),zz2.copy())
                DD1, pm1, dm1 = base_pivot(DD1, find(pm1 == piv1[0])[0], find(dm1 == piv1[1])[0], pm1, dm1)
                ndx, ndq = extract_rates(pm1, dm1, DD1, KK, JJ, totalK, totalJ)
                dx.append(ndx)
                dq.append(ndq)
        else:
            pm1 = AAN2['prim_name'].copy()
            dm1 = AAN2['dual_name'].copy()
            DD1 = AAN2['A'].copy()
            # zz1 = np.zeros(len(pm1))
            # zz2 = np.zeros(len(dm1))
            for i,piv1 in enumerate(reversed(solution.pivots)):
                #DD1,pm1,dm1,zz1,zz2 = full_pivot(DD1,find(pm1==piv1[1]),find(dm1==piv1[0]),pm1.copy(),dm1.copy(),zz1.copy(),zz2.copy())
                DD1, pm1, dm1 = base_pivot(DD1, find(pm1 == piv1[1]), find(dm1 == piv1[0]), pm1, dm1)
                ndx, ndq = extract_rates(pm1, dm1, DD1, KK, JJ, totalK, totalJ)
                dx.prepend(ndx)
                dq.prepend(ndq)
    return dx, dq, solution.pivots, Npivots, STEPCOUNT, ITERATION, pivot_problem
