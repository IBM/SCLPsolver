from typing import Iterator, overload, Iterable, List
from collections import Counter
import numpy as np


class pivot_iterator(Iterator):

    def __init__(self, iter, reversed = False):
        self._iterable = iter
        self._reversed = reversed
        if not self._reversed:
            self._current = 0
        else:
            self._current = len(self._iterable)

    def __next__(self):
        if not self._reversed:
            if self._current >= len(self._iterable):
                raise StopIteration
            else:
                self._current += 1
                return self._iterable.__getitem__(self._current - 1)
        else:
            if self._current <= 0:
                raise StopIteration
            else:
                self._current -= 1
                return self._iterable.__getitem__(self._current)

    def __iter__(self):
        return self



class pivot_storage(list):

    def __init__(self, outpivots = None, inpivots= None):
        super().__init__()
        if inpivots is None:
            self._in = []
            self._out = []
        else:
            self._in = inpivots
            self._out = outpivots

    def copy(self):
        return pivot_storage(self._out.copy(),self._in.copy())

    @property
    def inpivots(self):
        return self._in

    @property
    def outpivots(self):
        return self._out

    def clear(self) -> None:
        self._in.clear()
        self._out.clear()

    def append(self, object: list) -> None:
        self._in.append(object[1])
        self._out.append(object[0])

    def extend(self, other) -> None:
        self._in.extend(other.inpivots)
        self._out.extend(other.outpivots)

    def insert(self, index: int, object) -> None:
        self._in.insert(index, object[1])
        self._out.insert(index, object[0])

    def reverse(self) -> None:
        self._in.reverse()
        self._out.reverse()

    def __len__(self) -> int:
        return len(self._out)

    def __iter__(self):
        return pivot_iterator(self)

    @overload
    def __getitem__(self, i: int):
        return [self._out[i], self._in[i]]

    @overload
    def __getitem__(self, s: slice):
        return pivot_storage(self._out.__getitem__(s), self._in.__getitem__(s))

    def __getitem__(self, i: int):
        if isinstance(i, slice):
            return pivot_storage(self._out.__getitem__(i), self._in.__getitem__(i))
        else:
            return [self._out[i], self._in[i]]

    @overload
    def __setitem__(self, i: slice, o) -> None:
        self._in.__setitem__(i, o.inpivots)
        self._out.__setitem__(i, o.outpivots)

    @overload
    def __setitem__(self, s: slice, o) -> None:
        self._in.__setitem__(s, o[1])
        self._out.__setitem__(s, o[0])

    def __setitem__(self, i: int, o) -> None:
        if isinstance(i, slice):
            self._in.__setitem__(i, o.inpivots)
            self._out.__setitem__(i, o.outpivots)
        else:
            self._in.__setitem__(i, o[1])
            self._out.__setitem__(i, o[0])

    def __delitem__(self, i) -> None:
        self._in.__delitem__(i)
        self._out.__delitem__(i)

    def __add__(self, other):
        return pivot_storage(self._out.__add__(other.outpivots), self._in.__add__(other.inpivots))

    def __contains__(self, o) -> bool:
        for i, x in enumerate(self._out):
            if x == o[0]:
                if self._in[i] == o[1]:
                    return True
        return False

    def __reversed__(self):
        return pivot_iterator(self, True)

    def get_difference(self, N1, N2):
        diff = Counter(self._out[N1:N2]) - Counter(self._in[N1:N2])
        return list(diff.elements())

    def remove_pivots(self, N1, N2):
        c1 = Counter(self._in[N1:N2])
        c2 = Counter(self._out[N1:N2])
        diff1 = c1 - c2
        diff2 = c2 - c1
        if N1 >=0:
            if N2 < len(self._in):
                self._in = self._in[:N1]+list(diff1.elements())+self._in[N2:]
                self._out = self._out[:N1] + list(diff2.elements()) + self._out[N2:]
            elif N2 == len(self._in):
                self._in = self._in[:N1] + list(diff1.elements())
                self._out = self._out[:N1] + list(diff2.elements())
            else:
                self._in = self._in[:N1]
                self._out = self._out[:N1]
        else:
            self._in = self._in[N2:]
            self._out = self._out[N2:]

    def get_prim_name_at0(self, place, name):
        if place == 0:
            return name
        else:
            c1 = Counter(self._in[:place])
            c2 = Counter(self._out[:place])
            diff1 = c1 - c2
            diff2 = c2 - c1
            a1 = np.setdiff1d(name,np.asarray(list(diff1.elements())), assume_unique = True)
            a2 = np.union1d(a1, np.asarray(list(diff2.elements())))
            return a2

    def get_prim_name_atN(self, place, name):
        if place == len(self._in):
            return name
        else:
            c1 = Counter(self._in[place-1:])
            c2 = Counter(self._out[place-1:])
            diff1 = c1 - c2
            diff2 = c2 - c1
            a1 = np.setdiff1d(name,np.asarray(list(diff2.elements())), assume_unique = True)
            a2 = np.union1d(a1, np.asarray(list(diff1.elements())))
            return a2

    def replace_pivots(self, N1, N2, pivots):
        if N1 >= 0:
            self._in = self._in[:N1] + pivots.inpivots + self._in[N2:]
            self._out = self._out[:N1] + pivots.outpivots + self._out[N2:]
        else:
            self._in =  pivots.inpivots + self._in[N2:]
            self._out = pivots.outpivots + self._out[N2:]



