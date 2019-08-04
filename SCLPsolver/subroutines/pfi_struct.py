import numpy as np
import timeit

class pfi_struct:
    # simplex_dict - matrix
    # prim_names - vector
    # dual_names - vector
    # place - scalar - place of the matrix in the base sequence
    # pivots - object of the pivot_storage class (store names of entering and leaving variables)
    # eta_rows - eta vectors to perform pivoting on dual variables and matrix rows
    # eta_cols - eta vectors to perform pivoting on primal variables and matrix columns

    # __slots__ = ['simplex_dict', 'prim_names', 'dual_names', 'place', 'pivots', 'eta_rows', 'eta_cols']

    def __init__(self,simplex_dict, prim_names, dual_names, place, eta_rows, eta_cols, pivots):
        self.simplex_dict = simplex_dict
        self.prim_names = prim_names
        self.dual_names = dual_names
        self.place = place
        self.eta_rows = eta_rows
        self.eta_cols = eta_cols
        self.pivots = pivots

    def get_dict(self, n, var_name, names_vector, eta_vector, use_row):
        # 1 choose from a row/column from the matrix (taking the values vector) based on the index of the prim_names that
        # correspond to the var_name

        # 2 take the corresponding eta row based on the order in the vector
        result = None
        index = 0
        for eta in eta_vector:
            # 3 push these inputs into the ftran() function



            if result == None:
                index_to_pivot = np.where(names_vector == var_name)[0][0]
                if use_row:
                    values_vector = self.simplex_dict[index_to_pivot, :]
                else:
                    values_vector = self.simplex_dict[:, index_to_pivot]
                pivot = self.pivots[self.place]
                # check if this pivot[0] or pivot[1]
                index_of_pivot = np.where(self.prim_names == pivot[0])[0][0]
                result = ftran(self.prim_names, values_vector, eta, index_of_pivot, pivot[1])
            else:
                names_vector = result[0]
                values_vector = result[1]
                pivot = self.pivots[self.place + index]
                # check if this pivot[0] or pivot[1]
                index_of_pivot = np.where(self.prim_names == pivot[0])[0][0]
                result = ftran(names_vector, values_vector, eta, index_of_pivot, pivot[1])

            # 4 output of the ftran should be fed again to the ftran as input until iteration == n-place
            index += 1
            if (index <= n - self.place):
                break

        return result

    # should return row of the simplex dictionary performing sequence of ftran operations
    # n-place number of operations to perform
    # varname is an element of primal variable we should take index+1 that indicates row of the matrix
    def get_dict_row_at(self, n, var_name):
        return self.get_dict(n, var_name, self.prim_names, self.eta_rows, True)

    # same for columns
    def get_dict_col_at(self, n, var_name):
        # same as above but using the eta_cols and the column of the matrix, and using dual_names instead of prim_names
        pass

    # same for first column of matrix
    def get_prim_vars_at(self, n):
        # similar to 1st method but using the 1st column of the matrix
        pass

    # same for first row of matrix
    def get_dual_vars_at(self, n):
        # similar to 1st method but using the 1st row of the matrix
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


def ftran(names_vector, values_vector, eta_vector, pivot_index, entering_var_name):
    t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')

    # handle primal names vector
    index_of_location_to_insert_entering_variable = np.searchsorted(names_vector, entering_var_name)
    pivot_element_value = values_vector[pivot_index] * eta_vector[pivot_index]
    values_vector += values_vector[pivot_index] * eta_vector

    if index_of_location_to_insert_entering_variable > pivot_index:
        # handle names vector
        names_vector[pivot_index: index_of_location_to_insert_entering_variable - 1] = names_vector[pivot_index + 1: index_of_location_to_insert_entering_variable]
        names_vector[index_of_location_to_insert_entering_variable - 1] = entering_var_name

        # handle values vector
        values_vector[pivot_index: index_of_location_to_insert_entering_variable - 1] = values_vector[pivot_index + 1: index_of_location_to_insert_entering_variable]
        values_vector[index_of_location_to_insert_entering_variable - 1] = pivot_element_value
    else:
        # handle names vector
        names_vector[index_of_location_to_insert_entering_variable] = entering_var_name
        names_vector[index_of_location_to_insert_entering_variable + 1: pivot_index] = names_vector[index_of_location_to_insert_entering_variable: pivot_index]

        # handle values vector
        values_vector[index_of_location_to_insert_entering_variable] = pivot_element_value
        values_vector[index_of_location_to_insert_entering_variable + 1: pivot_index] = values_vector[index_of_location_to_insert_entering_variable: pivot_index]

    print('time taken in milliseconds =', t.timeit()/1000)

    print('new_primal_names_vector =', names_vector)
    print('new_primal_values_vector =', values_vector)

    return [names_vector, values_vector]

pfi_instance = pfi_struct(np.asarray([[1, 2],[ 3, 4]]),np.asarray([1, 2]), np.asarray([3, 4]), 2, np.asarray([[1, 2],[3, 4]]), np.asarray([[1, 2],[3, 4]]))
print(pfi_instance.get_dict_row_at(1, 2))
