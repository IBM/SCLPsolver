# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from .pivot_storage import pivot_storage
from .col_info_stack import col_info_stack
from .extract_rates import extract_rates_from_basis, extract_rates_from_subproblem, extract_rates_from_partial
from .SCLP_base_sequence import SCLP_base_sequence
from .rewind_info import rewind_info
from .problem_dimensions import problem_dimensions
from .solution_state import solution_state
from .matrix_constructor import matrix_constructor
from .equation_tools.calc_equations import time_equations
from .state_tools.loc_min_storage import loc_min_storage
from .state_tools.calc_states import calc_states, check_state, calc_specific_state
from .bases_memory_manager import bases_memory_manager


class generic_SCLP_solution():

    def __init__(self, LP_form, settings, KK=None, JJ=None, totalK = None, totalJ = None):
        self._klist = np.ascontiguousarray(np.sort(np.append(LP_form.prim_name[LP_form.prim_name > 0], LP_form.dual_name[LP_form.dual_name > 0])), dtype=np.int32)
        self._jlist = np.ascontiguousarray(np.sort(-np.append(LP_form.prim_name[LP_form.prim_name < 0], LP_form.dual_name[LP_form.dual_name < 0])), dtype=np.int32)
        if KK is None:
            KK = np.size(self._klist)
        if JJ is None:
            JJ = np.size(self._jlist)
        self._problem_dims = problem_dimensions(KK, JJ, totalK, totalJ)
        self._pivots = pivot_storage()
        self._base_sequence = SCLP_base_sequence(LP_form)
        dx, dq = extract_rates_from_basis(LP_form, self._problem_dims)
        self._dx = matrix_constructor(dx[0], dx[1], KK)
        self._dq = matrix_constructor(dq[0], dq[1], JJ)
        self.loc_min_storage = loc_min_storage(self._dx.get_matrix(), self._dq.get_matrix())
        self._equations = time_equations()
        self._col_info_stack = col_info_stack()
        self.bases_mm = bases_memory_manager(LP_form.prim_name.shape[0], LP_form.dual_name.shape[0])
        self._last_collision = None
        self._suppress_printing = settings.suppress_printing
        self.rewind_max_delta = settings.rewind_max_delta
        if self._problem_dims.totalK >= 100:
            self.partial_states = True
        else:
            self.partial_states = False
        self._state = solution_state(4*max(KK,JJ), JJ, KK)
        self.stable_iteration = True

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

    def get_raw_dx(self):
        return self._dx.get_raw_matrix()

    def get_raw_dq(self):
        return self._dq.get_raw_matrix()

    #'#@profile
    def update_state(self, param_line, check_state = False, tolerance=0, up_rewind =False):
        #state = solution_state()
        self._state.dx = self._dx.get_matrix()
        self._state.dq = self._dq.get_matrix()
        if self._last_collision and self._equations.can_update(self._last_collision) and not check_state and\
                param_line.is_main() and not up_rewind:
            dtau = self._equations.update(self._last_collision.N1 + 1, self._state.dx, self._state.dq)
            self._state.update_tau(self._last_collision, param_line.T)
            self.stable_iteration = False
        else:
            left_idx = self._equations.build(param_line, self._klist, self._jlist, self._pivots,
                                  self._state.dx, self._state.dq)
            tau, dtau = self._equations.solve()
            if np.any(tau < -tolerance):
                idx = np.argmin(tau)
                if  self._last_collision:
                    next_tau = self._last_collision.delta * dtau[idx] + tau[idx]
                else:
                    next_tau = 0.01 * dtau[idx] + tau[idx]
                print('Warning tau=', idx, 'has value', tau[idx], 'increase by', dtau[idx], 'to', next_tau)
                if self._last_collision and not check_state and param_line.is_main() and not up_rewind and\
                        dtau[idx] > -tolerance and next_tau > -10E-5:
                    print('Updating...')
                    self.stable_iteration = False
                    self._state.update_tau(self._last_collision, param_line.T)
                else:
                    self.stable_iteration = True
                    self._state.tau = tau
            else:
                self._state.tau = tau
                self.stable_iteration = True
        self._state.dtau = dtau
        if check_state or not self.partial_states:
            x, del_x, q, del_q = calc_states(self._dx.get_raw_matrix(), self._dq.get_raw_matrix(), param_line, self._state.tau,
                              self._state.dtau, check_state)
            self._state.x = x
            self._state.del_x = del_x
            self._state.q = q
            self._state.del_q = del_q
        if check_state:
            if self._check_state(self._state, tolerance*100):
                return True
            else:
                return False
        else:
            return True

    def recalc_tau(self, param_line, check_state = False):
        left_idx = self._equations.build(param_line, self._klist, self._jlist, self._pivots,
                                         self._state.dx, self._state.dq)
        tau, dtau = self._equations.solve()
        self._state.tau = tau
        self._state.dtau = dtau
        if check_state or not self.partial_states:
            self._state.x, self._state.del_x, self._state.q, self._state.del_q \
                = calc_states(self._dx.get_raw_matrix(), self._dq.get_raw_matrix(), param_line, self._state.tau,
                              self._state.dtau, check_state)

    def get_specific_state(self, n, i, is_primal, is_del, param_line):
        if self.partial_states:
            return calc_specific_state(n, i, is_primal, is_del, self._dx.get_raw_matrix(), self._dq.get_raw_matrix(),
                                       param_line, self._state.tau, self._state.dtau)
        else:
            if is_primal:
                if is_del:
                    return self._state.del_x[i, n]
                else:
                    return self._state.x[i, n]
            else:
                if is_del:
                    return self._state.del_q[i, n]
                else:
                    return self._state.q[i, n]

    def _check_state(self, state, tolerance):
        if self._state is not None:
            res = check_state(state.x, tolerance)
            res = res and check_state(state.q, tolerance, False)
            return res
        return False

    def update_from_subproblem(self, col_info, pivots, AAN1, AAN2):
        dx, dq = extract_rates_from_subproblem(pivots, AAN1, AAN2, self._problem_dims)
        Nnew = len(pivots)
        if AAN1 is not None and AAN2 is not None:
            Nnew -=1
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, pivots, Nnew)

    def update_from_basis(self, col_info, piv, AAN1, AAN2, basis):
        dx, dq = extract_rates_from_basis(basis, self._problem_dims)
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, piv, 1, basis, False)

    def update_from_partial(self, col_info, piv, AAN1, AAN2, prim_vars, dual_vars, prim_names, dual_names):
        dx, dq = extract_rates_from_partial(prim_vars, dual_vars, prim_names, dual_names, self._problem_dims)
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, piv, 1, None, False)

    #'#@profile
    def update_caseI(self, col_info):
        NN = self.NN
        self.store_rewind_info(col_info)
        self._last_collision = col_info
        N1 = col_info.N1
        N2 = col_info.N2
        self._base_sequence.remove_bases(N1, N2, self._pivots, self.bases_mm)
        self._dx.remove(N1 + 1, N2)
        self._dq.remove(N1 + 1, N2)
        self._pivots.remove_pivots(N1, N2)
        if N2 == NN:
            N2 = None
        self.loc_min_storage.update_caseI(N1, N2, self._dx.get_matrix(), self._dq.get_matrix())
        col_info.Nnew = self.NN - NN

    #'#@profile
    def _update_caseII(self, col_info, dx, dq, AAN1, AAN2, pivots, Nnew, basis = None, matrix = True):
        NN = self.NN
        self._last_collision = col_info
        self.store_rewind_info(col_info)
        N1 = col_info.N1
        N2 = col_info.N2
        self._base_sequence.replace_bases(N1, N2, Nnew, AAN1, AAN2, self.bases_mm)
        self._pivots.replace_pivots(N1, N2, pivots)
        if matrix:
            self._dx.replace_matrix(N1 + 1, N2, dx)
            self._dq.replace_matrix(N1 + 1, N2, dq)
            Nadd = Nnew
        else:
            self._dx.replace(N1 + 1, N2, dx[0], dx[1])
            self._dq.replace(N1 + 1, N2, dq[0], dq[1])
            Nadd = 1
        col_info.Nnew = self.NN - NN
        if N2 == NN:
            N2 = None
        self.loc_min_storage.update_caseII(N1, N2, Nadd, self._dx.get_matrix(), self._dq.get_matrix())
        if basis is not None:
            self._base_sequence.insert_basis(basis,N1+1)

    #'#@profile
    def update_rewind(self):
        if self.can_rewind():
            NN = self.NN
            col_info = self._col_info_stack.pop()
            N2_cor = col_info.N2 + col_info.Nnew
            self._base_sequence.remove_bases(col_info.N1, N2_cor, self._pivots, self.bases_mm, col_info.N2-col_info.N1-1)
            Npivots = len(col_info.rewind_info.pivots)
            self._pivots.replace_pivots(col_info.N1, col_info.N1 + col_info.Nnew + Npivots, col_info.rewind_info.pivots)
            self._dx.replace_matrix(col_info.N1 + 1, N2_cor, col_info.rewind_info.dx)
            self._dq.replace_matrix(col_info.N1 + 1, N2_cor, col_info.rewind_info.dq)
            Nadd = col_info.rewind_info.dx.shape[1]
            if N2_cor == NN:
                N2_cor = None
            if Nadd == 0:
                self.loc_min_storage.update_caseI(col_info.N1, N2_cor, self._dx.get_matrix(), self._dq.get_matrix())
            else:
                self.loc_min_storage.update_caseII(col_info.N1, N2_cor, Nadd, self._dx.get_matrix(), self._dq.get_matrix())
            self._last_collision = self._col_info_stack.last
            return col_info
        else:
            return None

    def can_rewind(self):
        return not self._col_info_stack.is_empty()

    #'#@profile
    def store_rewind_info(self, col_info):
        if col_info.delta < self.rewind_max_delta:
            N1 = col_info.N1
            N2 = col_info.N2
            cor_N1 = N1 + 1
            if col_info.case == 'Case iii':
                if N1 > -1:
                    pivots = self.pivots[N1:N2].copy()
                else:
                    pivots = pivot_storage()
            else:
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
        else:
            self._col_info_stack.clear()

    def store_ztau_ind(self, ztau_ind):
        if len(ztau_ind) > 0:
            if self._col_info_stack.last is not None:
                self._col_info_stack.last.ztau_ind = ztau_ind

    def get_ztau_ind(self):
        if self._col_info_stack.last is not None:
            return self._col_info_stack.last.ztau_ind
        else:
            return None

    #'#@profile
    def get_basis_at(self, place):
        new_mat, new_place = self._base_sequence.get_basis_at(place, self._pivots)
        self._base_sequence.insert_basis(new_mat, new_place)
        return new_mat

    #'#@profile
    def get_name_diff_with0(self, name):
        place, basis = self._base_sequence.get_nearby_basis_at0()
        pn = basis.prim_name
        pn0 = self._pivots.get_prim_name_at0(place,pn)
        return np.setdiff1d(pn0,name, assume_unique=True)

    #'#@profile
    def get_name_diff_withN(self, name):
        place, basis = self._base_sequence.get_nearby_basis_atN()
        pn = basis.prim_name
        pnN = self._pivots.get_prim_name_atN(self.NN + place,pn)
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
    def get_next_basis_for_solution(self, basis, place, preserve = True):
        return self._base_sequence.get_next_basis(basis, place, self._pivots, preserve)

    def print_status(self, STEPCOUNT, DEPTH, ITERATION, theta, col_info):
        if not self._suppress_printing:
            print(STEPCOUNT, DEPTH, ITERATION, self.JJ, 'x', self.KK, self.NN, theta, theta + col_info.delta,
                  col_info.case, col_info.N1, col_info.N2,  col_info.v1, col_info.v2, self.base_sequence.num_bases)

    def print_short_status(self, STEPCOUNT, DEPTH, ITERATION, theta, theta1, case):
        if not self._suppress_printing:
            print(STEPCOUNT, DEPTH, ITERATION, self.JJ, 'x', self.KK, self.NN, theta, theta1,
                  case, self.base_sequence.num_bases)

    def prepare_to_save(self):
        self._base_sequence.keep_only_one()
        #self._state = None

    def clear_collision_stack(self):
        self._last_collision = None
        self._col_info_stack.clear()

    def clear_base_sequence(self, mm):
        if mm is not None:
            self._base_sequence.clear_base_sequense(mm.num_bases_to_remove(), mm.max_bs, self.NN)
