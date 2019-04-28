import numpy as np
from .LP_formulate5 import LP_formulate
from .SCLP_subproblem8 import SCLP_subproblem
from .pivot_storage import pivot_storage


#'#@profile
def SCLP_pivot(Kset_0, Jset_N, solution, col_info, DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    pivot_problem = {'result': 0}
    v1 = col_info.v1
    v2 = col_info.v2
    if col_info.N1 == -1:
        AAN1 = None
        AAN2 = solution.get_basis_at(col_info.N2)
        BB2 = AAN2['A']
        pbaseB2 = AAN2['prim_name']
        dbaseB2 = AAN2['dual_name']
        Jset = dbaseB2[dbaseB2 < 0]
        Kset = Kset_0
        if  not isinstance(v1, list):
            Jset = Jset[Jset!= v1]
            if v1 > 0:
                Kset = np.append(Kset, v1)
        else:
            print('v1',v1)
        pbaseDD, dbaseDD, DD = LP_formulate(BB2, pbaseB2, dbaseB2, Kset, Jset, tolerance)
        pp21 = np.setdiff1d(pbaseDD, pbaseB2, assume_unique=True)
        pp22 = np.setdiff1d(dbaseDD, dbaseB2, assume_unique=True)
        #piv1 = [pp21.tolist()+pp22.tolist()]
        piv1 = pivot_storage(pp21.tolist(),pp22.tolist())
        if np.size(pp21) == 0 and np.size(pp22) == 0:
            print('Basis B2 is optimal')
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, ITERATION, pivot_problem
    elif col_info.N2 == solution.NN:
        AAN1 = solution.get_basis_at(col_info.N1)
        AAN2 = None
        BB1 = AAN1['A']
        pbaseB1 = AAN1['prim_name']
        dbaseB1 = AAN1['dual_name']
        Kset = pbaseB1[pbaseB1 > 0]
        Jset = [-v for v in Jset_N]
        if not isinstance(v2, list):
            Kset = Kset[Kset!=v2]
            if v2 < 0:
                Jset = np.append(Jset, v2)
        else:
            print('v2', v2)
        pbaseDD, dbaseDD, DD = LP_formulate(BB1, pbaseB1, dbaseB1, Kset, Jset, tolerance)
        pp11 = np.setdiff1d(pbaseB1, pbaseDD, assume_unique=True)
        pp12 = np.setdiff1d(dbaseB1, dbaseDD, assume_unique=True)
        #piv1 = [pp11.tolist()+ pp12.tolist()]
        piv1 = pivot_storage(pp11.tolist(), pp12.tolist())
        if np.size(pp11) == 0 and np.size(pp12) == 0:
            pivot_problem['result'] = 1
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
    else:
        AAN1, AAN2 = solution.get_bases(col_info.N1, col_info.N2)
        BB2 = AAN2['A']
        pbaseB1 = AAN1['prim_name']
        dbaseB1 = AAN1['dual_name']
        pbaseB2 = AAN2['prim_name']
        dbaseB2 = AAN2['dual_name']

        if isinstance(v1, list) or isinstance(v2, list):
            vv =np.setdiff1d(pbaseB1, pbaseB2, assume_unique=True)
            if isinstance(v2, list):
                v2 = vv
            else:
                v1 = vv
        Kset = pbaseB1[pbaseB1 > 0]
        Kset = Kset[Kset != v2]
        Jset = dbaseB2[dbaseB2 < 0]
        Jset = Jset[Jset != v1]
        pbaseDD, dbaseDD, DD = LP_formulate(BB2, pbaseB2, dbaseB2, Kset, Jset, tolerance)
        pp21 = np.setdiff1d(pbaseDD, pbaseB2, assume_unique=True)
        pp22 = np.setdiff1d(dbaseDD, dbaseB2, assume_unique=True)
        pp11 = np.setdiff1d(pbaseB1, pbaseDD, assume_unique=True)
        pp12 = np.setdiff1d(dbaseB1, dbaseDD, assume_unique=True)
        piv1 = pivot_storage(pp11.tolist() + pp21.tolist(), pp12.tolist()  + pp22.tolist())
        if np.size(pp11) == 0 and np.size(pp12) == 0:
            pivot_problem['result'] = 1
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
        elif np.size(pp21) == 0 and np.size(pp22) == 0:
            print('Basis B2 is optimal')
            pivot_problem['result'] = 1
            return solution, STEPCOUNT, ITERATION, pivot_problem
        #piv1 = [pp11.tolist()+ pp12.tolist(),pp21.tolist()+ pp22.tolist()]
    objective = DD[0, 0]

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
                if DD[0, 1:][dbaseDD == pp11[0]][0] > 0:
                    print('Positive dq jumping to 0!')
                    pivot_problem['result'] = 1
                    return solution, STEPCOUNT, ITERATION, pivot_problem
    if col_info.N2 < solution.NN:
        i2 = np.size(pp21)
        # check that positive dx not jumping to 0
        if i2 == 1:
            if pp21[0] > 0:
                if DD[1:, 0][pbaseDD == pp21[0]][0] > 0:
                    print('Positive dx jumping to 0!')
                    pivot_problem['result'] = 1
                    return solution, STEPCOUNT, ITERATION, pivot_problem
    if i1 == 1 and i2 == 1:
        solution.update_from_basis(col_info, piv1, AAN1, AAN2, pbaseDD, dbaseDD, DD)
        return solution, STEPCOUNT, ITERATION, pivot_problem
    else:
        sub_solution, STEPCOUNT, ITERATION, pivot_problem =\
         SCLP_subproblem(pbaseDD, dbaseDD, DD, v1, v2, Kset_0, Jset_N, AAN1, AAN2, solution.totalK, solution.totalJ,
                            DEPTH+1, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 0:
            solution.update_from_subproblem(col_info, sub_solution.pivots, AAN1, AAN2)
    return solution, STEPCOUNT, ITERATION, pivot_problem

