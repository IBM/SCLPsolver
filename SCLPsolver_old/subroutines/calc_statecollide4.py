import numpy as np


def calc_statecollide(klist, jlist, x, del_x, q, del_q, sdx, sdq, tolerance):
# Calculates time and variable for which state shrinks to zero, and performs testing
# problem   result = 0  Ok
#           result = 1  immediate collision         data = TODO
#           result = 2  multiple states hit zero    data = TODO
    problem = {'result': 0, 'data': []}

    KK = len(klist)
    JJ = len(jlist)
    #TODO: paralellize
    rz_x = calc_rz(KK, x, del_x, sdx, True)
    rz_q = calc_rz(JJ, q, del_q, sdq, False)
    #end

    rz = np.vstack((rz_x,rz_q))
    if np.all(np.isnan(rz)):
        return [], problem

    kk, nn = np.unravel_index(rz.argmax(), rz.shape)
    bb = rz[kk,nn]
    if bb == 0:
        print(kk, nn)
        test1 = np.inf
        nn=1
        vv=0
    else:
        #kk = find(rz(:, nn) == bb); %
        test1 =1./bb
        if test1 <= -tolerance:
            return [], problem
        elif abs(test1) < tolerance:
            print('immediate collision\n')
            problem['result'] = 1
            return [], problem
        elif test1 >= tolerance:
            test2 = rz/bb - 1
            zstates = np.fabs(test2) < tolerance
            if np.sum(zstates) > 1:
                print('multiple states hit zero\n')
                problem['result'] = 2
                return [], problem
        all_names = np.hstack((klist, -jlist))
        vv = all_names[kk]
    return [test1, nn - 1, vv], problem


def calc_rz(vdim, state, del_state, sd, is_primal = True):
    if is_primal:
        locmin_state = np.asarray(np.logical_and(np.hstack((sd == 1, np.full((vdim, 1), True))),
                                  np.hstack((np.full((vdim, 1), False), sd == -1))))
    else:
        locmin_state = np.asarray(np.logical_and(np.hstack((sd == -1, np.full((vdim, 1), False))),
                                  np.hstack((np.full((vdim, 1), True), sd == 1))))
    w = np.logical_and(del_state < 0, locmin_state)
    # TODO: paralellize
    # test_val = state[locmin_state]
    # test_dval = del_state[locmin_state]
    # end
    xxx = np.any(np.equal(state,np.zeros_like(state),out = np.full_like(state, False), where=w))
    if xxx:
        print(np.where(np.equal(state,np.zeros_like(state), out = np.full_like(state, False), where=w)))
    rz = np.divide(-del_state, state, out=np.zeros_like(del_state), where=w)
    # res = np.zeros(locmin_state.shape)
    # res[locmin_state] = rz
    return rz
