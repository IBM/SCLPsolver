import numpy as np
from .SCLP_solution7 import SCLP_solution
from .parametric_line import parametric_line
from .prepare_subproblem_data import prepare_subproblem_basis, prepare_subproblem_boundaries
from .collision_info8 import collision_info


#'#@profile
def SCLP_subproblem(pbaseDD,dbaseDD,DD, v1,v2,Kset_0, Jset_N,
                     AAN1,AAN2, totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    # Excluding the k's and j's which are > 0
    DDred, pbaseDDred, dbaseDDred, pbaseB1red, pbaseB2red = prepare_subproblem_basis(DD, pbaseDD, dbaseDD, Kset_0, Jset_N, v1, v2, AAN1, AAN2)

    klist = np.sort(np.append(pbaseDDred[pbaseDDred > 0], dbaseDDred[dbaseDDred > 0]))
    jlist = np.sort(-np.append(pbaseDDred[pbaseDDred < 0], dbaseDDred[dbaseDDred < 0]))

    lk = np.size(klist)
    lj = np.size(jlist)

    # The starting solution
    solution = SCLP_solution(pbaseDDred, dbaseDDred, DDred.copy(), lk, lj, totalK, totalJ)
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
        from .SCLP_pivot7 import SCLP_pivot
        col_info = collision_info('', 0, 0,1,[],v1)
        solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(K_0,J_N,solution,col_info, lk, lj, 1, totalK, totalJ,
                                                    DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 1:
            print('Problem during right pivot...')
            return solution, STEPCOUNT, ITERATION, pivot_problem
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
        from .SCLP_pivot7 import SCLP_pivot
        col_info = collision_info('', 0, -1,0,v2,[])
        solution, STEPCOUNT, ITERATION, pivot_problem  = SCLP_pivot(K_0,J_N,solution,col_info, lk, lj, 1, totalK, totalJ,
                                                    DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 1:
            print('Problem during left pivot...')
            return solution,  STEPCOUNT, ITERATION, pivot_problem

    # prepare the boundaries
    del_q_N, del_x_0, q_N, x_0 = prepare_subproblem_boundaries(DD, pbaseDD, dbaseDD, jlist, klist, lj, lk, v1, v2, AAN1, AAN2)

    param_line = parametric_line(x_0, q_N, klist, jlist, 1, 0, del_x_0, del_q_N)

    #############################################
    # solving the subproblem
    from .SCLP_solver7 import SCLP_solver
    solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 1,'sub_prob', pbaseB1red, pbaseB2red,
                                                     totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance)

    #############################################

    return solution, STEPCOUNT, ITERATION, pivot_problem
