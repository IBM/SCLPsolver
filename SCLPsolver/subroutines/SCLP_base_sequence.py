import numpy as np
from .get_new_dict import calc_nearby_bases
from .lp_tools.pivot import pivot_mn


#TODO: overall idea to speedup this class - replase list of plases to 0,1 array where 0- no dict and 1 has dict
class SCLP_base_sequence():

    def __init__(self, basis, place=0):
        self._bases = [basis]
        self._places = [place]

    @property
    def bases(self):
        return self._bases

    @property
    def places(self):
        return self._places

    def insert_basis(self, basis, place):
        if place not in self._places:
            self._places.append(place)
            self._bases.append(basis)

    def remove_bases(self, N1, N2, pivots, bases_mm, Nnew = None):
        if Nnew is None:
            Nnew = N2 - N1 - 1
        rem_indexes = [i for i,v in enumerate(self._places) if N1 < v < N2]
        rem_places = [self._places.pop(i) for i in reversed(rem_indexes)]
        rem_bases = [self._bases.pop(i) for i in reversed(rem_indexes)]
        bases_mm.add(rem_bases)
        if len(self._places) == 0:
            new_mat, new_place = calc_nearby_bases(N1, N2, pivots, rem_bases, rem_places)
            self._places = [new_place if new_place == N1 else new_place - Nnew]
            self._bases = [new_mat]
        else:
            self._places = [v if v < N2 else v - Nnew for v in self._places]

    def replace_bases(self, N1, N2, Nnew, AAN1, AAN2, bases_mm):
        rem_indexes = [i for i, v in enumerate(self._places) if N1 < v < N2]
        rem_places = [self._places.pop(i) for i in reversed(rem_indexes)]
        rem_bases = [self._bases.pop(i) for i in reversed(rem_indexes)]
        bases_mm.add(rem_bases)
        if len(self._places) == 0:
            if AAN1 is not None:
                self._places = [N1]
                self._bases = [AAN1]
            else:
                self._places = [N1 + Nnew + 1]
                self._bases = [AAN2]
        else:
            self._places = [v if v < N2 else v - (N2 - N1 - 1) + Nnew for v in self._places]

    def get_basis_at(self, place, pivots):
        return self.get_nearby_basis(place, place, pivots)

    def get_next_basis(self, basis, place, pivots, preserve = True):
        if not preserve and place + 1 in self._places:
            return self._bases[self._places.index(place + 1)]
        else:
            return pivot_mn(basis, pivots[place][0], pivots[place][1])

    def get_nearby_place(self, N1, N2):
        result ={'N1':None, 'N2':None, 'N1v': None, 'N2v':None }
        if N1 in self._places:
            result['N1'] = self._places.index(N1)
            result['N1v'] = N1
            t1 = 0
        else:
            test1 = np.fabs(np.asarray(self._places) - N1)
            ind1 = np.argmin(test1)
            result['N1'] = ind1
            result['N1v'] = self._places[ind1]
            t1 = test1[ind1]
        if N2 in self._places:
            result['N2'] = self._places.index(N2)
            result['N2v'] = N2
            t2 = 0
        else:
            test2 = np.fabs(np.asarray(self._places) - N2)
            ind2 = np.argmin(test2)
            t2 = test2[ind2]
            result['N2'] = ind2
            result['N2v'] = self._places[ind2]
        if t1 + N2 - N1 < t2 and N1 in self._places:
            result['N2'] = None
            result['N2v'] = N1
        elif t2 + N2 - N1 < N1 and N2 in self._places:
            result['N1'] = None
            result['N1v'] = N2
        return result

    def get_nearby_place_at(self, at):
        test1 = np.fabs(np.asarray(self._places) - at)
        ind1 = np.argmin(test1)
        return ind1, self._places[ind1]

    def get_nearby_basis(self, N1, N2, pivots):
        if N1 in self._places:
            return self._bases[self._places.index(N1)],N1
        elif N2 in self._places:
            return self._bases[self._places.index(N2)],N2
        else:
            return calc_nearby_bases(N1, N2, pivots, self._bases, self._places)

    def clear_base_sequense(self, numBasesToRemove, maxBases, NN):
        basesActive = len(self._places)
        numBasesToRemove = max(numBasesToRemove, basesActive-maxBases, 0)
        if (numBasesToRemove > 0):
            orderedSequence = sorted(self._places)
            order = sorted(range(len(self._places)), key=lambda i: self._places[i])
            diffSeq = [orderedSequence[1]] + [orderedSequence[i + 2] - p for i, p in
                                              enumerate(orderedSequence[:-2])] + [NN - orderedSequence[-2]]
            if 2 * numBasesToRemove < basesActive:
                candidates = sorted(range(len(diffSeq)), key=lambda i: diffSeq[i])[:2 * numBasesToRemove + 1]
                to_remove = [candidates[0]]
                for i in range(1, len(candidates)):
                    if candidates[i] - candidates[i - 1] > 1 or candidates[i - 1] not in to_remove:
                        to_remove.append(candidates[i])
                    if len(to_remove) >= numBasesToRemove:
                        break
                self._bases = [self._bases[p] for i, p in enumerate(order) if i not in to_remove]
                self._places = [self._places[p] for i, p in enumerate(order) if i not in to_remove]

    def check_places(self):
        return len(self._places) == len(set(self._places))

    def keep_only_one(self):
        self._places = [self._places[0]]
        self._bases = [self._bases[0]]

