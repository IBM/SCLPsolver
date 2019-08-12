import numpy as np
import subroutines.matrix as mm

class equation_solver():

    def __init__(self, alloc_size):
        self._steps = 0
        self._eta_rows = []
        self._eta_cols = []
        self._row_places = []
        self._col_places = []
        self._matrix = mm.matrix(1, alloc_size)
        self._inv_matrix = mm.matrix(1, alloc_size)

    def add_equation(self, n_row, n_col, row, col):
        self._steps += 1
        pass

    def remove_equation(self, n_row, n_col):
        self._steps += 1
        vcol = 1
        vrow = 1
        #looks like this not correct
        for i, r in enumerate(self._eta_rows):
            vcol *= self._eta_rows[self._row_places[i]]
            vrow *= self._eta_cols[self._col_places[i]]
        col = self._inv_matrix.get_matrix()[:, n_col] * vcol
        row = self._inv_matrix.get_matrix()[n_row, :] * vrow
        for i, c in enumerate(self._eta_cols):
            col = ftran(col, c, self._col_places[i])
            row = ftran(row, self._eta_rows[i], self._row_places[i])
        self._row_places.append(n_row)
        self._col_places.append(n_col)
        self._eta_rows.append(to_eta(row, n_col))
        self._eta_cols.append(to_eta(col, n_row))
        #do something to remove column and row

    def replace_equation(self, n_row, n_col, row, col):
        self._steps += 1
        for i, r in enumerate(self._eta_rows):
            col = btran(col, r, self._row_places[i])
            row = btran(row, self._eta_cols[i], self._col_places[i])
        col = np.dot(self._inv_matrix.get_matrix(), col)
        row = np.dot(self._inv_matrix.get_matrix().T, row)
        for i, c in enumerate(self._eta_cols):
            col = ftran(col, c, self._col_places[i])
            row = ftran(row, self._eta_rows[i], self._row_places[i])
        self._row_places.append(n_row)
        self._col_places.append(n_col)
        self._eta_rows.append(to_eta(row, n_col))
        self._eta_cols.append(to_eta(col, n_row))

def to_eta(values, index_to_pivot):
    pivot_val = values[index_to_pivot]
    values /= -values[index_to_pivot]
    values[index_to_pivot] = pivot_val
    return values

def ftran(values, eta, index_to_pivot):
    pivot_val = values[index_to_pivot] * eta[index_to_pivot]
    values[:len(eta)] += values[index_to_pivot] * eta
    values[index_to_pivot] = pivot_val
    return values

def btran(values, eta, index_to_pivot):
    pivot_val = np.inner(values[:len(eta)], eta)
    values[index_to_pivot] = pivot_val
    return values