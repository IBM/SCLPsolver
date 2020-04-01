import numpy as np
from .state_tools import calc_state_prim, calc_state_dual
#from multiprocessing import Process, Value, Array


#'#@profile
def calc_states(dx,dq,param_line,tau,dtau):
    K1, N1  = dx.shape
    J1 = dq.shape[0]
    # TODO: parallelize
    x, del_x = _calc_states(K1, param_line.x_0, param_line.del_x_0, tau, dtau, dx, True)
    q, del_q = _calc_states(J1, param_line.q_N, param_line.del_q_N, tau, dtau, dq, False)
    return x, del_x, q, del_q


#'#@profile
def _calc_states(vdim, state0, del_state0, tau, dtau, dstate, is_primal):
    if vdim > 0:
        if is_primal:
            #TODO: parallelize
            state =calc_state_prim(dstate, tau, state0)
            del_state = calc_state_prim(dstate, dtau, del_state0)
        else:
            # TODO: parallelize
            state = calc_state_dual(dstate, tau, state0)
            del_state = calc_state_dual(dstate, dtau, del_state0)
        return state, del_state

def check_state(state, tolerance, is_primal = True):
    test1 = state < -tolerance
    if np.any(test1):
        print('Negative ' + ('primal' if is_primal else 'dual') + ' state!')
        print(np.where(test1))
        return False
    return True
