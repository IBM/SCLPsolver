import numpy as np


def SCLP_recalculate(solution, param_line, t0, new_x0, settings, tolerance, find_alt_line=True, mm=None):

    DEPTH = 0
    STEPCOUNT = 0
    ITERATION = {0:0}

    solution.truncate_at(t0)
    nz_indexes = np.where(np.logical_and(solution.state.x[:, 0] <= tolerance, new_x0 >= tolerance))[0]

    for nz_index in nz_indexes:
        col_info = collision_info('', 0, -1, 0, v2, [])
        solution, STEPCOUNT, ITERATION, pivot_problem = SCLP_pivot(K_0, J_N, solution, col_info, DEPTH, STEPCOUNT,
                                                                   ITERATION, settings, tolerance)