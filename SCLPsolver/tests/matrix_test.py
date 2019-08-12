from subroutines.matrix import matrix
import numpy as np
import time

a = 8
b = 6
test_matrix = matrix(a, b)
print(test_matrix.get_matrix())

index = 0
row_vector = np.asarray([1, 1])
column_vector = np.asarray([1, 1])
test_matrix.insert(index, row_vector, column_vector)
print(test_matrix.get_matrix())

index = 1
row_vector = np.asarray([2,2,2])
column_vector = np.asarray([2,2,2])
test_matrix.insert(index, row_vector, column_vector)
print(test_matrix.get_matrix())

index = 2
row_vector = np.asarray([3,3,3,3])
column_vector = np.asarray([3,3,3,3])
test_matrix.insert(index, row_vector, column_vector)
print(test_matrix.get_matrix())

index = 3
test_matrix.delete(index)
print(test_matrix.get_matrix())

index = 1
row_vector = np.asarray([4,4,4])
column_vector = np.asarray([4,4,4])
test_matrix.overwrite(index, row_vector, column_vector)
print(test_matrix.get_matrix())


matrix_size = 200
# comparing numpy inverse speed to new algorithm speed
# 1st testing the numpy implementation
matrix_a = np.random.randint(10, size=(2, 2))
vector_b = np.asarray([2,2])
vector_c = np.asarray([2,2])
scalar_d = 4

matrix_to_inverse = np.zeros((3,3))
matrix_to_inverse[0:2,0:2] = matrix_a
matrix_to_inverse[0:2,2] = vector_b
matrix_to_inverse[2,0:2] = vector_c
matrix_to_inverse[2,2] = scalar_d

start_time = time.time()
numpy_inverse_update_matrix = np.linalg.inv(matrix_to_inverse)
numpy_inverse_time = time.time() - start_time
print("numpy took ",numpy_inverse_time," seconds")

inversed_matrix_a = np.linalg.inv(matrix_a)

c = matrix(None, len(inversed_matrix_a)*2)

start_time = time.time()
improved_algorithm_inverse_update_matrix = c.inverseUpdate2(inversed_matrix_a, vector_b, vector_c, scalar_d)
new_algorithm_time = time.time() - start_time
print("new algorithm took ",time.time() - start_time," seconds")
print("new algorithm is ",numpy_inverse_time-new_algorithm_time," faster")
print("Numpy result:\n",numpy_inverse_update_matrix)
print("New Algorithm result:\n",improved_algorithm_inverse_update_matrix)
print(np.array_equal(numpy_inverse_update_matrix,improved_algorithm_inverse_update_matrix))


