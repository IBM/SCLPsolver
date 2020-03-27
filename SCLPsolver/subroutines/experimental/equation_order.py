import numpy as np


class equation_order():

    # To identify equations (rows) we use 2 parameters:
    #   var_names: names of variables that leave basis providing new equation
    #   out_bases: basis number after which variable leave
    # To identify columns we still using col_order
    __slots__ = ['_out_bases', '_var_names', '_col_order']

    def __init__(self, row_data = None):
        if row_data is not None:
            self._out_bases = list(range(len(row_data)))
            self._var_names = row_data.copy()
            self._col_order = list(range(len(row_data)+1))
        else:
            self._out_bases = []
            self._var_names = []
            self._col_order = [0]

    @property
    def out_bases(self):
        return self._out_bases

    @property
    def var_names(self):
        return self._var_names

    @property
    def col_order(self):
        return self._col_order

    # This handles collision type I: we need to remove all bases between n1 and n2
    # That is all columns between n1 and n2 should be removed
    # Also we need to remove corresponding equations (rows)
    # There are 2 main cases:
    #   1. bases at the beginning or bases at the end should be removed (n1 == -1 or n2 not in self._col_order)
    #   2. bases in the middle should be removed: in this case var_name is a variable leaving on pivot n1->n2 after removal
    # Returns indexes of rows and columns that should be removed
    def remove(self, n1, n2, var_name=None):
        rows_to_remove = []
        cols_to_remove = []
        for i, v in enumerate(self._col_order):
            if v > n2:
                self._col_order[i] = v - n2 + n1 + 1
            elif v > n1: #TODO the comparison on the left is not the same as the one in 58 - is this a bug?
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
                elif v >= n1: #TODO the comparison on the left is not the same as the one in 42 - is this a bug?
                    self._out_bases[i] = -1
                    rows_to_remove.append(i)
                    self._var_names[i] = 0
        return rows_to_remove, cols_to_remove

    # This handles collision type III: we need to insert bases between n1 and n1+1
    # That is we need to insert columns between n1 and n1+1
    # Also we need to insert corresponding equations (rows)
    # There are 2 main cases:
    #   1. we need to insert bases at the beginning or bases at the end (n1 == -1 or n1 not in self._out_bases)
    #   2. we need to insert bases in the middle
    # var_names handles variables leaving on pivots n1->n1+1, n1+1->n1+2,..., n1+m->n2 after insertion
    # Returns indexes of rows and columns that should be inserted
    def insert(self, n1, var_names):
        enlarge_count = 0
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
            enlarge_count +=1
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
        return rows_to_insert, cols_to_insert, enlarge_count

    # This handles collision type II: we need to replace bases between n1 and n2
    # The number of new bases could be less or greater then number of old bases (n2 - n1 - 1)
    # var_names include all leaving variable names n1->n1+1, n1+1->n1+2,..., n1+m->n2 after replacement
    # v1 and v2 includes names of two variables that are differs between n1 and n2 before (and after) replacement
    # this helps to identify equations (rows) that should not be replaced
    # Returns:
    #   cols_to_replace - indexes of columns that should be replaced
    #   cols_to_ar - indexes of columns that should be inserted or removed
    #   rows_to_ar - indexes of rows that should be replaced or removed
    #   need_to_add; True/False if we need to add rows and columns
    def replace(self, n1, n2, v1, v2, var_names):
        enlarge_count = 0
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
            enlarge_count += 1
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
        return cols_to_replace, cols_to_ar, rows_to_ar, need_to_add, enlarge_count
