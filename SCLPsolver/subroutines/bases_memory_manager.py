class bases_memory_manager():

    def __init__(self, max_bases = 3):
        self.max_bases = max_bases
        self._bases = []

    def add(self, bases):
        for i in range(min(len(bases), self.max_bases - len(self._bases))):
            self._bases.append(bases[i])

    def pop(self):
        if len(self._bases) > 0:
            return self._bases.pop(0)
        else:
            return None