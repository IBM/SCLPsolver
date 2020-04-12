import numpy as np

from subroutines.time_collision_resolver import classify_time_collision


def ztau_resolver(col_info, solution, tolerance):
    if np.any(col_info.ztau_ind == col_info.N1):
        result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, col_info.N1-1, col_info.N2, solution,
                                         tolerance)
        if result is None:
            if np.any(col_info.ztau_ind == col_info.N1 -1):
                result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, col_info.N1 - 2,
                                             col_info.N2, solution, tolerance)
                if result is not None:
                    return result
        else:
            return result
    if np.any(col_info.ztau_ind == col_info.N2):
        result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, col_info.N1, col_info.N2+1,
                                         solution, tolerance)
        if result is None:
            if np.any(col_info.ztau_ind == col_info.N2 +1):
                result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, col_info.N1,
                                             col_info.N2 +2, solution, tolerance)
                if result is not None:
                    return result
                else:
                    if np.any(col_info.ztau_ind == col_info.N1):
                        result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff,
                                                         col_info.N1 - 1, col_info.N2 + 2, solution, tolerance)
                        if result is None:
                            if np.any(col_info.ztau_ind == col_info.N1 - 1):
                                result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff,
                                                                 col_info.N1 - 2, col_info.N2 + 2, solution,
                                                                 tolerance)
                                if result is not None:
                                    return result
                        else:
                            return result
            if np.any(col_info.ztau_ind == col_info.N1):
                result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, col_info.N1 - 1,
                                                 col_info.N2 +1, solution, tolerance)
                if result is None:
                    if np.any(col_info.ztau_ind == col_info.N1 - 1):
                        result = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff,
                                                         col_info.N1 - 2, col_info.N2 +1, solution, tolerance)
                        if result is not None:
                            return result
                else:
                    return result
        else:
            return result
    return None


def ztau_resolver2(col_info, solution, tolerance):
    import itertools
    if col_info.ztau_ind is None:
        return None
    zmin = np.min(col_info.ztau_ind)
    zmax = np.max(col_info.ztau_ind)
    list1 = range(min(zmin - 1, col_info.N1),max(zmax + 1, col_info.N2))
    list2 = reversed(range(min(zmin - 1, col_info.N1), max(zmax + 1, col_info.N2)))
    res = list(itertools.product(list1, list2))
    res = [x for x in res if x[1]-x[0]>=2]
    for el in res:
        col = classify_time_collision(col_info.delta, col_info.rz, col_info.tol_coeff, el[0], el[1], solution, tolerance)
        if col is not None:
            return col
    return None