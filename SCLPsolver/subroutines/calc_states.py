import numpy as np
#from multiprocessing import Process, Value, Array


#'#@profile
def calc_states(dx,dq,param_line,tau,dtau,sdx, sdq):
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
    _calc_states(x, del_x, K1, param_line.x_0, param_line.del_x_0, tau, dtau, dx, sdx, True)
    _calc_states(q, del_q, J1, param_line.q_N, param_line.del_q_N, tau, dtau, dq, sdq, False)
    return x, del_x, np.fliplr(q), np.fliplr(del_q)


#'#@profile
def _calc_states(state, del_state, vdim, state0, del_state0, tau, dtau, dstate, sdstate, is_primal):
    if vdim > 0:
        sstate = sdstate == 0
        sdstate = np.logical_or(sstate[:,:-1],sstate[:,1:])
        if is_primal:
            #TODO: parallelize
            _calc_primal(state, dstate, tau, state0, sdstate)
            _calc_primal(del_state, dstate, dtau, del_state0, sdstate)
        else:
            # TODO: parallelize
            _calc_dual(state, dstate, tau, state0, sdstate)
            _calc_dual(del_state, dstate, dtau, del_state0, sdstate)

#'#@profile
def _calc_primal(state, dstate, tau, state0, sd):
    if state0 is not None:
        state[:, 0:1] = state0
    np.multiply(dstate, tau, out=state[:, 1:])
    np.cumsum(state, 1, out=state)
    state[sd] = 0


#'#@profile
def _calc_dual(state, dstate, tau, state0, sd):
    if state0 is not None:
        state[:, 0:1] = state0
    np.multiply(np.fliplr(dstate), tau[::-1], out=state[:, 1:])
    np.cumsum(state, 1, out=state)
    state[np.fliplr(sd)] = 0

def check_state(state, tolerance, is_primal = True):
    test1 = state < -tolerance
    if np.any(test1):
        print('Negative ' + ('primal' if is_primal else 'dual') + ' state!')
        print(np.where(test1))
        return False
    return True

def check_sd(sd, is_primal):
    xsd = sd == 0
    if is_primal:
        test1 = np.logical_and(xsd[:,1:], sd[:,:-1] == 1)
        if np.any(test1):
            print('Positive dx jumping to 0!')
            print(np.where(test1))
            return False
        test2 = np.logical_and(xsd[:,:-1], sd[:,1:] == -1)
        if np.any(test2):
            print('Zero dx going to negative direction!')
            print(np.where(test2))
            return False
        else:
            return True
    else:
        test1 = np.logical_and(xsd[:, :-1], sd[:, 1:] == 1)
        if np.any(test1):
            print('Positive dq jumping to 0!')
            print(np.where(test1))
            return False
        test2 = np.logical_and(xsd[:, 1:], sd[:, :-1] == -1)
        if np.any(test2):
            print('Zero dq going to negative direction!')
            print(np.where(test2))
            return False
        else:
            return True