# data - a matrix
# partition - list of scalars
import numpy as np
from subroutines.piecewise_data import piecewise_data, piecewise_LP_data

# test add_rows(self, picewise_data)
matrix_size = 2
test_data_matrix1 = np.random.randint(9, size=(matrix_size, matrix_size)) #np.asarray([[1,2,3,4],[5,6,7,8]])
test_partition_vector1 = np.random.randint(1, 9, size=matrix_size) #np.asarray([0,1,5,7]) #
test_partition_vector1[0] = 0

piecewise_data_test1 = piecewise_data(test_data_matrix1, test_partition_vector1)

test_data_matrix2 = np.random.randint(9, size=(matrix_size, matrix_size)) #np.asarray([[1,2,3],[5,6,7]])#
test_partition_vector2 = np.random.randint(1, 9, size=matrix_size) #np.asarray([0,2,5])#
test_partition_vector2[0] = 0

piecewise_data_test2 = piecewise_data(test_data_matrix2, test_partition_vector2)


print('\ntest add_rows')

print('Instance partition: ', test_partition_vector1,'Input partition: ', test_partition_vector2)
print('\nInstance data: \n', test_data_matrix1, '\nInput data: \n', test_data_matrix2)

piecewise_data_test1.add_rows(piecewise_data_test2)
print('\nResult: ')
print('Partition:', piecewise_data_test1.partition)
print('Data:', piecewise_data_test1.data)

# test add_columns

##piecewise_data_test1.add_columns(test_data_matrix2,test_partition_vector2)

# test next_data


piecewise_data_LP_test = piecewise_LP_data(piecewise_data_test1, piecewise_data_test2)
