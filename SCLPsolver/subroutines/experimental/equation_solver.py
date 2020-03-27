import numpy as np
from subroutines.experimental.equation_order import equation_order
from subroutines.experimental.generic_equation_solver import generic_equation_solver
from subroutines.matlab_utils import find

class equation_solver(generic_equation_solver):

    def __init__(self, alloc_size, steps_to_reinvert=10):
        super().__init__(alloc_size, steps_to_reinvert)
        self._eq_order = equation_order()
        self.rhs = None
        self.drhs = None
        self._raw_dtau = None

    def update_caseIII(self, param_line, klist, jlist, pivots, dx, dq, n1, var_names):
        matrix, rhs, drhs = build_equations(param_line, klist, jlist, pivots, dx, dq)
        if self._steps + len(var_names) > self._steps_to_reinvert:
            self.reinvert(matrix)
            self._raw_dtau = np.dot(self._inv_matrix.get_matrix(), drhs)
            return self._raw_dtau
        else:
            self.insert_equations(matrix, n1, var_names)
            self._col_order = self._eq_order.col_order
            self._raw_dtau = self.raw_resolve(drhs)
            return self.vector_order(self._raw_dtau)

    def update_caseI(self, param_line, klist, jlist, pivots, dx, dq, n1, n2, var_name):
        if self._steps + n2 - n1 > self._steps_to_reinvert:
            matrix, rhs, drhs = build_equations(param_line, klist, jlist, pivots, dx, dq)
            self.reinvert(matrix)
        else:
            self.remove_equations(n1, n2, var_name)
            self._col_order = self._eq_order.col_order
            if param_line.is_main():
                drhs = np.zeros(len(self._eq_order.col_order))
                drhs[0] = 1
                self._raw_dtau = self._resolve(drhs)
            else:
                matrix, rhs, drhs = build_equations(param_line, klist, jlist, pivots, dx, dq)
                self._raw_dtau = self.raw_resolve(drhs)
            return self.vector_order(self._raw_dtau)

    def update_caseII(self, param_line, klist, jlist, pivots, dx, dq, n1, n2, v1, v2, var_names):
        matrix, rhs, drhs = build_equations(param_line, klist, jlist, pivots, dx, dq)
        # TODO: check this condition
        if self._steps + n2 - n1 + max(len(var_names) - 2, 0) > self._steps_to_reinvert:
            self.reinvert(matrix)
        else:
            replace_only = self.replace_equations(matrix, n1, n2, v1, v2, var_names)
            self._col_order = self._eq_order.col_order
            if replace_only:
                self._raw_dtau = self.update_solution(self._raw_dtau, n2-n1-1)
            else:
                self._raw_dtau = self.raw_resolve(drhs)
            return self.vector_order(self._raw_dtau)

    def insert_equations(self, matrix, n1, var_names):
        rows_to_insert, cols_to_insert, enlarge_count = self._eq_order.insert(n1, var_names)
        self._inv_matrix.enlarge(enlarge_count)
        self.insert_cols_and_rows(matrix, rows_to_insert, cols_to_insert)

    def replace_equations(self, matrix, n1, n2, v1, v2, var_names):
        cols_to_replace, cols_to_ar, rows_to_ar, need_to_add, enlarge_count = self._eq_order.replace(n1, n2, v1, v2, var_names)
        for j in cols_to_replace:
            # run on columns
            m_col_index = self._eq_order.col_order[j]
            result = self.reverse_vector_order(matrix[1:,m_col_index], self._eq_order.out_bases, 1)
            self._replace_column(j, result)
        if need_to_add:
            self._inv_matrix.enlarge(enlarge_count)
            self.insert_cols_and_rows(matrix, rows_to_ar, cols_to_ar)
        else:
            self.remove_cols_and_rows(cols_to_ar, rows_to_ar)
        return len(cols_to_ar) == 0

    def remove_equations(self, n1, n2, var_name):
        rows_to_remove, cols_to_remove = self._eq_order.remove(n1, n2, var_name)
        self.remove_cols_and_rows(cols_to_remove, rows_to_remove)

    def remove_cols_and_rows(self, cols_to_remove, rows_to_remove):
        size = len(self._eq_order.col_order)
        for i, r in enumerate(rows_to_remove):
            col = np.zeros(size)
            col[r] = 1
            row = np.zeros(size)
            row[cols_to_remove[i]] = 1
            self._replace_equation(r, cols_to_remove[i], row, col)

    def insert_cols_and_rows(self, matrix, rows, cols):
        for i, r in enumerate(rows):
            # run on rows
            m_row_index = self._eq_order.out_bases[r]
            row_result = self.reverse_vector_order(matrix[m_row_index,:], self._eq_order.col_order)
            m_col_index = self._eq_order.col_order[cols[i]]
            col_result = self.reverse_vector_order(matrix[1:,m_col_index], self._eq_order.out_bases, 1)
            self._replace_equation(r, cols[i], row_result, col_result)

def build_equations(param_line, klist, jlist, pivots, dx, dq):
    NN = len(pivots) + 1
    coeff = np.zeros((NN, NN))
    rhs = np.zeros(NN)
    drhs = np.zeros(NN)
    coeff[0, :] = np.ones(NN)
    rhs[NN - 1] = param_line.T
    drhs[NN - 1] = param_line.del_T
    for n in range(NN - 1):
        vv = pivots[n][0]
        if vv > 0:
            k = find(klist == vv)[0]
            prev_in = pivots.get_previous_in(n)
            if prev_in is not None:
                coeff[n+1, prev_in + 1:n + 1] = dx[k, prev_in + 1:n + 1]
            else:
                coeff[n+1, 0:n + 1] = dx[k, 0:n + 1]
                rhs[n+1] = -param_line.x_0[k]
                if param_line.del_x_0 is not None:
                    drhs[n+1] = -param_line.del_x_0[k]
        else:
            j = find(jlist == -vv)[0]
            next_in = pivots.get_next_in(n)
            if next_in is not None:
                coeff[n+1, n + 1:next_in + 1] = dq[j, n + 1:next_in + 1]
            else:
                coeff[n+1, n + 1:] = dq[j, n + 1:]
                rhs[n+1] = -param_line.q_N[j]
                if param_line.del_q_N is not None:
                    drhs[n+1] = -param_line.del_q_N[j]
    return coeff, rhs, drhs