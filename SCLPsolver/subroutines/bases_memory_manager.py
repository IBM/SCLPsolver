import numpy as np


class bases_memory_manager():

    def __init__(self, pl, dl, max_bases = 3):
        self.max_bases = max_bases
        self._bases = []
        self.ps = np.zeros(pl, dtype=np.int32, order='C')
        self.ds = np.zeros(dl, dtype=np.int32, order='C')

    def add(self, bases):
        for i in range(min(len(bases), self.max_bases - len(self._bases))):
            self._bases.append(bases[i])

    def pop(self):
        if len(self._bases) > 0:
            return self._bases.pop(0)
        else:
            return None