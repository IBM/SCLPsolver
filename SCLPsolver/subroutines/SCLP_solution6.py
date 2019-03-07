import numpy as np
from .pivot_storage import pivot_storage

class SCLP_solution():

    def __init__(self, pivots, base_sequence, dx, dq):
        if pivots is None or len(pivots) == 0:
            self._pivots = pivot_storage()
        else:
            self._pivots = pivots
        self._base_sequence = base_sequence
        self._dx = dx
        self._dq = dq

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

    #'#@profile
    def update_caseI(self, N1, N2):
        self._base_sequence.remove_bases(N1, N2, self._pivots)
        self._dx.remove(N1 + 1, N2)
        self._dq.remove(N1 + 1, N2)
        self._pivots.remove_pivots(N1, N2)


    #'#@profile
    def update_caseII(self, N1, N2, dx, dq, AAN1, AAN2, pivots, Nnew, basis = None):
        self._base_sequence.replace_bases(N1, N2, Nnew, AAN1, AAN2)
        self._pivots.replace_pivots(N1, N2, pivots)
        self._dx.replace_matrix(N1 + 1, N2, dx)
        self._dq.replace_matrix(N1 + 1, N2, dq)
        if basis is not None:
            self._base_sequence.insert_basis(basis,N1+1)

    #'#@profile
    def update_rewind(self, col_info):
        N2_cor = col_info.N2 + col_info.Nnew
        N2b = max(col_info.N2, N2_cor)
        self._base_sequence.remove_bases(col_info.N1, N2b, self._pivots, col_info.Nnew)
        Npivots = len(col_info.rewind_info.pivots)
        self._pivots.replace_pivots(col_info.N1, col_info.N1 + col_info.Nnew + Npivots, col_info.rewind_info.pivots)
        self._dx.replace_matrix(col_info.N1 + 1, N2_cor, col_info.rewind_info.dx)
        self._dq.replace_matrix(col_info.N1 + 1, N2_cor, col_info.rewind_info.dq)

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
