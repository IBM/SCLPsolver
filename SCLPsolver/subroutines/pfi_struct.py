


class pfi_struct():

    # simplex_dict - matrix
    # prim_names - vector
    # dual_names - vector
    # place - scalar - place of the matrix in the base sequence
    # pivots - object of the pivot_storage class (store nnames of entering and leaving variables)
    # eta_rows - eta vectors to perform pivoting on dual variables and matrix rows
    # eta_cols - eta vectors to perform pivoting on primal variables and matrix columns
    __slots__ = ['_simplex_dict','_prim_names', '_dual_names', '_place', '_pivots', '_eta_rows', '_eta_cols']

    # should return row of the simplex dictionary performing sequence of ftran operations
    # n-place number of operations to perform
    # var_name  of primal variable which index+1 indicates row of the matrix
    def get_dict_row_at(self, n, var_name):
        pass

    # should return column of the simplex dictionary performing sequence of ftran operations
    def get_dict_col_at(self, n, var_name):
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