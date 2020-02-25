from .matlab_utils import find
from .sparse_matrix_constructor import sparse_matrix_constructor


#'#@profile
def calc_controls(solution, JJ, KK, preserve = True):

    new_dict = solution.get_basis_at(0)
    u = sparse_matrix_constructor(None, None, JJ)
    p = sparse_matrix_constructor(None, None, KK)
    if preserve:
        new_dict = {'prim_name': new_dict['prim_name'].copy(), 'dual_name': new_dict['dual_name'].copy(), 'A': new_dict['A'].copy()}

    for place in range(solution.NN):
        klist2 = find(new_dict['dual_name'] > 0)
        jlist1 = find(new_dict['prim_name'] < 0)
        kn2 =  new_dict['dual_name'][klist2]
        jn1 = -new_dict['prim_name'][jlist1]
        u.append(sparse_matrix_constructor(new_dict['A'][jlist1+1,0].copy(), jn1-1, JJ))
        p.append(sparse_matrix_constructor(new_dict['A'][0,klist2+1].copy(), kn2-1, KK))
        if place < solution.NN - 1:
            new_dict = solution.get_next_basis_for_solution(new_dict, place, preserve)
    return u.get_matrix(), p.get_matrix()