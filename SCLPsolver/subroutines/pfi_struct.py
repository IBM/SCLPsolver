


class pfi_struct():

    __slots__ = ['_col_list', '_prim_vars', '_row_list', '_dual_vars', '_prim_inv_basis', '_dual_inv_basis', '_dict', '_pivots']

    # should return row of the simplex dictionary performing sequence of ftran operations
    def get_dict_row_at(self, n):
        pass

    # should return column of the simplex dictionary performing sequence of ftran operations
    def get_dict_col_at(self, n):
        pass

    # should return primal variables performing sequence of ftran operations
    def get_prim_vars_at(self, n):
        pass

    # should return dual variables performing sequence of ftran operations
    def get_dual_vars_at(self, n):
        pass

    # should remove data between n1 and n2 positions
    def remove_data(self, n1, n2):
        pass

    # should replace data between n1 and n2 positions one new
    def replace_to_one(self, n1, n2, col, row):
        pass

    # should replace data between n1 and n2 positions many
    def replace_to_many(self, n1, n2, struct):
        pass