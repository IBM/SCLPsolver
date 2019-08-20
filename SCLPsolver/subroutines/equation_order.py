

class equation_order():

    __slots__ = ['_out_bases', '_var_names']

    def __init__(self):
        self._out_bases = []
        self._var_names = []

    def remove(self, n1, n2, var_name=None):
        if var_name is not None:
            ind_v = self._var_names.index(var_name, n1, n2 + 1)
        else:
            if n1 == -1:
                ind_v = self._out_bases.index(n2)
            else:
                ind_v = self._out_bases.index(n1)
        for i, v in enumerate(self._out_bases):
            if i == ind_v:
                self._out_bases[i] = n1 + 1
            else:
                if v > n2:
                    self._out_bases[i] = v - n2 + n1 + 1
                elif v >= n1:
                    self._out_bases[i] = -1
                    self._var_names[i] = 0

    def insert(self, n1, var_names):
        if n1 != -1 and n1 in self._out_bases:
            ind_v = var_names.index(self._var_names[self._out_bases.index(n1)])
            corr = 0
        else:
            ind_v = None
            corr = 1
        m = 0
        for i, v in enumerate(self._out_bases):
            if v == -1:
                if m < len(var_names):
                    if m != ind_v:
                        self._out_bases[i] = n1 + m + corr
                        self._var_names[i] = var_names[m]
                    m += 1
            elif v > n1:
                self._out_bases[i] = v + len(var_names)
            elif v == n1 and ind_v is not None:
                self._out_bases[i] = n1 + ind_v
        for j in range(m, len(var_names)):
            if j != ind_v:
                self._out_bases.append(n1 + j + corr)
                self._var_names.append(var_names[j])

    # var_names include all out_pivots (both n1-> and ->n2)
    def replace(self, n1, n2, v1, v2, var_names):
        ind_v1 = var_names.index(v1)
        ind_v2 = var_names.index(v2)
        num_to_add = len(var_names) - (n2-n1+1)
        m = 0
        for i, v in enumerate(self._out_bases):
            if v == -1:
                if m < num_to_add:
                    if m != ind_v1 and m != ind_v2 :
                        self._out_bases[i] = n1 + m
                        self._var_names[i] = var_names[m]
                    m += 1
            elif v >= n2:
                self._out_bases[i] = v + len(var_names) - 2
            elif v >= n1:
                if self._var_names[i] == v1:
                    self._out_bases[i] = n1 + ind_v1
                elif self._var_names[i] == v2:
                    self._out_bases[i] = n1 + ind_v2
                elif m < len(var_names):
                    self._out_bases[i] = n1 + m
                    self._var_names[i] = var_names[m]
                    m += 1
        for j in range(m, len(var_names)):
            self._out_bases.append(n1 + j)
            self._var_names.append(var_names[j])
