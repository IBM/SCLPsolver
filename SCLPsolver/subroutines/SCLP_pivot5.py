import numpy as np
from .LP_formulate5 import LP_formulate
from .extract_rates5 import extract_rates
from .SCLP_subproblem5 import SCLP_subproblem
from .pivot_storage import pivot_storage


#'#@profile
def SCLP_pivot(Kset_0, Jset_N, solution, N1, N2, v1, v2, KK, JJ, NN, totalK, totalJ,
               DEPTH, STEPCOUNT, ITERATION, settings, tolerance):

    pivot_problem = {'result': 0}
    if N1 == -1:
        pbaseB1 = np.array([])
        AAN1 = None
        AAN2 = solution.get_basis_at(N2)
        BB2 = AAN2['A']
        pbaseB2 = AAN2['prim_name']
        dbaseB2 = AAN2['dual_name']
        Jset = dbaseB2[dbaseB2 < 0]
        Kset = Kset_0
        if  not isinstance(v1, list):
            Jset = Jset[Jset!=v1]
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
            return solution, STEPCOUNT, ITERATION, pivot_problem
    elif N2 == NN:
        pbaseB2 = np.array([])
        AAN1 = solution.get_basis_at(N1)
        AAN2 = None
        BB1 = AAN1['A']
        pbaseB1 = AAN1['prim_name']
        dbaseB1 = AAN1['dual_name']
        dbaseB2 = np.array([])
        Kset = pbaseB1[pbaseB1 > 0]
        Jset = [-v for v in Jset_N]
        if not isinstance(v2, list):
            Kset = Kset[Kset!=v2]
            if v2 < 0:
                Jset = np.append(Jset, -v2)
        else:
            print('v2', v2)
        pbaseDD, dbaseDD, DD = LP_formulate(BB1, pbaseB1, dbaseB1, Kset, Jset, tolerance)
        pp11 = np.setdiff1d(pbaseB1, pbaseDD, assume_unique=True)
        pp12 = np.setdiff1d(dbaseB1, dbaseDD, assume_unique=True)
        #piv1 = [pp11.tolist()+ pp12.tolist()]
        piv1 = pivot_storage(pp11.tolist(), pp12.tolist())
        if np.size(pp11) == 0 and np.size(pp12) == 0:
            print('Basis B1 is optimal')
            return solution, STEPCOUNT, ITERATION, pivot_problem
    else:
        AAN1, AAN2 = solution.get_bases(N1, N2)
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
        #piv1 = [pp11.tolist()+ pp12.tolist(),pp21.tolist()+ pp22.tolist()]
    objective = DD[0, 0]

    if objective == np.inf or objective == -np.inf:
        if N1 == -1:
            print('***  beyond this primal problem is unbounded, dual is infeasible')
            cases = 'unbound_'
        elif N2 == NN:
            print('***  beyond this primal problem is infeasible, dual is unbounded')
            cases = 'infeas__'
        else:
            raise Exception('*** infeasibility in middle of base sequence')
        return solution, STEPCOUNT, ITERATION, pivot_problem

    i1 = 1
    i2 = 1
    if N1 >= 0:
        i1 = np.size(pp11)
    if N2 < NN:
        i2 = np.size(pp21)
    if i1 == 1 and i2 == 1:
        dx, dq = extract_rates(pbaseDD, dbaseDD, DD, KK, JJ, totalK, totalJ)
        solution.update_caseII(N1, N2, np.reshape(pbaseDD,(-1,1)), np.reshape(dbaseDD,(-1,1)), dx, dq, AAN1, AAN2, piv1, 1, {'prim_name': pbaseDD, 'dual_name': dbaseDD, 'A': DD})
        return solution, STEPCOUNT, ITERATION, pivot_problem
    else:
        if N1 == -1:
            Kex1 =  np.intersect1d(pbaseDD[pbaseDD > 0], Kset_0, assume_unique=True)
            Kexclude =  np.intersect1d(Kex1, pbaseB2[pbaseB2 > 0], assume_unique=True)
            Jexclude = -np.intersect1d(dbaseDD[dbaseDD < 0], dbaseB2[dbaseB2 < 0], assume_unique=True)
        elif N2 == NN:
            Kexclude =  np.intersect1d(pbaseDD[pbaseDD > 0], pbaseB1[pbaseB1 > 0], assume_unique=True)
            Jex1 =  np.intersect1d(dbaseDD[dbaseDD < 0], [-v for v in Jset_N], assume_unique=True)
            Jexclude = -np.intersect1d(Jex1, dbaseB1[dbaseB1 < 0], assume_unique=True)
        else:
            Kexclude =  np.intersect1d(pbaseB1[pbaseB1 > 0], pbaseB2[pbaseB2 > 0], assume_unique=True)
            Jexclude = -np.intersect1d(dbaseB1[dbaseB1 < 0], dbaseB2[dbaseB2 < 0], assume_unique=True)
            if not isinstance(v1, list):
                Kexclude = Kexclude[Kexclude != v1]
                Jexclude = Jexclude[Jexclude != -v1]
            if not isinstance(v2, list):
                Kexclude = Kexclude[Kexclude != v2]
                Jexclude = Jexclude[Jexclude != -v2]
        prim_name, dual_name, dx, dq, pivots, Nnew, STEPCOUNT, ITERATION, pivot_problem =\
         SCLP_subproblem(pbaseDD, dbaseDD, DD, N1, N2, v1, v2, Kexclude, Jexclude, pbaseB1, pbaseB2, AAN1, AAN2, KK, JJ,
                            NN, totalK, totalJ, DEPTH+1, STEPCOUNT, ITERATION, settings, tolerance)
        if pivot_problem['result'] == 0:
            solution.update_caseII(N1, N2, prim_name, dual_name, dx, dq, AAN1, AAN2, pivots, Nnew)
    return solution, STEPCOUNT, ITERATION, pivot_problem

