from .get_new_dict import get_new_dict
from .lp_tools.pivot import pivot_mn

class SCLP_base_sequence():

    def __init__(self, basis):
        self._bases = [basis]
        self._num_bases = 1

    @property
    def bases(self):
        return self._bases

    @property
    def num_bases(self):
        return self._num_bases

    def insert_basis(self, basis, place):
        if self._bases[place] is None:
            self._bases[place] = basis
            self._num_bases += 1

    def remove_bases(self, N1, N2, pivots, bases_mm, Nadd = 0):
        rem_bases = [self._bases.pop(i) for i in range(N2-1, N1, -1)]
        rem_places = [N2-i-1 for i,v in enumerate(rem_bases) if v is not None]
        rem_bases = [v for v in rem_bases if v is not None]
        bases_mm.add(rem_bases)
        if len(rem_bases) == self._num_bases:
            last_place = rem_places[-1]
            first_place = rem_places[0]
            if N1 >= 0:
                if N2 <= len(pivots):
                    if N2 - last_place < first_place - N1:
                        self._bases[N1+1] = get_new_dict(rem_bases[-1], last_place, N2, pivots)
                    else:
                        self._bases[N1] = get_new_dict(rem_bases[0], first_place, N1, pivots)
                else:
                    self._bases[N1] = get_new_dict(rem_bases[0], first_place, N1, pivots)
            else:
                self._bases[N1 + 1] = get_new_dict(rem_bases[-1], last_place, N2, pivots)
            self._num_bases = 1
        else:
            self._num_bases -= len(rem_bases)
        #this for a case when called from solution.rewind
        if Nadd > 0:
            self._bases[N1+1:N1+1] = [None] * Nadd

    def replace_bases(self, N1, N2, Nnew, AAN1, AAN2, bases_mm):
        rem_bases = [self._bases.pop(i) for i in range(N2-1, N1, -1) if self._bases[i] is not None]
        bases_mm.add(rem_bases)
        Nadd = Nnew - (N2 - N1 - 1 - len(rem_bases))
        if Nadd > 0:
            self._bases[N1+1:N1+1] = [None] * Nadd
        else:
            del self._bases[N1+1:N1+1-Nadd]
        if len(rem_bases) == self._num_bases:
            if AAN1 is not None:
                self._bases[N1] = AAN1
            else:
                self._bases[N1 + Nnew + 1] = AAN2
            self._num_bases = 1
        else:
            self._num_bases -= len(rem_bases)

    def get_basis_at(self, place, pivots):
        return self.get_nearby_basis(place, place, pivots)

    def get_next_basis(self, basis, place, pivots, preserve = True):
        exist_basis = self._bases[place+1]
        if not preserve and exist_basis is not None:
            return exist_basis
        else:
            return pivot_mn(basis, pivots[place][0], pivots[place][1])

    def get_nearby_basis_at0(self):
        return next((i,b) for i, b in enumerate(self._bases) if b is not None)

    def get_nearby_basis_atN(self):
        return next((-i,b) for i, b in enumerate(reversed(self._bases)) if b is not None)

    def get_nearby_basis(self, N1, N2, pivots):
        basis_N1 = self._bases[N1]
        if basis_N1 is not None:
            return basis_N1, N1
        elif self._bases[N2] is not None:
            return self._bases[N2], N2
        else:
            res1 = next(((i,b) for i, b in enumerate(self._bases[N2+1:]) if b is not None), (2*len(self._bases), None))
            res2 = next(((i, b) for i, b in enumerate(reversed(self._bases[:N2])) if b is not None), (2*len(self._bases), None))
            if res1[0] <= res2[0]:
                #print('New1:', N2 + res1[0] + 1)
                old_place = N2 + res1[0] + 1
                if N1<old_place<N2:
                    self._bases[old_place] = None
                    self._num_bases -= 1
                    return get_new_dict(res1[1], old_place, N2, pivots, False), N2
                else:
                    return get_new_dict(res1[1], old_place, N2, pivots), N2
            else:
                #print('New2:', N2 - res2[0] - 1)
                old_place = N2 - res2[0] - 1
                if N1 < old_place < N2:
                    self._bases[old_place] = None
                    self._num_bases -= 1
                    return get_new_dict(res2[1], old_place, N2, pivots, False), N2
                else:
                    return get_new_dict(res2[1], old_place, N2, pivots), N2

    # rewrite
    def clear_base_sequense(self, numBasesToRemove, maxBases, NN):
        pass

    def keep_only_one(self):
        n, b = self.get_nearby_basis_atN()
        self._bases = [None] * len(self._bases)
        self._bases[n-1] = b
        self._num_bases = 1

    def check_places(self, places):
        if len(places) != self._num_bases:
            raise Exception('Num bases')
        else:
            for p in places:
                if self._bases[p] is None:
                    raise Exception('Not same')

    def check_bases_num(self):
        bases_num = sum([1 for basis in self._bases if basis is not None])
        if self._num_bases != bases_num:
            print('here')
