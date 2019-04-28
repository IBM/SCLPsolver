import numpy as np


#'#@profile
def calc_statecollide(klist, jlist, state, tolerance):
# Calculates time and variable for which state shrinks to zero, and performs testing
# problem   result = 0  Ok
#           result = 1  immediate collision         data = TODO
#           result = 2  multiple states hit zero    data = TODO
    problem = {'result': 0, 'data': []}

    #TODO: paralellize
    w_x = get_where(state.del_x, True, state.sdx)
    rz_x, bb_x, kk_x, nn_x = calc_rz_bb(state.x, state.del_x, w_x)
    ###
    w_q = get_where(state.del_q, False, state.sdq)
    rz_q, bb_q, kk_q, nn_q = calc_rz_bb(state.q, state.del_q, w_q)
    #end
    if bb_x > bb_q:
        if bb_x == 0:
            print(kk_x, nn_x)
            return [np.inf, 0, 0], problem
        else:
            test1 = 1. / bb_x
            if test1 <= -tolerance:
                return [], problem
            elif abs(test1) < tolerance:
                print('immediate collision\n')
                problem['result'] = 1
                return [], problem
            else:                    # test1 >= tolerance
                nn = nn_x - 1
                vv = klist[kk_x]
                bb = bb_x
    else:
        if bb_q == 0:
            print(kk_q, nn_q)
            return [np.inf, 0, 0], problem
        else:
            test1 = 1. / bb_q
            if test1 <= -tolerance:
                return [], problem
            elif abs(test1) < tolerance:
                print('immediate collision\n')
                problem['result'] = 1
                return [], problem
            else:                   # test1 >= tolerance
                nn = nn_q - 1
                vv = -jlist[kk_q]
                bb = bb_q
    # TODO: paralellize
    test2 = np.add(np.divide(rz_x, bb, where=w_x), -1.0, where=w_x)
    zstates = np.less(np.fabs(test2, where=w_x), tolerance, where = w_x, out=w_x)
    sz_x = np.sum(zstates)
    ###
    test2 = np.add(np.divide(rz_q, bb, where=w_q), -1.0, where=w_q)
    zstates = np.less(np.fabs(test2, where=w_q), tolerance, where = w_q, out=w_q)
    sz_q = np.sum(zstates)
    #end
    if sz_x + sz_q > 1:
        print('multiple states hit zero\n')
        problem['result'] = 2
        return [test1, nn, vv], problem
    else:
        return [test1, nn, vv], problem

#'#@profile
def calc_rz_bb(state, del_state, w):
    rz = np.divide(-del_state, state, out=np.zeros_like(del_state), where=w)
    kk, nn = np.unravel_index(rz.argmax(), rz.shape)
    bb = rz[kk, nn]
    return rz, bb, kk, nn


#'#@profile
def get_where(del_state, is_primal, sd):
    if is_primal:
        locmin_state = np.logical_and( (sd==1)[:,1:],(sd==-1)[:,:-1])
    else:
        locmin_state = np.logical_and((sd == 1)[:, :-1], (sd == -1)[:, 1:])
    np.logical_and(del_state < 0, locmin_state, out=locmin_state)
    return locmin_state
