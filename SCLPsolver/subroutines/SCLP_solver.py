from .classification import classification
from .SCLP_pivot import SCLP_pivot
from .collision_info import collision_info
from .time_collision_resolver import reclassify, reclassify_ztau

#'#@profile
def SCLP_solver(solution, param_line, case, DEPTH, STEPCOUNT, ITERATION, settings, tolerance, find_alt_line=True, mm=None):

    ITERATION[DEPTH] = 0

    col_info = collision_info(case)
    pivot_problem = {'result': 0}
    solution.print_short_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], 0, 0, case)
    solution.clear_collision_stack()
    rewind_required = False


    while True:

        # if not solution.base_sequence.check_places():
        #     raise Exception('Bases placement failure!')
        if not rewind_required:
            res = solution.update_state(param_line, settings.check_intermediate_solution, tolerance*100)
            if not res:
                return solution, STEPCOUNT, {'result': 1}
            if solution.check_if_complete(param_line):
                solution.print_short_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], param_line.theta, param_line.theta, 'complete')
                return solution, STEPCOUNT, pivot_problem
            col_info, problem = classification(solution, tolerance)
            if problem['result'] > 0:
                ztau_ind = solution.get_ztau_ind()
                if ztau_ind is not None:
                    new_col_info = reclassify_ztau(col_info, solution, ztau_ind, tolerance, DEPTH>0)
                    if new_col_info is None:
                        rewind_required = True
                    else:
                        col_info = new_col_info
                        rewind_required = False
                else:
                    rewind_required = True
                # if solution.last_collision.case == 'Case iii':
                #     ztau_ind = solution.get_ztau_ind()
                #     if ztau_ind is not None:
                #         new_col_info = reclassify_ztau(col_info, solution, ztau_ind, tolerance)
                #         if new_col_info is None:
                #             rewind_required = True
                #         else:
                #             col_info = new_col_info
                #             rewind_required = False
                #     else:
                #         rewind_required = True
                # else:
                #     rewind_required = True
            else:
                rewind_required = False

        if rewind_required:
            if DEPTH == 0:
                lastCollision = solution.update_rewind()
                resolved = False
                up_theta = param_line.theta + col_info.delta + 0.04
                while lastCollision is not None:
                    # rewinding to previous iteration
                    print('rewind... ')
                    param_line.backward_to(lastCollision.delta)
                    res = solution.update_state(param_line, settings.check_intermediate_solution, tolerance*10)
                    if not res:
                        return solution, STEPCOUNT, {'result': 1}
                    solution.print_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], param_line.theta, lastCollision)
                    col_info, resolved = reclassify(lastCollision, solution, tolerance)
                    if not resolved:
                        lastCollision = solution.update_rewind()
                    else:
                        break
                if not resolved:
                    if find_alt_line and not param_line.is_orthogonal() and param_line.theta > 0:
                        print('Unable to rewind... Trying to outflank!')
                        param_line.forward_to(col_info.delta)
                        main_theta_bar = param_line.theta_bar
                        param_line.theta_bar = param_line.theta - 0.02 - col_info.delta
                        print('Going backward by:', 0.02)
                        solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 'start', DEPTH,
                                                                         STEPCOUNT,
                                                                         ITERATION, settings, tolerance, mm=mm)
                        ort_line = param_line.get_orthogonal_line(0.04)
                        print('Going orthogonal to:', ort_line.theta_bar)
                        solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, ort_line, 'start', DEPTH, STEPCOUNT, ITERATION, settings, tolerance, mm=mm)
                        if pivot_problem['result'] == 1:
                            print('Problem during orthogonal step!')
                        param_line.theta_bar = up_theta
                        print('Going forward to:', up_theta)
                        solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, param_line, 'start', DEPTH, STEPCOUNT,
                                                                         ITERATION, settings, tolerance, mm=mm)
                        ort_line.theta_bar = 0
                        ort_line.T = param_line.T
                        print('Returning to main line.')
                        #update T before going forward
                        solution, STEPCOUNT, pivot_problem = SCLP_solver(solution, ort_line, 'start', DEPTH, STEPCOUNT,
                                                                         ITERATION, settings, tolerance, mm=mm)
                        param_line.theta_bar = max(main_theta_bar,param_line.T)
                        if pivot_problem['result'] == 1:
                            print('Problem during orthogonal step!')
                            return solution, STEPCOUNT, pivot_problem
                        rewind_required = False
                        continue
                    else:
                        pivot_problem['result'] = 1
                        return solution, STEPCOUNT, pivot_problem
            else:
                pivot_problem = {'result':1}
                print('Rewind in subproblem not supported. Returning to main problem!')
                return solution, STEPCOUNT, pivot_problem

        if DEPTH == 0 and param_line.is_end(col_info.delta):
            col_info.case = 'solved__'
            solution.print_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], param_line.theta, col_info)
            param_line.forward_to_end()
            return solution, STEPCOUNT, pivot_problem

        STEPCOUNT = STEPCOUNT + 1
        ITERATION[DEPTH] = ITERATION[DEPTH] + 1

        if settings.max_iteration is not None:
            if DEPTH == 0 and ITERATION[DEPTH] >= settings.max_iteration:
                return solution, STEPCOUNT, pivot_problem

        solution.print_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], param_line.theta, col_info)

        if DEPTH > 0 and param_line.is_end(col_info.delta):
            print("Theta > 1....")
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, pivot_problem

        if col_info.case == 'Case i__':
            solution.update_caseI(col_info)
            rewind_required = False
        elif col_info.case == 'Case ii_' or col_info.case == 'Case iii':
            solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(param_line.Kset_0, param_line.Jset_N, solution,
                                                                       col_info, DEPTH, STEPCOUNT, ITERATION, settings,
                                                                       tolerance)
            # try:
            #     solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(param_line.Kset_0, param_line.Jset_N, solution,
            #                                                            col_info, DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
            # except Exception as ex:
            #     print('Exception during SCLP pivot:')
            #     print(ex)
            #     return solution, STEPCOUNT, {'result': 1}
            while pivot_problem['result'] == 1: # theta > 1
                print('Pivot problem: trying to resolve * ', col_info.tol_coeff, '...')
                new_col_info, resolved = reclassify(col_info, solution, tolerance)
                if resolved:
                    print('resolved!')
                    col_info = new_col_info
                    solution.print_status(STEPCOUNT, DEPTH, ITERATION[DEPTH], param_line.theta, col_info)
                    if col_info.case == 'Case i__':
                        solution.update_caseI(col_info)
                        pivot_problem['result'] = 0
                    elif col_info.case == 'Case ii_' or col_info.case == 'Case iii':
                        try:
                            solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(param_line.Kset_0, param_line.Jset_N, solution,
                                                                           col_info, DEPTH, STEPCOUNT, ITERATION, settings, tolerance)
                        except Exception as ex:
                            print('Exception during SCLP pivot:')
                            print(ex)
                            return solution, STEPCOUNT, {'result': 1}
                else:
                    break
            if pivot_problem['result'] == 1:
                if DEPTH > 0:
                    return solution, STEPCOUNT, pivot_problem
                else:
                    rewind_required = True
            else:
                rewind_required = False

        if not rewind_required:
            param_line.forward_to(col_info.delta)
            if DEPTH == 0:
                if mm is not None:
                    solution.clear_base_sequence(mm)

    return solution, STEPCOUNT, pivot_problem

