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


matrix_a_size = 400
times_to_run = 100
# comparing numpy inverse speed to new algorithm speed
# 1st testing the numpy implementation
matrix_a = 10*np.random.rand(matrix_a_size, matrix_a_size)
vector_b = 10*np.random.rand(matrix_a_size)
vector_c = 10*np.random.rand(matrix_a_size)
scalar_d = 4

matrix_to_inverse = np.zeros((matrix_a_size + 1, matrix_a_size + 1))
matrix_to_inverse[0:matrix_a_size, 0:matrix_a_size] = matrix_a
matrix_to_inverse[0:matrix_a_size, matrix_a_size] = vector_b
matrix_to_inverse[matrix_a_size, 0:matrix_a_size] = vector_c
matrix_to_inverse[matrix_a_size, matrix_a_size] = scalar_d

tmp_matrix = np.zeros_like(matrix_a)

new_algorithm2_time = 0
new_algorithm3_time = 0
numpy_inverse_time =0
for i in range(times_to_run):
    matrix_a = 10 * np.random.rand(matrix_a_size, matrix_a_size)
    vector_b = 10 * np.random.rand(matrix_a_size)
    vector_c = 10 * np.random.rand(matrix_a_size)
    scalar_d = 4

    matrix_to_inverse = np.zeros((matrix_a_size + 1, matrix_a_size + 1))
    matrix_to_inverse[0:matrix_a_size, 0:matrix_a_size] = matrix_a
    matrix_to_inverse[0:matrix_a_size, matrix_a_size] = vector_b
    matrix_to_inverse[matrix_a_size, 0:matrix_a_size] = vector_c
    matrix_to_inverse[matrix_a_size, matrix_a_size] = scalar_d
    start_time = time.time()
    numpy_inverse_update_matrix = np.linalg.inv(matrix_to_inverse)
    numpy_inverse_time += time.time() - start_time
    inversed_matrix_a = np.linalg.inv(matrix_a)
    c = matrix(None, len(inversed_matrix_a) * 2)
    c.set_matrix(inversed_matrix_a)

    start_time = time.time()
    improved_algorithm_inverse_update_matrix = c.inverseUpdate3(vector_b, vector_c, scalar_d, tmp_matrix)
    new_algorithm3_time += time.time() - start_time

    start_time = time.time()
    improved_algorithm_inverse_update_matrix = c.inverseUpdate2(inversed_matrix_a, vector_b, vector_c, scalar_d)
    new_algorithm2_time += time.time() - start_time

print("Numpy iverse took ",numpy_inverse_time," seconds")

print("New algorithm 2 took ",new_algorithm2_time," seconds")
size_comparison = numpy_inverse_time/new_algorithm2_time
print("** New algorithm is ",abs(round((size_comparison-1)*100,1)), "%" ,'faster' if (size_comparison >= 1) else 'slower')

print("New algorithm 3 took ",new_algorithm3_time," seconds")
size_comparison = numpy_inverse_time/new_algorithm3_time
print("** New algorithm is ",abs(round((size_comparison-1)*100,1)), "%" ,'faster' if (size_comparison >= 1) else 'slower')

print("Are Numpy and new Algorithm results the same? :",  np.allclose(numpy_inverse_update_matrix,improved_algorithm_inverse_update_matrix))


