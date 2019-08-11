import numpy as np
import math


class matrix():

    # assuming data is a scalar
    # assuming matrix is the size n*n
    def __init__(self, data, allocation_size):
        self._allocation_size = allocation_size

        self._matrix = np.zeros(shape=(allocation_size, allocation_size))

        self._top = 0
        self._left = 0

        if data is not None:
            self._bottom = self._top+1
            self._right = self._left+1
            self._matrix[self._top,self._left] = data
        else:
            self._bottom = self._top
            self._right = self._left

    #'#@profile
    def get_matrix(self):
        return self._matrix[self._left:self._right,self._top:self._bottom]

    def insert(self, index, row_vector, column_vector):
        matrix_size = self._bottom - self._top

        if index > self._allocation_size or index < 0:
            print('Index out of bounds, index value is ',index,' while matrix size is ',matrix_size)

        # move top right corner
        self._matrix[self._top:self._top+index,self._left+index+1:self._right+1] = self._matrix[self._top:self._top+index,self._left+index:self._right]
        # move bottom right corner
        self._matrix[self._top+index+1:self._bottom+1,self._left+index+1:self._right+1] = self._matrix[self._top+index:self._bottom,self._left+index:self._right]
        # move bottom left corner
        self._matrix[self._top + index+1:self._bottom+1,self._left:self._left+index] = self._matrix[self._top + index:self._bottom,self._left:self._left+index]

        self._bottom += 1
        self._right += 1

        # insert row vector
        self._matrix[self._top+index,self._left:self._right] = row_vector
        # insert the column vector
        self._matrix[self._top:self._bottom,self._left+index] = column_vector

    def delete(self, index):
        # move top right corner
        self._matrix[self._top:self._top + index, self._left + index :self._right - 1] = self._matrix[
                                                                                            self._top:self._top + index,
                                                                                            self._left + index + 1:self._right]
        # move bottom right corner
        self._matrix[self._top + index:self._bottom - 1 , self._left + index :self._right - 1] = self._matrix[
                                                                                                       self._top + index+1:self._bottom,
                                                                                                       self._left + index+1:self._right]
        # move bottom left corner
        self._matrix[self._top + index:self._bottom - 1, self._left:self._left + index] = self._matrix[
                                                                                              self._top + index + 1:self._bottom,
                                                                                              self._left:self._left + index]

        self._bottom -= 1
        self._right -= 1


    def overwrite(self, index, row_vector, column_vector):
        matrix_size = self._bottom - self._top

        if index > self._allocation_size or index < 0:
            print('Index out of bounds, index value is ', index, ' while matrix size is ', matrix_size)

        # insert row vector
        self._matrix[self._top + index, self._left:self._right] = row_vector
        # insert the column vector
        self._matrix[self._top:self._bottom, self._left + index] = column_vector


    def inverseUpdate2(self, inverse_of_matrix_a, vector_b, vector_c, scalar_d):

        v = np.dot(vector_c,inverse_of_matrix_a)
        z = 1/(scalar_d - np.inner(v, vector_b))
        y = -z * v
        x = np.dot(-inverse_of_matrix_a , vector_b * z)
        w = inverse_of_matrix_a - np.outer(vector_b, y)

        self._right = self._bottom = len(w) + 1

        self._matrix[:self._bottom - 1,:self._right -1] = w
        self._matrix[:len(x), self._right -1 ] = x
        self._matrix[self._bottom - 1, :len(y)] = y
        self._matrix[self._bottom - 1, self._right - 1] = z

        return self.get_matrix()
