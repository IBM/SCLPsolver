import numpy as np
from .pivot_storage import pivot_storage
from .col_info_stack import col_info_stack
from .extract_rates import extract_rates_from_basis, extract_rates_from_subproblem
from .SCLP_base_sequence import SCLP_base_sequence
from .rewind_info import rewind_info
from .problem_dimensions import problem_dimensions
from .solution_state import solution_state
from .matrix_constructor import matrix_constructor
from .calc_equations import calc_equations
from .calc_states import calc_states, check_state


class SCLP_solution():

    def __init__(self, prim_name, dual_name, dct, KK=None, JJ=None, totalK = None, totalJ = None):
        self._klist = np.sort(np.append(prim_name[prim_name > 0], dual_name[dual_name > 0]))
        self._jlist = np.sort(-np.append(prim_name[prim_name < 0], dual_name[dual_name < 0]))
        if KK is None:
            KK = np.size(self._klist)
        if JJ is None:
            JJ = np.size(self._jlist)
        self._problem_dims = problem_dimensions(KK, JJ, totalK, totalJ)
        self._pivots = pivot_storage()
        self.tmp_matrix = np.zeros_like(dct)
        self._base_sequence = SCLP_base_sequence({'prim_name': prim_name, 'dual_name': dual_name, 'A': dct}, self.tmp_matrix)
        dx, dq = extract_rates_from_basis(prim_name, dual_name, dct, self._problem_dims)
        self._dx = matrix_constructor(dx[0], dx[1], KK)
        self._dq = matrix_constructor(dq[0], dq[1], JJ)
        self._col_info_stack = col_info_stack()
        self._last_collision = None
        self._state = solution_state()

    def __getstate__(self):
        return self._problem_dims, self._pivots, self._base_sequence, self._dx, self._dq, self._last_collision, self._col_info_stack

    def __setstate__(self, state):
        self._problem_dims, self._pivots, self._base_sequence, self._dx, self._dq, self._last_collision, self._col_info_stack = state
        self._state = solution_state()

    @property
    def klist(self):
        return self._klist

    @property
    def jlist(self):
        return self._jlist

    @property
    def last_collision(self):
        return self._last_collision

    @property
    def pivots(self):
        return self._pivots

    @property
    def base_sequence(self):
        return self._base_sequence

    @property
    def state(self):
        return self._state

    @property
    def NN(self):
        return len(self._pivots) + 1

    @property
    def KK(self):
        return self._problem_dims.KK

    @property
    def JJ(self):
        return self._problem_dims.JJ

    @property
    def totalK(self):
        return self._problem_dims.totalK

    @property
    def totalJ(self):
        return self._problem_dims.totalJ

    #'#@profile
    def update_state(self, param_line, check_state = False, tolerance=0):
        state = solution_state()
        state.dx = self._dx.get_matrix()
        state.dq = self._dq.get_matrix()
        state.sdx = np.ones((state.dx.shape[0], state.dx.shape[1] + 2))
        state.sdq = np.ones((state.dq.shape[0], state.dq.shape[1] + 2))
        np.sign(state.dx, out=state.sdx[:, 1:-1])
        np.sign(state.dq, out=state.sdq[:, 1:-1])
        try:
            state.tau, state.dtau = calc_equations(param_line, self._klist, self._jlist, self._pivots, state.dx, state.dq)
            state.x, state.del_x, state.q, state.del_q\
                = calc_states(state.dx, state.dq, param_line, state.tau, state.dtau, state.sdx, state.sdq)
        except Exception as ex:
            print('Exception during state calculation:')
            print(ex)
            return False
        if check_state:
            if self._check_state(state, tolerance):
                self._state = state
                return True
            else:
                return False
        else:
            self._state = state
            return True

    def _check_state(self, state, tolerance):
        if self._state is not None:
            res = check_state(state.x, tolerance)
            res = res and check_state(state.q, tolerance, False)
            return res
        return False

    def update_from_subproblem(self, col_info, pivots, AAN1, AAN2):
        dx, dq = extract_rates_from_subproblem(pivots, AAN1, AAN2, self._problem_dims, self.tmp_matrix)
        Nnew = len(pivots)
        if AAN1 is not None and AAN2 is not None:
            Nnew -=1
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, pivots, Nnew)

    def update_from_basis(self, col_info, piv, AAN1, AAN2, prim_name, dual_name, dct):
        dx, dq = extract_rates_from_basis(prim_name, dual_name, dct, self._problem_dims)
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, piv, 1,
                           {'prim_name': prim_name, 'dual_name': dual_name, 'A': dct}, False)

    #'#@profile
    def update_caseI(self, col_info):
        NN = self.NN
        self.store_rewind_info(col_info)
        self._last_collision = col_info
        N1 = col_info.N1
        N2 = col_info.N2
        self._base_sequence.remove_bases(N1, N2, self._pivots)
        self._dx.remove(N1 + 1, N2)
        self._dq.remove(N1 + 1, N2)
        self._pivots.remove_pivots(N1, N2)
        col_info.Nnew = self.NN - NN

    #'#@profile
    def _update_caseII(self, col_info, dx, dq, AAN1, AAN2, pivots, Nnew, basis = None, matrix = True):
        NN = self.NN
        self._last_collision = col_info
        if col_info.case == 'Case ii_':
            self.store_rewind_info(col_info)
        else:
            self._col_info_stack.clear()
        N1 = col_info.N1
        N2 = col_info.N2
        self._base_sequence.replace_bases(N1, N2, Nnew, AAN1, AAN2)
        self._pivots.replace_pivots(N1, N2, pivots)
        if matrix:
            self._dx.replace_matrix(N1 + 1, N2, dx)
            self._dq.replace_matrix(N1 + 1, N2, dq)
        else:
            self._dx.replace(N1 + 1, N2, dx[0], dx[1])
            self._dq.replace(N1 + 1, N2, dq[0], dq[1])
        col_info.Nnew = self.NN - NN
        if basis is not None:
            self._base_sequence.insert_basis(basis,N1+1)

    #'#@profile
    def update_rewind(self):
        if self.can_rewind():
            col_info = self._col_info_stack.pop()
            N2_cor = col_info.N2 + col_info.Nnew
            N2b = max(col_info.N2, N2_cor)
            self._base_sequence.remove_bases(col_info.N1, N2b, self._pivots, col_info.Nnew)
            Npivots = len(col_info.rewind_info.pivots)
            self._pivots.replace_pivots(col_info.N1, col_info.N1 + col_info.Nnew + Npivots, col_info.rewind_info.pivots)
            self._dx.replace_matrix(col_info.N1 + 1, N2_cor, col_info.rewind_info.dx)
            self._dq.replace_matrix(col_info.N1 + 1, N2_cor, col_info.rewind_info.dq)
            self._last_collision = self._col_info_stack.last
            return col_info
        else:
            return None

    def can_rewind(self):
        return not self._col_info_stack.is_empty()

    def store_rewind_info(self, col_info):
        N1 = col_info.N1
        N2 = col_info.N2
        cor_N1 = N1 + 1
        if N1 > -1:
            pivots = self.pivots[N1:N2 + 1].copy()
        else:
            pivots = self.pivots[N1 + 1:N2 + 1].copy()
        dx = self._dx.get_sub_matrix(cor_N1, N2)
        dq = self._dq.get_sub_matrix(cor_N1, N2)
        col_info.rewind_info = rewind_info(pivots, dx, dq)
        if not col_info.had_resolution:
            if len(self._col_info_stack) == 1 and not self._col_info_stack.last.had_resolution:
                self._col_info_stack.clear()
        self._col_info_stack.push(col_info)

    def store_ztau_ind(self, ztau_ind):
        if len(ztau_ind) > 0:
            if self._col_info_stack.last is not None:
                self._col_info_stack.last.ztau_ind = ztau_ind


    #'#@profile
    def get_basis_at(self, place):
        new_mat, new_place = self._base_sequence.get_basis_at(place, self._pivots)
        self._base_sequence.insert_basis(new_mat, new_place)
        return new_mat

    #'#@profile
    def get_name_diff_with0(self, name):
        ind, place = self._base_sequence.get_nearby_place_at(0)
        pn = self._base_sequence.bases[ind]['prim_name']
        pn0 = self._pivots.get_prim_name_at0(place,pn)
        return np.setdiff1d(pn0,name, assume_unique=True)

    #'#@profile
    def get_name_diff_withN(self, name):
        ind, place = self._base_sequence.get_nearby_place_at(self.NN-1)
        pn = self._base_sequence.bases[ind]['prim_name']
        pnN = self._pivots.get_prim_name_atN(place,pn)
        return np.setdiff1d(pnN,name, assume_unique=True)

    def check_if_complete(self, param_line):
        if param_line.is_sub():
            res = True
            if param_line.B1 is not None:
                res = res and self.get_name_diff_with0(param_line.B1).size == 0
            if param_line.B2 is not None:
                res = res and self.get_name_diff_withN(param_line.B2).size == 0
            return res
        return False

    #'#@profile
    def get_bases(self, N1, N2):
        new_mat, new_place = self._base_sequence.get_nearby_basis(N1, N2, self._pivots)
        self._base_sequence.insert_basis(new_mat, new_place)
        if new_place == N1:
            return new_mat, self.get_basis_at(N2)
        elif new_place == N2:
            return self.get_basis_at(N1), new_mat
        else:
            raise Exception('Cannot calculate correct bases!')

    #'#@profile
    def get_next_basis_for_solution(self, basis, place):
        return self._base_sequence.get_next_basis(basis, place, self._pivots)

    def print_status(self, STEPCOUNT, DEPTH, ITERATION, theta, col_info):
        print(STEPCOUNT, DEPTH, ITERATION, self.JJ, 'x', self.KK, self.NN, theta, theta + col_info.delta,
              col_info.case, col_info.N1, col_info.N2,  col_info.v1, col_info.v2, len(self.base_sequence.places))

    def print_short_status(self, STEPCOUNT, DEPTH, ITERATION, theta, theta1, case):
        print(STEPCOUNT, DEPTH, ITERATION, self.JJ, 'x', self.KK, self.NN, theta, theta1,
              case, len(self.base_sequence.places))

    def prepare_to_save(self):
        self._base_sequence.keep_only_one()
        self._state = None

    def clear_collision_stack(self):
        self._last_collision = None
        self._col_info_stack.clear()

    def clear_base_sequence(self, mm):
        if mm is not None:
            self._base_sequence.clear_base_sequense(mm.num_bases_to_remove(), mm.max_bs, self.NN)

