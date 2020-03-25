from .generic_SCLP_solution import generic_SCLP_solution
from .parametric_line import parametric_line
from .prepare_subproblem_data import prepare_subproblem_basis
from .collision_info import collision_info

#'#@profile
def SCLP_subproblem(new_basis, v1,v2,Kset_0, Jset_N,
                     AAN1,AAN2, totalK, totalJ, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    # Excluding the k's and j's which are > 0
    rates_LP_form, pbaseB1red, pbaseB2red = prepare_subproblem_basis(new_basis, Kset_0, Jset_N, v1, v2, AAN1, AAN2)
    # The starting solution
    solution = generic_SCLP_solution(rates_LP_form, totalK=totalK, totalJ=totalJ)
    # performing the left and right first pivots
    #		the right pivot:
    K_0 = []
    J_N = []
    if pbaseB2red is not None:
        if not isinstance(v1, list):
            if v1 > 0:
                K_0 = [v1]
            else:
                J_N = [-v1]
        if not isinstance(v2, list):
            if v2 < 0:
                J_N.append(-v2)
        from .SCLP_pivot import SCLP_pivot
        col_info = collision_info('', 0, 0,1,[],v1)
        solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(K_0,J_N,solution,col_info, DEPTH, STEPCOUNT,
                                                                   ITERATION, settings, tolerance)
        if pivot_problem['result'] == 1:
            print('Problem during right pivot...')
            return solution, STEPCOUNT, ITERATION, pivot_problem
    #		the left pivot:
    K_0 = []
    J_N = []
    if pbaseB1red is not None:
        if not isinstance(v2, list):
            if v2 > 0:
                K_0 = [v2]
            else:
                J_N = [-v2]
        if not isinstance(v1, list):
            if v1 > 0:
                K_0.append(v1)
        from .SCLP_pivot import SCLP_pivot
        col_info = collision_info('', 0, -1,0,v2,[])
        solution, STEPCOUNT, ITERATION, pivot_problem  = SCLP_pivot(K_0,J_N,solution,col_info, DEPTH, STEPCOUNT,
                                                                    ITERATION, settings, tolerance)
        if pivot_problem['result'] == 1:
            print('Problem during left pivot...')
            return solution,  STEPCOUNT, ITERATION, pivot_problem

    # prepare the boundaries
    param_line = parametric_line.get_subproblem_parametric_line(new_basis, solution, v1, v2, AAN1, AAN2, pbaseB1red, pbaseB2red)

    #############################################
    # solving the subproblem
    from .SCLP_solver import SCLP_solver
    solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 'sub_prob', DEPTH, STEPCOUNT, ITERATION, settings, tolerance)

    #############################################

    return solution, STEPCOUNT, ITERATION, pivot_problem
