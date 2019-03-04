import numpy as np
from multiprocessing import Process, Value, Array


#'#@profile
def calc_states(dx,dq,x_0,del_x_0,q_N,del_q_N,tau,dtau,sdx, sdq, tolerance):
    K1, N1  = dx.shape
    if K1 == 0:
        x = np.zeros((0, N1 + 1))
        del_x = np.zeros((0, N1 + 1))
    else:
        # x = Array('d',K1 * (N1 + 1))
        # del_x = Array('d',K1 * (N1 + 1))
        # K1 = Value('d', K1)
        # x_0 = Array('d', x_0)
        # p = Process(target=calc_prim_states, args=())
        x = np.zeros((K1, N1 + 1))
        del_x = np.zeros((K1, N1 + 1))

    J1 = dq.shape[0]
    if J1 == 0:
        q = np.zeros((0,N1+1))
        del_q = np.zeros((0,N1+1))
    else:
        q = np.zeros((J1, N1 + 1))
        del_q = np.zeros((J1, N1 + 1))
    # TODO: parallelize
    _calc_states(x, del_x, K1, x_0, del_x_0, tau, dtau, dx, sdx, tolerance, True)
    _calc_states(q, del_q, J1, q_N, del_q_N, tau, dtau, dq, sdq, tolerance, False)
    return x, del_x, np.fliplr(q), np.fliplr(del_q)


#'#@profile
def _calc_states(state, del_state, vdim, state0, del_state0, tau, dtau, dstate, sdstate, tolerance, is_primal):
    if vdim > 0:
        sstate = sdstate == 0
        #sdstate = np.logical_or(np.hstack((np.full((vdim, 1), False), sdstate)), np.hstack((sdstate, np.full((vdim, 1), False))))
        sdstate = np.logical_or(sstate[:,:-1],sstate[:,1:])
        if is_primal:
            #TODO: parallelize
            _calc_primal(state, dstate, tau, state0, sdstate, tolerance)
            _calc_primal(del_state, dstate, dtau, del_state0, sdstate, tolerance)
        else:
            # TODO: parallelize
            _calc_dual(state, dstate, tau, state0, sdstate, tolerance)
            _calc_dual(del_state, dstate, dtau, del_state0, sdstate, tolerance)

#'#@profile
def _calc_primal(state, dstate, tau, state0, sd, tolerance):
    #state[:, :] = np.cumsum(np.hstack((state0, dstate * np.hstack(tau[:, None]))), 1)
    np.cumsum(np.hstack((state0, dstate * tau)), 1, out=state)
    #state[np.logical_or(np.absolute(state) < tolerance, sd)] = 0
    state[sd] = 0


####'#@profile
def _calc_dual(state, dstate, tau, state0, sd, tolerance):
    np.cumsum(np.fliplr(np.hstack((dstate * tau, state0))), 1, out=state)
    #state[:,:] = np.fliplr(np.cumsum(np.fliplr(np.hstack((dstate * tau, state0))),1))
    #state[np.logical_or(np.absolute(state) < tolerance, sd)] = 0
    state[np.fliplr(sd)] = 0

def check_state(state, tolerance):
    test1 = state < -tolerance
    if np.any(test1):
        print('Negative state!')
        print(np.where(test1))

def check_sd(sd, is_primal):
    xsd = sd == 0
    if is_primal:
        test1 = np.logical_and(xsd[:,1:], sd[:,:-1] == 1)
        if np.any(test1):
            print('Positive state jumping to 0!')
            print(np.where(test1))
        test2 = np.logical_and(xsd[:,:-1], sd[:,1:] == -1)
        if np.any(test2):
            print('State going to negative direction!')
            print(np.where(test2))
    else:
        test1 = np.logical_and(xsd[:, :-1], sd[:, 1:] == 1)
        if np.any(test1):
            print('Positive state jumping to 0!')
            print(np.where(test1))
        test2 = np.logical_and(xsd[:, 1:], sd[:, :-1] == -1)
        if np.any(test2):
            print('State going to negative direction!')
            print(np.where(test2))