from subroutines.matrix import matrix
from subroutines.equation_solver import equation_solver
import numpy as np
import random
import time


matrix_size = 400
times_to_run = 100

print('\n test reverse_vector_order')

vector = [1,2,3]
order = [0, -1, 2, -1 ,1]

equation_solver_test = equation_solver(matrix_size*2)
print('result : ', equation_solver_test.reverse_vector_order(vector, order))


# # test that do replace, add and remove several times

def test_replace(inputMatrix):
    print(' testing replace equation')
    numpy_algorithm_time = 0
    new_algorithm_time = 0
    vector_2 = 10 * np.random.normal(size=matrix_size)

    matrix_3 = np.linalg.inv(inputMatrix)

    # step 9
    equation_solver_9 = equation_solver(matrix_size)
    equation_solver_9.set_inverse_matrix(matrix_3)

    index_to_replace = random.randint(0, matrix_size - 1)

    random_row_vector_5_1 = 10 * np.random.normal(size=matrix_size)
    random_column_vector_5_2 = 10 * np.random.normal(size=matrix_size)
    # step 6
    inputMatrix[:, index_to_replace] = random_column_vector_5_2
    inputMatrix[index_to_replace, :] = random_row_vector_5_1

    # step 7
    start_time = time.time()
    matrix_7 = np.linalg.inv(inputMatrix)
    # step 8
    matrix_2 = np.dot(matrix_7, vector_2)
    numpy_algorithm_time += time.time() - start_time

    start_time = time.time()
    # step 10
    equation_solver_9._replace_equation(index_to_replace, index_to_replace, random_row_vector_5_1,
                                        random_column_vector_5_2)
    result_11 = equation_solver_9.resolve(vector_2)
    new_algorithm_time += time.time() - start_time

    print("Iteration:", i, " Are Numpy and new Algorithm results the same? :", np.allclose(matrix_2, result_11))

    # print("Numpy algorithm took ", numpy_algorithm_time, " seconds")
    # print("New algorithm took ", new_algorithm_time, " seconds")
    size_comparison = numpy_algorithm_time / new_algorithm_time
    print("** New algorithm is ", abs(round((size_comparison - 1) * 100, 1)), "%",
          'faster' if (size_comparison >= 1) else 'slower')

    return equation_solver_9.get_inverse();

def test_add(inputMatrix):
    print(' testing add equation')
    numpy_algorithm_time = 0
    new_algorithm_time = 0
    vector_2 = 10 * np.random.normal(size=matrix_size + 1)

    matrix_3 = np.linalg.inv(inputMatrix)

    index_to_replace = 0  # random.randint(0, matrix_size - 1)

    random_row_vector_5_1 = 10 * np.random.normal(size=matrix_size + 1)
    random_column_vector_5_2 = 10 * np.random.normal(size=matrix_size + 1)

    # expand matrix by 1 row and 1 column
    matrix_2 = np.eye(inputMatrix.shape[0] + 1)

    matrix_2[:index_to_replace, :index_to_replace] = inputMatrix[:index_to_replace, :index_to_replace]
    matrix_2[:index_to_replace, index_to_replace + 1:] = inputMatrix[:index_to_replace, index_to_replace:]
    matrix_2[index_to_replace + 1:, :index_to_replace] = inputMatrix[index_to_replace:, :index_to_replace]
    matrix_2[index_to_replace + 1:, index_to_replace + 1:] = inputMatrix[index_to_replace:, index_to_replace:]
    res22 = np.linalg.inv(matrix_2)
    matrix_2[:, index_to_replace] = random_column_vector_5_2
    matrix_2[index_to_replace, :] = random_row_vector_5_1

    # step 7
    start_time = time.time()
    matrix_7 = np.linalg.inv(matrix_2)
    # step 8
    matrix_2 = np.dot(matrix_7, vector_2)
    numpy_algorithm_time += time.time() - start_time

    # step 9
    equation_solver_9 = equation_solver(matrix_size * 2)
    equation_solver_9.set_inverse_matrix(matrix_3)

    start_time = time.time()

    equation_solver_9.add_equation(index_to_replace, index_to_replace, random_row_vector_5_1, random_column_vector_5_2)

    result_11 = equation_solver_9.resolve(vector_2)

    new_algorithm_time += time.time() - start_time

    print("Are Numpy and new Algorithm results the same? :", np.allclose(matrix_2, result_11))

    # print("Numpy algorithm took ", numpy_algorithm_time, " seconds")
    # print("New algorithm took ", new_algorithm_time, " seconds")
    size_comparison = numpy_algorithm_time / new_algorithm_time
    print("** New algorithm is ", abs(round((size_comparison - 1) * 100, 1)), "%",
          'faster' if (size_comparison >= 1) else 'slower')
    #
    # print("results using numpy:\n",result_8)
    # print("results using add equation:\n",result_11)
    return equation_solver_9.get_inverse();

def test_remove(inputMatrix):
    print(' testing remove equation')
    vector_2 = 10 * np.random.normal(size=len(inputMatrix) - 1)

    matrix_3 = np.linalg.inv(inputMatrix)

    index_to_replace = random.randint(0, len(inputMatrix) - 1)

    # removing row and column
    matrix_2 = np.zeros([len(inputMatrix) - 1, len(inputMatrix) - 1])
    matrix_2[:index_to_replace, :index_to_replace] = inputMatrix[:index_to_replace, :index_to_replace]
    matrix_2[:index_to_replace, index_to_replace:] = inputMatrix[:index_to_replace, index_to_replace + 1:]
    matrix_2[index_to_replace:, :index_to_replace] = inputMatrix[index_to_replace + 1:, :index_to_replace]
    matrix_2[index_to_replace:, index_to_replace:] = inputMatrix[index_to_replace + 1:, index_to_replace + 1:]

    # inverse matrix
    matrix_7 = np.linalg.inv(matrix_2)

    # dot on rhs
    result_8 = np.dot(matrix_7, vector_2)

    equation_solver_test = equation_solver(len(inputMatrix))
    equation_solver_test.set_inverse_matrix(matrix_3)
    equation_solver_test.remove_equation(index_to_replace, index_to_replace)
    equation_solver_result = equation_solver_test.resolve(vector_2)
    print("Are Numpy and new Algorithm results the same? :", np.allclose(result_8, equation_solver_result))
    #
    # print('result_8              :',result_8)
    # print('equation_solver_result:',equation_solver_result)
    return equation_solver_test.get_inverse();

test_matrix = 10 * np.random.rand(matrix_size, matrix_size)

for i in range(times_to_run):

    matrix_result = test_replace(test_matrix)
    matrix_result = test_add(matrix_result)
    matrix_result = test_remove(matrix_result)