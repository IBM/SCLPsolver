import numpy as np
from .lp_tools.LP_formulation import solve_ratesLP, get_pivot, get_value_by_name, get_dx_names, get_dq_names
from .SCLP_subproblem import SCLP_subproblem
from .pivot_storage import pivot_storage


#'#@profile
def SCLP_pivot(Kset_0, Jset_N, solution, col_info, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    pivot_problem = {'result': 0}
    v1 = col_info.v1
    v2 = col_info.v2
    if col_info.N1 == -1:
        AAN1 = None
        AAN2 = solution.get_basis_at(col_info.N2)
        Jset = get_dq_names(AAN2)
        Kset = Kset_0
        if  not isinstance(v1, list):
            Jset = Jset[Jset!= v1]
            if v1 > 0:
                Kset = Kset_0.copy()
                Kset = np.append(Kset, v1)
        else:
            print('v1',v1)
        new_basis, err = solve_ratesLP(AAN2, Kset, Jset, tolerance)
        pp21 = get_pivot(new_basis, AAN2, True)
        pp22 = get_pivot(new_basis, AAN2, False)
        if np.size(pp21) == 0 and np.size(pp22) == 0:
            print('Basis B2 is optimal')
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, ITERATION, pivot_problem
        piv1 = pivot_storage(pp21.tolist(),pp22.tolist())
    elif col_info.N2 == solution.NN:
        AAN1 = solution.get_basis_at(col_info.N1)
        AAN2 = None
        Kset = get_dx_names(AAN1)
        Jset = [-v for v in Jset_N]
        if not isinstance(v2, list):
            Kset = Kset[Kset!=v2]
            if v2 < 0:
                Jset = np.append(Jset, v2)
        else:
            print('v2', v2)
        new_basis, err = solve_ratesLP(AAN1, Kset, Jset, tolerance)
        pp11 = get_pivot(AAN1, new_basis, True)
        pp12 = get_pivot(AAN1, new_basis, False)
        if np.size(pp11) == 0 and np.size(pp12) == 0:
            pivot_problem['result'] = 1
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
        piv1 = pivot_storage(pp11.tolist(), pp12.tolist())
    else:
        AAN1, AAN2 = solution.get_bases(col_info.N1, col_info.N2)
        if isinstance(v1, list) or isinstance(v2, list):
            vv = get_pivot(AAN1, AAN2, True)
            if isinstance(v2, list):
                v2 = vv
            else:
                v1 = vv
        Kset = get_dx_names(AAN1)
        Kset = Kset[Kset != v2]
        Jset = get_dq_names(AAN2)
        Jset = Jset[Jset != v1]
        new_basis, err = solve_ratesLP(AAN2, Kset, Jset, tolerance)
        pp21 = get_pivot(new_basis, AAN2, True)
        pp22 = get_pivot(new_basis, AAN2, False)
        pp11 = get_pivot(AAN1, new_basis, True)
        pp12 = get_pivot(AAN1, new_basis, False)
        if np.size(pp11) == 0 and np.size(pp12) == 0:
            pivot_problem['result'] = 1
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
        elif np.size(pp21) == 0 and np.size(pp22) == 0:
            print('Basis B2 is optimal')
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, ITERATION, pivot_problem
        piv1 = pivot_storage(pp11.tolist() + pp21.tolist(), pp12.tolist() + pp22.tolist())

    objective = new_basis.simplex_dict[0, 0]
    if objective == np.inf or objective == -np.inf:
        pivot_problem['result'] = 1
        if col_info.N1 == -1:
            print('***  beyond this primal problem is unbounded, dual is infeasible')
            cases = 'unbound_'
        elif col_info.N2 == solution.NN:
            print('***  beyond this primal problem is infeasible, dual is unbounded')
            cases = 'infeas__'
        else:
            print('*** infeasibility in middle of base sequence')
        return solution, STEPCOUNT, ITERATION, pivot_problem

    i1 = 1
    i2 = 1
    if col_info.N1 >= 0:
        i1 = np.size(pp11)
        # check that positive dq not jumping to 0
        if i1 == 1:
            if pp11[0] < 0:
                if get_value_by_name(new_basis, pp11[0], False) > 0:
                    print('Positive dq jumping to 0!')
                    pivot_problem['result'] = 1
                    return solution, STEPCOUNT, ITERATION, pivot_problem
    if col_info.N2 < solution.NN:
        i2 = np.size(pp21)
        # check that positive dx not jumping to 0
        if i2 == 1:
            if pp21[0] > 0:
                if get_value_by_name(new_basis, pp21[0], True) > 0:
                    print('Positive dx jumping to 0!')
                    pivot_problem['result'] = 1
                    return solution, STEPCOUNT, ITERATION, pivot_problem
    if i1 == 1 and i2 == 1:
        solution.update_from_basis(col_info, piv1, AAN1, AAN2, new_basis)
        return solution, STEPCOUNT, ITERATION, pivot_problem
    else:
        sub_solution, STEPCOUNT, ITERATION, pivot_problem =\
         SCLP_subproblem(new_basis, v1, v2, Kset_0, Jset_N, AAN1, AAN2, solution.totalK, solution.totalJ,
                            DEPTH+1, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 0:
            solution.update_from_subproblem(col_info, sub_solution.pivots, AAN1, AAN2)
    return solution, STEPCOUNT, ITERATION, pivot_problem

