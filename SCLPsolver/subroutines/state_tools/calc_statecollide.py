import numpy as np
from .state_tools import get_rz_bb


#'#@profile
def calc_statecollide(klist, jlist, state, loc_min, tolerance):
# Calculates time and variable for which state shrinks to zero, and performs testing
# problem   result = 0  Ok
#           result = 1  immediate collision         data = TODO
#           result = 2  multiple states hit zero    data = TODO
    problem = {'result': 0, 'data': []}

    #TODO: paralellize
    bb_x, kk_x, nn_x = get_rz_bb(state.del_x[:, 1:], state.x[:, 1:], loc_min.dx_min.data, loc_min.dx_min.sizes)
    ###
    bb_q, kk_q, nn_q = get_rz_bb(state.del_q[:, :-1], state.q[:, :-1], loc_min.dq_min.data, loc_min.dq_min.sizes)
    #end
    if bb_x > bb_q:
        if bb_x == 0:
            print(kk_x, nn_x)
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
            print(kk_q, nn_q)
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
    # TODO: paralellize
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

