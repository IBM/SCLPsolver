import numpy as np
from .pivot_storage import pivot_storage
from .col_info_stack import col_info_stack
from .extract_rates7 import extract_rates_from_basis, extract_rates_from_subproblem
from .SCLP_base_sequence import SCLP_base_sequence
from .rewind_info7 import rewind_info


class SCLP_solution():

    def __init__(self, prim_name, dual_name, dct, KK, JJ, totalK = None, totalJ = None):
        self._pivots = pivot_storage()
        self._base_sequence = SCLP_base_sequence({'prim_name': prim_name, 'dual_name': dual_name, 'A': dct})
        dx, dq = extract_rates_from_basis(prim_name.copy(), dual_name.copy(), dct, KK, JJ, totalK, totalJ)
        self._dx = dx
        self._dq = dq
        self._col_info_stack = col_info_stack()
        self._last_collision = None

    @property
    def pivots(self):
        return self._pivots

    @property
    def base_sequence(self):
        return self._base_sequence

    @property
    def dx(self):
        return self._dx

    @property
    def dq(self):
        return self._dq

    @property
    def NN(self):
        return len(self._pivots) + 1

    def update_from_subproblem(self, col_info, pivots, AAN1, AAN2, JJ, KK, totalJ, totalK):
        dx, dq = extract_rates_from_subproblem(pivots, AAN1, AAN2, JJ, KK, totalJ, totalK)
        Nnew = len(pivots)
        if AAN1 is not None and AAN2 is not None:
            Nnew -=1
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, pivots, Nnew)

    def update_from_basis(self, col_info, piv, AAN1, AAN2, JJ, KK, totalJ, totalK, prim_name, dual_name, dct):
        dx, dq = extract_rates_from_basis(prim_name, dual_name, dct, KK, JJ, totalK, totalJ)
        self._update_caseII(col_info, dx, dq, AAN1, AAN2, piv, 1,
                           {'prim_name': prim_name, 'dual_name': dual_name, 'A': dct})

    #'#@profile
    def update_caseI(self, col_info):
        NN = self.NN
        self._col_info_stack.clear()
        self._last_collision = col_info
        N1 = col_info.N1
        N2 = col_info.N2
        self._base_sequence.remove_bases(N1, N2, self._pivots)
        self._dx.remove(N1 + 1, N2)
        self._dq.remove(N1 + 1, N2)
        self._pivots.remove_pivots(N1, N2)
        col_info.Nnew = self.NN - NN

    #'#@profile
    def _update_caseII(self, col_info, dx, dq, AAN1, AAN2, pivots, Nnew, basis = None):
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
        self._dx.replace_matrix(N1 + 1, N2, dx)
        self._dq.replace_matrix(N1 + 1, N2, dq)
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

    # '#@profile
    def get_state_slopes(self):
        dx = self.dx.get_matrix()
        dq = self.dq.get_matrix()
        sdx = np.ones((dx.shape[0], dx.shape[1] + 2))
        sdq = np.ones((dq.shape[0], dq.shape[1] + 2))
        np.sign(dx, out=sdx[:, 1:-1])
        np.sign(dq, out=sdq[:, 1:-1])
        return dx, dq, sdx, sdq
