import numpy as np
from .matlab_utils import find

#check indexing

def calc_order_ratio(v1, v2, N1, N2, solution, param_line, delta):
    correct = True
    if v1 > 0 and v2 > 0:
        k1 = find(solution.klist == v1)
        dx1 = solution.state.dx[k1, N1]
        if dx1 > 0:
            correct = False
            print('Incorrect dx!', k1, N1)
        x1 = solution.get_specific_state(N1+1, k1, True, False, param_line) + delta * \
             solution.get_specific_state(N1+1, k1, True, True, param_line)
        k2 = find(solution.klist == v2)
        dx2 = solution.state.dx[k2, N1]
        if dx2 > 0:
            correct = False
            print('Incorrect dx!', k2, N1)
        x2 = solution.get_specific_state(N1 + 1, k2, True, False, param_line) + delta * \
             solution.get_specific_state(N1 + 1, k2, True, True, param_line)
        return (x1 / dx1) / (x2 / dx2), correct
    elif v1 < 0 and v2 < 0:
        j1 = find(solution.jlist == -v1)
        dq1 = solution.state.dq[j1, N2]
        if dq1 > 0:
            correct = False
            print('Incorrect dq!', j1, N2)
        q1 = solution.get_specific_state(N2, j1, False, False, param_line) + delta * \
             solution.get_specific_state(N2, j1, False, True, param_line)
        j2 = find(solution.jlist == -v2)
        dq2 = solution.state.dq[j2, N2]
        if dq2 > 0:
            correct = False
            print('Incorrect dq!', j2, N2)
        q2 = solution.get_specific_state(N2, j2, False, False, param_line) + delta * \
             solution.get_specific_state(N2, j2, False, True, param_line)
        return (q2 / dq2) / (q1 / dq1), correct
    elif v1 > 0 and v2 < 0:
        k1 = find(solution.klist == v1)
        dx1 = solution.state.dx[k1, N1]
        if dx1 > 0:
            correct = False
            print('Incorrect dx!', k1, N1)
        x1 = solution.get_specific_state(N1+1, k1, True, False, param_line) + delta * \
             solution.get_specific_state(N1+1, k1, True, True, param_line)
        j2 = find(solution.jlist == -v2)
        dq2 = solution.state.dq[j2, N2]
        if dq2 > 0:
            correct = False
            print('Incorrect dq!', j2, N2)
        q2 = solution.get_specific_state(N2, j2, False, False, param_line) + delta * \
             solution.get_specific_state(N2, j2, False, True, param_line)
        t_interval = np.sum(solution.state.tau[N1 + 1:N2]) + delta * np.sum(solution.state.dtau[N1 + 1:N2])
        return -(x1 / dx1 + q2 / dq2) / t_interval, correct
    elif v1 < 0 and v2 > 0:
        j1 = find(solution.jlist == -v1)
        dq1 = solution.state.dq[j1, N2]
        if dq1 > 0:
            correct = False
            print('Incorrect dq!', j1, N2)
        q1 = solution.get_specific_state(N2, j1, False, False, param_line) + delta * \
             solution.get_specific_state(N2, j1, False, True, param_line)
        k2 = find(solution.klist == v2)
        dx2 = solution.state.dx[k2, N1]
        if dx2 > 0:
            correct = False
            print('Incorrect dx!', k2, N1)
        x2 = solution.get_specific_state(N1 + 1, k2, True, False, param_line) + delta * \
             solution.get_specific_state(N1 + 1, k2, True, True, param_line)
        t_interval = np.sum(solution.state.tau[N1 + 1:N2]) + delta * np.sum(solution.state.dtau[N1 + 1:N2])
        return -t_interval / (q1 / dq1 + x2 / dx2), correct