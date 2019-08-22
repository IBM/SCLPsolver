import numpy as np


class equation_order():

    __slots__ = ['_out_bases', '_var_names', '_col_order']

    def __init__(self):
        self._out_bases = []
        self._var_names = []
        self._col_order = []

    def remove(self, n1, n2, var_name=None):
        rows_to_remove = []
        cols_to_remove = []
        for i, v in enumerate(self._col_order):
            if v > n2:
                self._col_order[i] = v - n2 + n1 + 1
            elif v > n1:
                self._col_order[i] = -1
                cols_to_remove.append(i)
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
                    rows_to_remove.append(i)
                    self._var_names[i] = 0
        return rows_to_remove, cols_to_remove

    # def insert_row_to_cols(self, vv, dx, dq, klist, jlist, pivots, cols, n1, n2, n):
    #     if vv > 0:
    #         k = find(klist == vv)[0]
    #         prev_in = pivots.get_previous_in(n)
    #         if prev_in is None:
    #             prev_in = -1
    #         start = max(n1 + 1, prev_in + 1)
    #         end = n + 1
    #         if start < end:
    #             cols[n, start-n1:end-n1] = dx[k, start:end]
    #     else:
    #         j = find(jlist == -vv)[0]
    #         next_in = pivots.get_next_in(n)
    #         if next_in is None:
    #             next_in = n2 -1
    #         start = n + 1
    #         end = min(next_in + 1, n2)
    #         if start < end:
    #             cols[n, start-n1:end-n1] = dq[j, start:end]

    # def insert_at_start(self, var_names):
    #     m = 0
    #     n1 = -1
    #     corr = 1
    #     cols_to_insert = []
    #     rows_to_insert = []
    #     cols = np.zeros((len(self._col_order)+len(var_names) - 1 + corr,len(var_names) - 1 + corr))
    #     cols[0,:] = np.ones(len(var_names) - 1 + corr)
    #     rows = np.zeros((len(var_names) - 1 + corr,len(self._col_order)+len(var_names) - 1 + corr))
    #     for i, v in enumerate(self._col_order):
    #         if v == -1:
    #             if m < len(var_names):
    #                 m += 1
    #                 self._col_order[i] = n1 + m
    #                 cols_to_insert.append(i)
    #         elif v > n1:
    #             self._col_order[i] = v + len(var_names) - 1 + corr
    #     for j in range(m, len(var_names) - 1 + corr):
    #         cols_to_insert.append(len(self._col_order))
    #         self._col_order.append(n1 + 1 + j)
    #     m = 0
    #     ind_v = None
    #     for i, v in enumerate(self._out_bases):
    #         if v == -1:
    #             if m == ind_v:
    #                 m += 1
    #             if m < len(var_names):
    #                 self._out_bases[i] = n1 + m + corr
    #                 self._var_names[i] = var_names[m]
    #                 rows_to_insert.append(i)
    #                 #self.insert_row_to_cols(self._var_names[i], dx, dq, klist, jlist, pivots, cols, n1, n1+len(var_names) - 1 + corr, n1 + m + corr)
    #                 m += 1
    #         elif v > n1:
    #             self._out_bases[i] = v + len(var_names) - 1 + corr
    #         elif v == n1 and ind_v is not None:
    #             self._out_bases[i] = n1 + ind_v
    #     for j in range(m, len(var_names) - 1 + corr):
    #         if j != ind_v:
    #             rows_to_insert.append(len(self._out_bases))
    #             self._out_bases.append(n1 + j + corr)
    #             self._var_names.append(var_names[j])
    #             #self.insert_row_to_cols(var_names[j], dx, dq, klist, jlist, pivots, cols, n1, n1 + len(var_names) - 1 + corr, n1 + j + corr)
    #     return rows_to_insert, cols_to_insert


    def insert(self, n1, var_names):
        cols_to_insert = []
        rows_to_insert = []
        if n1 != -1 and n1 in self._out_bases:
            ind_v = var_names.index(self._var_names[self._out_bases.index(n1)])
            corr = 0
        else:
            ind_v = None
            corr = 1
        m = 0
        for i, v in enumerate(self._col_order):
            if v == -1:
                if m < len(var_names):
                    m += 1
                    self._col_order[i] = n1 + m
                    cols_to_insert.append(i)
            elif v > n1:
                self._col_order[i] = v + len(var_names) - 1 + corr
        for j in range(m, len(var_names) - 1 + corr):
            cols_to_insert.append(len(self._col_order))
            self._col_order.append(n1 + j + 1)
        m = 0
        for i, v in enumerate(self._out_bases):
            if v == -1:
                if m == ind_v:
                    m += 1
                if m < len(var_names):
                    self._out_bases[i] = n1 + m + corr
                    self._var_names[i] = var_names[m]
                    rows_to_insert.append(i)
                    m += 1
            elif v > n1:
                self._out_bases[i] = v + len(var_names) - 1 + corr
            elif v == n1 and ind_v is not None:
                self._out_bases[i] = n1 + ind_v
        for j in range(m, len(var_names) - 1 + corr):
            if j != ind_v:
                rows_to_insert.append(len(self._out_bases))
                self._out_bases.append(n1 + j + corr)
                self._var_names.append(var_names[j])
        return rows_to_insert, cols_to_insert

    # ar_names include all out_pivots (both n1-> and ->n2)
    def replace(self, n1, n2, v1, v2, var_names):
        cols_to_replace = []
        cols_to_ar = []
        rows_to_ar = []
        ind_v1 = var_names.index(v1)
        ind_v2 = var_names.index(v2)
        num_to_add = len(var_names) - (n2-n1+1)
        need_to_add = num_to_add > 0
        m = 0
        for i, v in enumerate(self._col_order):
            if v == -1:
                if m < num_to_add:
                    m += 1
                    self._col_order[i] = n1 + m
                    cols_to_ar.append(i)
            elif n1 < v < n2:
                if v < n2 + num_to_add:
                    m += 1
                    self._col_order[i] = n1 + m
                    cols_to_replace.append(i)
                else:
                    self._col_order[i] = -1
                    cols_to_ar.append(i)
        for j in range(m, len(var_names)):
            cols_to_ar.append(len(self._col_order))
            self._col_order.append(n1 + j)
        m = 0
        for i, v in enumerate(self._out_bases):
            if v == -1:
                if m == ind_v1 or m == ind_v2:
                    m += 1
                    # This not a bug! This correct situation when ind_v1 == ind_v2+-1 !
                    if m == ind_v1 or m == ind_v2:
                        m += 1
                if m < num_to_add:
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
                else:
                    if m < len(var_names):
                        self._out_bases[i] = n1 + m
                        self._var_names[i] = var_names[m]
                        m += 1
                    else:
                        self._out_bases[i] = -1
                        self._var_names[i] = 0
                        rows_to_ar.append(i)
        for j in range(m, len(var_names)):
            rows_to_ar.append(len(self._out_bases))
            self._out_bases.append(n1 + j)
            self._var_names.append(var_names[j])
        return cols_to_replace, cols_to_ar, rows_to_ar, need_to_add