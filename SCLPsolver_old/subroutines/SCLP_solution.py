import numpy as np


class SCLP_solution():

    def __init__(self, prim_name, dual_name, pivots, base_sequence, dx, dq):
        self._prim_name = prim_name
        self._dual_name = dual_name
        self._pivots = pivots
        self._base_sequence = base_sequence
        self._dx = dx
        self._dq = dq

    @property
    def prim_name(self):
        return self._prim_name

    @property
    def dual_name(self):
        return self._dual_name

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

    ###@profile
    def update_caseI(self, N1, N2):
        self._base_sequence.remove_bases(N1, N2, self._pivots)
        self._dx.remove(N1 + 1, N2)
        self._dq.remove(N1 + 1, N2)
        NN = self.NN

        if N1 >= 0:
            pivots_new = self._pivots[0:N1]
        else:
            pivots_new = []
        if N1 >= 0 and N2 < NN:
            pivots_new.append(np.setdiff1d(self._prim_name[:, N1], self._prim_name[:, N2], assume_unique=True).tolist()
                              + np.setdiff1d(self._prim_name[:, N2], self._prim_name[:, N1], assume_unique=True).tolist())
        self._pivots = pivots_new + self._pivots[N2:]
        self._prim_name = np.hstack((self._prim_name[:, 0:N1 + 1], self._prim_name[:, N2:]))
        #self._dual_name = np.hstack((self._dual_name[:, 0:N1 + 1], self._dual_name[:, N2:]))

    ###@profile
    def update_caseII(self, N1, N2, prim_name, dual_name, dx, dq, AAN1, AAN2, pivots, basis = None):
        Nnew = prim_name.shape[1]
        self._base_sequence.replace_bases(N1, N2, Nnew, AAN1, AAN2)
        NNold = self.NN
        if pivots is not None and len(pivots) > 0:
            if N1 > 0:
                if N2 - 1 == self.NN:
                    self._pivots = self._pivots[0:N1] + pivots
                else:
                    self._pivots = self._pivots[0:N1] + pivots + self._pivots[N2:]
            else:
                self._pivots = pivots + self._pivots[N2:]
        #else:
            # pivots_new = self._pivots[0:N1 + 1]
            # if N1 >= 0:
            #     piv = np.setdiff1d(self._prim_name[:, N1], prim_name[:, 0], assume_unique=True).tolist() + \
            #                          np.setdiff1d(self._dual_name[:, N1], dual_name[:, 0], assume_unique=True).tolist()
            #     if len(pivots_new) > N1:
            #         pivots_new[N1] = piv
            #     else:
            #         pivots_new.append(piv)
            # for nn in range(Nnew - 1):
            #     pivots_new.append(np.setdiff1d(prim_name[:, nn], prim_name[:, nn + 1], assume_unique=True).tolist()
            #                       + np.setdiff1d(dual_name[:, nn], dual_name[:, nn + 1], assume_unique=True).tolist())
            # if N2 < NNold:
            #     pivots_new.append(np.setdiff1d(prim_name[:, -1], self._prim_name[:, N2], assume_unique=True).tolist()
            #                       + np.setdiff1d(dual_name[:, -1], self._dual_name[:, N2], assume_unique=True).tolist())
            #     if len(self._pivots[N2:]) > 0:
            #         pivots_new += (self._pivots[N2:])
            # self._pivots = pivots_new
        self._prim_name = np.hstack((self._prim_name[:, :N1 + 1], prim_name, self._prim_name[:, N2:]))
        #self._dual_name = np.hstack((self._dual_name[:, :N1 + 1], dual_name, self._dual_name[:, N2:]))
        self._dx.replace_matrix(N1 + 1, N2, dx)
        self._dq.replace_matrix(N1 + 1, N2, dq)

    ###@profile
    def update_rewind(self, N1, N2, Nnew, prim_name, dual_name, dx, dq, pivots):
        N2_cor = N2 + Nnew
        N2b = max(N2, N2_cor)
        self._base_sequence.remove_bases(N1, N2b, self._pivots, Nnew)
        Npivots = len(pivots)
        if N1 > 0:
            if N2_cor - 1 == self.NN:
                self._pivots = self._pivots[0:N1] + pivots
            else:
                self._pivots = self._pivots[0:N1] + pivots + self._pivots[(N1 + Nnew + Npivots):]
        else:
            self._pivots = pivots + self._pivots[(N1 + Nnew + Npivots):]
        self._prim_name = np.hstack((self._prim_name[:, :N1 + 1], prim_name, self._prim_name[:, N2_cor:]))
        #self._dual_name = np.hstack((self._dual_name[:, :N1 + 1], dual_name, self._dual_name[:, N2_cor:]))
        self._dx.replace_matrix(N1 + 1, N2_cor, dx)
        self._dq.replace_matrix(N1 + 1, N2_cor, dq)

    ###@profile
    def get_basis_at(self, place):
        new_mat, new_place = self._base_sequence.get_basis_at(place, self._pivots)
        self._base_sequence.insert_basis(new_mat, new_place)
        return new_mat

    ###@profile
    def get_bases(self, N1, N2):
        new_mat, new_place = self._base_sequence.get_nearby_basis(N1, N2, self._pivots)
        self._base_sequence.insert_basis(new_mat, new_place)
        if new_place == N1:
            return new_mat, self.get_basis_at(N2)
        elif new_place == N2:
            return self.get_basis_at(N1), new_mat
        else:
            raise Exception('Cannot calculate correct bases!')

    ###@profile
    def get_next_basis_for_solution(self, basis, place):
        return self._base_sequence.get_next_basis(basis, place, self._pivots)
