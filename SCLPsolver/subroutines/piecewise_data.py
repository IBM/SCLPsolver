# input
# data - a matrix
# partition - list of scalars
import numpy as np


class piecewise_data():

    __slots__ = ['data', 'partition', '_current_index', '_nextT']

    def __init__(self, data, partition):
        # np 2dim array data
        self.data = data
        # list partition
        self.partition = partition
        self._current_index = 0
        self._nextT = 0

    # should add picewise data combining partitions and data
    def add_rows(self, picewise_data):
        number_of_cols_for_new_matrix = len(np.setdiff1d(picewise_data.partition,self.partition))
        number_of_rows_for_new_matrix = len (picewise_data.data) + len(self.data)
        new_matrix = np.zeros((number_of_rows_for_new_matrix,number_of_cols_for_new_matrix))
        new_partition = np.zeros(len(number_of_cols_for_new_matrix))

        new_col_index = 0
        self_partition_index = 0
        input_partition_index = 0

        for new_col_index in range(number_of_cols_for_new_matrix):
            top_vector = self.data[:, self_partition_index]
            bottom_vector = picewise_data.data[:, input_partition_index]
            new_matrix[:len(top_vector), new_col_index] = top_vector
            new_matrix[len(top_vector):, new_col_index] = bottom_vector

            new_partition[new_col_index] = max(self.partition[self_partition_index], picewise_data.partition[input_partition_index])

            if self.partition[self_partition_index] == picewise_data.partition[input_partition_index]:
                self_partition_index += 1

            if self.partition[self_partition_index] > picewise_data.partition[input_partition_index]:
                input_partition_index += 1

            if self.partition[self_partition_index] < picewise_data.partition[input_partition_index]:
                self_partition_index += 1
                input_partition_index += 1
‎


                # should append columns to data and partition to partition
    def add_columns(self, data, partition):
        self.data = np.concatante(self.data,data)
        self.partition = np.concatenate(self.partition,partition)

    @property
    def nextT(self):
        return self._nextT

    def next_data(self):
        self._current_index +=1
        #check if we at the end of list if yes set self._nextT=np.inf
        self._nextT = self.partition[self._current_index+1]
        return self.data[:,self._current_index]


class piecewise_LP_data():

    def __init__(self, rhs, objective):
        self.rhs = rhs
        self.objective = objective

    # should return minimum of self._nextT of objective and rhs
    def get_nextT(self):
        return min(self.rhs.nextT,self.objective.nextT)

    # should return next data from objective and/or rhs and indicator what data are returned
    def next_data(self):
        if self.rhs.nextT < self.rhs.nextT:
            return self.rhs.next_data, 'rhs'
        else:
            return self.objective.next_data, 'objective'
