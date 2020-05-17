import numpy as np
from .lp_tools.LP_formulation import solve_ratesLP, get_value_by_name, get_dx_names, get_dq_names, solve_simple_caseII
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
                Kset = np.append(Kset, v1).astype(np.int32)
        else:
            print('v1',v1)
        new_basis, lp_pivots, err = solve_ratesLP(AAN2, Kset, Jset, solution.bases_mm, tolerance)
        pp21 = lp_pivots.in_
        pp22 = lp_pivots.out_
        if len(pp21) == 0 and len(pp22) == 0:
            print('Basis B2 is optimal')
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, ITERATION, pivot_problem
        piv1 = pivot_storage(list(pp21), list(pp22))
    elif col_info.N2 == solution.NN:
        AAN1 = solution.get_basis_at(col_info.N1)
        AAN2 = None
        Kset = get_dx_names(AAN1)
        Jset = -Jset_N.copy()
        if not isinstance(v2, list):
            Kset = Kset[Kset!=v2]
            if v2 < 0:
                Jset = np.append(Jset, v2)
        else:
            print('v2', v2)
        new_basis, lp_pivots, err = solve_ratesLP(AAN1, Kset, Jset, solution.bases_mm, tolerance)
        pp11 = lp_pivots.out_
        pp12 = lp_pivots.in_
        if len(pp11) == 0 and len(pp12) == 0:
            pivot_problem['result'] = 1
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
        piv1 = pivot_storage(list(pp11), list(pp12))
    else:
        AAN1, AAN2 = solution.get_bases(col_info.N1, col_info.N2)
        #this for the collusion case III
        if isinstance(v1, list) or isinstance(v2, list):
            #vv = get_pivot(AAN1, AAN2, True)
            vv = solution.pivots.outpivots[col_info.N1]
            out_diff = {vv}
            if isinstance(v2, list):
                v2 = vv
            else:
                v1 = vv
        else:
            out_diff = {v1, v2}
        Kset = get_dx_names(AAN1)
        Kset = Kset[Kset != v2]
        Jset = get_dq_names(AAN2)
        Jset = Jset[Jset != v1]
        in_diff = solution.pivots.get_in_difference(col_info.N1,col_info.N2)
        if col_info.N2 - col_info.N1 == 2:
            in_diff_list = list(in_diff)
            ok, new_basis, lp_pivots, err = solve_simple_caseII(AAN2, Kset, Jset, solution.bases_mm, v1, in_diff_list)
            if ok == 1:
                in_diff_list.remove(lp_pivots[1])
                piv1 = pivot_storage([v2, v1], in_diff_list + [lp_pivots[1]])
                solution.update_from_basis(col_info, piv1, AAN1, AAN2, new_basis)
                return solution, STEPCOUNT, ITERATION, pivot_problem
        else:
            new_basis, lp_pivots, err = solve_ratesLP(AAN2, Kset, Jset, solution.bases_mm, tolerance)
        # new_basis, lp_pivots, err = solve_ratesLP(AAN2, Kset, Jset, solution.bases_mm, tolerance)
        # if col_info.N2 - col_info.N1 == 2:
        #     in_diff_list = list(in_diff)
        #     ok, prim_vars, dual_vars, i, j = partial_solve_caseII(AAN2, Kset, Jset, solution.bases_mm, v1, in_diff_list)
        #     if ok == 0:
        #         new_basis, lp_pivots, err = solve_ratesLP(AAN2, Kset, Jset, solution.bases_mm, tolerance, build_sign=False)
        #     else:
        #         prim_name, dual_name = AAN2.prim_name.copy(), AAN2.dual_name.copy()
        #         in_diff_list.remove(prim_name[i])
        #         piv1 = pivot_storage([v2, v1], in_diff_list + [prim_name[i]])
        #         tmp = dual_name[j]
        #         dual_name[j] = prim_name[i]
        #         prim_name[i] = tmp
        #         solution.update_from_partial(col_info, piv1, AAN1, AAN2, prim_vars, dual_vars, prim_name, dual_name)
        #         return solution, STEPCOUNT, ITERATION, pivot_problem
        # else:
        #     new_basis, lp_pivots, err = solve_ratesLP(AAN2, Kset, Jset, solution.bases_mm, tolerance)
        #new_basis, lp_pivots, err = solve_ratesLP(AAN2, Kset, Jset, solution.bases_mm, tolerance)
        pp21 = lp_pivots.in_.copy()
        pp22 = lp_pivots.out_.copy()
        #instead of solution.pivots.get_out_difference
        # if out_diff != solution.pivots.get_out_difference(col_info.N1, col_info.N2):
        #     print('aaa')
        lp_pivots.extr(out_diff, set(in_diff))
        pp11 = lp_pivots.in_
        pp12 = lp_pivots.out_
        if len(pp11) == 0 and len(pp12) == 0:
            pivot_problem['result'] = 1
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
        elif len(pp21) == 0 and len(pp22) == 0:
            print('Basis B2 is optimal')
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, ITERATION, pivot_problem
        piv1 = pivot_storage(list(pp11) + list(pp21), list(pp12) + list(pp22))

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
        i1 = len(pp11)
        # check that positive dq not jumping to 0
        if i1 == 1:
            v = pp11.pop()
            if v < 0:
                if get_value_by_name(new_basis, v, False) > 0:
                    print('Positive dq jumping to 0!')
                    pivot_problem['result'] = 1
                    return solution, STEPCOUNT, ITERATION, pivot_problem
    if col_info.N2 < solution.NN:
        i2 = len(pp21)
        # check that positive dx not jumping to 0
        if i2 == 1:
            v = pp21.pop()
            if v > 0:
                if get_value_by_name(new_basis, v, True) > 0:
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

