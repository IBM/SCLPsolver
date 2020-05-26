# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


print('\n*** test add_rows')

print('Instance partition: ', test_partition_vector1,'Input partition: ', test_partition_vector2)
print('\nInstance data: \n', test_data_matrix1, '\nInput data: \n', test_data_matrix2)

piecewise_data_test1.add_rows(piecewise_data_test2)
print('\nResult: ')
print('Partition:', piecewise_data_test1.partition)
print('Data:', piecewise_data_test1.data)

# test add_columns
print('\n*** test add_columns')
test_data_matrix1 = np.random.randint(9, size=(matrix_size, matrix_size)) #np.asarray([[1,2,3,4],[5,6,7,8]])
test_partition_vector1 = np.random.randint(1, 9, size=matrix_size) #np.asarray([0,1,5,7]) #
test_partition_vector1[0] = 0
piecewise_data_test1 = piecewise_data(test_data_matrix1, test_partition_vector1)

print('Instance partition: ', test_partition_vector1,'Input partition: ', test_partition_vector2)
print('\nInstance data: \n', test_data_matrix1, '\nInput data: \n', test_data_matrix2)

piecewise_data_test1.add_columns(test_data_matrix2,test_partition_vector2)
print('\nResult: ')
print('Partition:', piecewise_data_test1.partition)
print('Data:', piecewise_data_test1.data)

# test next_data
print('\n*** test next_data')
matrix_size = 2
test_data_matrix1 = np.random.randint(9, size=(matrix_size, matrix_size)) #np.asarray([[1,2,3,4],[5,6,7,8]])
test_partition_vector1 = np.random.randint(1, 9, size=matrix_size) #np.asarray([0,1,5,7]) #
test_partition_vector1[0] = 0
piecewise_data_test1 = piecewise_data(test_data_matrix1, test_partition_vector1)

test_data_matrix2 = np.random.randint(9, size=(matrix_size, matrix_size)) #np.asarray([[1,2,3],[5,6,7]])#
test_partition_vector2 = np.random.randint(1, 9, size=matrix_size) #np.asarray([0,2,5])#
test_partition_vector2[0] = 0
piecewise_data_test2 = piecewise_data(test_data_matrix2, test_partition_vector2)

piecewise_data_LP_test = piecewise_LP_data(piecewise_data_test1, piecewise_data_test2)
print(piecewise_data_LP_test.next_data())
