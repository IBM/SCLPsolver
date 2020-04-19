import numpy as np


def calc_states_partial1(dx_tuple, dq_tuple, param_line, tau, dtau, loc_mins):
    K1 = dx_tuple[0].shape[0]
    J1 = dq_tuple[0].shape[0]
    # TODO: parallelize
    x, del_x = _calc_states_partial1(K1, param_line.x_0, param_line.del_x_0, tau, dtau, dx_tuple, True, loc_mins.dx_min)
    q, del_q = _calc_states_partial1(J1, param_line.q_N, param_line.del_q_N, tau, dtau, dq_tuple, False, loc_mins.dq_min)
    return x, del_x, q, del_q


def _calc_states_partial1(vdim, state0, del_state0, tau, dtau, dstate_tuple, is_primal, loc_min):
    if vdim > 0:
        if is_primal:
            #TODO: parallelize
            state =calc_state_partial_prim1(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], tau, state0, loc_min.row_idx)
            del_state = calc_state_partial_prim1(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], dtau, del_state0, loc_min.row_idx)
        else:
            # TODO: parallelize
            state = calc_state_partial_dual1(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], tau, state0, loc_min.row_idx)
            del_state = calc_state_partial_dual1(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], dtau, del_state0, loc_min.row_idx)
        return state, del_state


def calc_states_partial(dx_tuple, dq_tuple, param_line, tau, dtau, loc_mins):
    K1 = dx_tuple[0].shape[0]
    J1 = dq_tuple[0].shape[0]
    # TODO: parallelize
    x, del_x = _calc_states_partial(K1, param_line.x_0, param_line.del_x_0, tau, dtau, dx_tuple, True, loc_mins.dx_min)
    q, del_q = _calc_states_partial(J1, param_line.q_N, param_line.del_q_N, tau, dtau, dq_tuple, False, loc_mins.dq_min)
    return x, del_x, q, del_q


def _calc_states_partial(vdim, state0, del_state0, tau, dtau, dstate_tuple, is_primal, loc_min):
    if vdim > 0:
        if is_primal:
            #TODO: parallelize
            state =calc_state_partial_prim(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], tau, state0, loc_min.data, loc_min.sizes)
            del_state = calc_state_partial_prim(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], dtau, del_state0, loc_min.data, loc_min.sizes)
        else:
            # TODO: parallelize
            state = calc_state_partial_dual(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], tau, state0, loc_min.data, loc_min.sizes)
            del_state = calc_state_partial_dual(dstate_tuple[0], dstate_tuple[1], dstate_tuple[2], dtau, del_state0, loc_min.data, loc_min.sizes)
        return state, del_state


def calc_states1(dx_tuple, dq_tuple, param_line, tau, dtau, checked = False):
    K1, N = dx_tuple[0].shape
    J1 = dq_tuple[0].shape[0]
    x = np.zeros((K1, N+1), dtype=np.float64, order="C")
    del_x = np.zeros((K1, N+1), dtype=np.float64, order="C")
    q = np.zeros((J1, N+1), dtype=np.float64, order="C")
    del_q = np.zeros((J1, N+1), dtype=np.float64, order="C")
    cy_calc_state(dx_tuple[0], dx_tuple[1], dx_tuple[2], dq_tuple[0], dq_tuple[1], dq_tuple[2], tau, dtau,
                  param_line.x_0, param_line.del_x_0, param_line.q_N, param_line.del_q_N, x, del_x, q, del_q, checked)
    return x, del_x, q, del_q