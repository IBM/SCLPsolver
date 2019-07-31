from numpy import outer


def base_pivot(LP_form, i, j, tmp):
    nam = LP_form.prim_name[i]
    LP_form.prim_name[i] = LP_form.dual_name[j]
    LP_form.dual_name[j] = nam
    i += 1
    j += 1
    p = LP_form.simplex_dict[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = LP_form.simplex_dict[i,:] / p
    c = LP_form.simplex_dict[:, j].copy()
    LP_form.simplex_dict -= outer(c, rp, out=tmp)
    LP_form.simplex_dict[i,:] = rp
    LP_form.simplex_dict[:, j] = c / -p
    LP_form.simplex_dict[i, j] = 1. / p
    return LP_form

def full_pivot(LP_form, i, j, tmp):
    sam = LP_form.prim_sign[i]
    LP_form.prim_sign[i] = - LP_form.dual_sign[j]
    LP_form.dual_sign[j] = - sam
    nam = LP_form.prim_name[i]
    LP_form.prim_name[i] = LP_form.dual_name[j]
    LP_form.dual_name[j] = nam
    i += 1
    j += 1
    p = LP_form.simplex_dict[i, j]
    if p == 0:
        raise Exception('pivot on zero')
    rp = LP_form.simplex_dict[i, :] / p
    c = LP_form.simplex_dict[:, j].copy()
    LP_form.simplex_dict -= outer(c, rp, out=tmp)
    LP_form.simplex_dict[i, :] = rp
    LP_form.simplex_dict[:, j] = c / -p
    LP_form.simplex_dict[i, j] = 1. / p
    return LP_form