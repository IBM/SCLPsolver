import numpy as np
from .state_tools import get_rz_bb
from .state_collide import calc_state_ratio_prim, calc_state_ratio_dual

#'#@profile
def calc_statecollide(klist, jlist, state, raw_dx, raw_dq, param_line, loc_min, has_no_state, tolerance):
    # Calculates time and variable for which state shrinks to zero, and performs testing
    # problem   result = 0  Ok
    #           result = 1  immediate collision         data = TODO
    #           result = 2  multiple states hit zero    data = TODO
    problem = {'result': 0, 'data': []}

    #TODO: paralellize?
    if has_no_state:
        bb_x, kk_x, nn_x = calc_state_ratio_prim(raw_dx[0], raw_dx[1], raw_dx[2], state.tau, state.dtau, param_line.x_0,
                                           param_line.del_x_0, loc_min.dx_min.data, loc_min.dx_min.sizes, state.del_x, state.x, 0)
        bb_q, kk_q, nn_q = calc_state_ratio_dual(raw_dq[0], raw_dq[1], raw_dq[2], state.tau, state.dtau, param_line.q_N,
                                           param_line.del_q_N, loc_min.dq_min.data, loc_min.dq_min.sizes, state.del_q, state.q, 0)
    else:
        bb_x, kk_x, nn_x = get_rz_bb(state.del_x[:, 1:], state.x[:, 1:], loc_min.dx_min.data, loc_min.dx_min.sizes)
        bb_q, kk_q, nn_q = get_rz_bb(state.del_q[:, :-1], state.q[:, :-1], loc_min.dq_min.data, loc_min.dq_min.sizes)
    if bb_x > bb_q:
        if bb_x == 0:
            #print(kk_x, nn_x)
            return [np.inf, 0, 0], problem
        else:
            test1 = 1. / bb_x
            #nn = nn_x - 1 #because we have no x_0
            nn = nn_x
            vv = klist[kk_x]
            if test1 <= -tolerance:
                return [], problem
            elif abs(test1) < tolerance:
                print('immediate collision',nn,vv)
                problem['result'] = 1
                return [test1, nn, vv], problem
            else:                    # test1 >= tolerance
                bb = bb_x
    else:
        if bb_q == 0:
            #print(kk_q, nn_q)
            return [np.inf, 0, 0], problem
        else:
            nn = nn_q - 1
            vv = -jlist[kk_q]
            test1 = 1. / bb_q
            if test1 <= -tolerance:
                return [], problem
            elif abs(test1) < tolerance:
                print('immediate collision',nn,vv)
                problem['result'] = 1
                return [test1, nn, vv], problem
            else:                   # test1 >= tolerance
                bb = bb_q
    # TODO: this check now impossible
    # test2 = np.add(np.divide(rz_x, bb, where=w_x), -1.0, where=w_x)
    # zstates = np.less(np.fabs(test2, where=w_x), tolerance, where = w_x, out=w_x)
    # sz_x = np.sum(zstates)
    # ###
    # test2 = np.add(np.divide(rz_q, bb, where=w_q), -1.0, where=w_q)
    # zstates = np.less(np.fabs(test2, where=w_q), tolerance, where = w_q, out=w_q)
    # sz_q = np.sum(zstates)
    # #end
    # if sz_x + sz_q > 1:
    #     print('multiple states hit zero\n')
    #     problem['result'] = 2
    #     return [test1, nn, vv], problem
    # else:
    return [test1, nn, vv], problem

