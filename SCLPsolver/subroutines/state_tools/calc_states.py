import numpy as np
from .state_tools import calc_state_prim, calc_state_dual, calc_specific_state_prim, calc_specific_state_dual

from collections import namedtuple
State = namedtuple('State', ['x', 'del_x', 'q', 'del_q'])

#'#@profile
def calc_states(dx_tuple, dq_tuple, param_line, tau, dtau, checked = False):
    K1 = dx_tuple[0].shape[0]
    J1 = dq_tuple[0].shape[0]
    # TODO: parallelize
    x, del_x = _calc_states(K1, param_line.x_0, param_line.del_x_0, tau, dtau, dx_tuple, True, checked)
    q, del_q = _calc_states(J1, param_line.q_N, param_line.del_q_N, tau, dtau, dq_tuple, False, checked)
    return x, del_x, q, del_q

def _calc_states(vdim, state0, del_state0, tau, dtau, dstate_tuple, is_primal, checked = False):
    if vdim > 0:
        if is_primal:
            state = calc_state_prim(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], tau, state0, checked)
            del_state = calc_state_prim(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], dtau, del_state0, checked)
        else:
            # TODO: parallelize
            state = calc_state_dual(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], tau, state0, checked)
            del_state = calc_state_dual(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], dtau, del_state0, checked)
        return state, del_state

def check_state(state, tolerance, is_primal = True):
    test1 = state < -tolerance
    if np.any(test1):
        print('Negative ' + ('primal' if is_primal else 'dual') + ' state! ', state.min())
        print(np.where(test1))
        return False
    return True

def calc_specific_state(n, i, is_primal, is_del, dx_tuple, dq_tuple, param_line, tau, dtau):
    if is_primal:
        if is_del:
            return calc_specific_state_prim(n, i, dx_tuple[0], dx_tuple[1], dx_tuple[2], dtau, param_line.del_x_0)
        else:
            return calc_specific_state_prim(n, i, dx_tuple[0], dx_tuple[1], dx_tuple[2], tau, param_line.x_0)
    else:
        if is_del:
            return calc_specific_state_dual(n, i, dq_tuple[0], dq_tuple[1], dq_tuple[2], dtau, param_line.del_q_N)
        else:
            return calc_specific_state_dual(n, i, dq_tuple[0], dq_tuple[1], dq_tuple[2], tau, param_line.q_N)