from subroutines.experimental.generic_equation_solver import generic_equation_solver
import numpy as np
import random
import time


matrix_size = 1000
times_to_run = 4

print('\n test reverse_vector_order')

vector = [1,2,3]
order = [0, -1, 2, -1 ,1]

equation_solver_test = generic_equation_solver(matrix_size * 2)
print('result : ', equation_solver_test.reverse_vector_order(vector, order))


# # test that do replace, add and remove several times

def test_replace(input_matrix, equation_solver_parameter):
    print(' testing replace equation')
    input_matrix_size = len(input_matrix)
    vector_2 = 10 * np.random.normal(size=input_matrix_size)

    index_to_replace = random.randint(0, input_matrix_size - 1)

    #step 5
    random_row_vector_5_1 = 10 * np.random.normal(size=input_matrix_size)
    random_column_vector_5_2 = 10 * np.random.normal(size=input_matrix_size)

    # step 6
    input_matrix[:, index_to_replace] = random_column_vector_5_2
    input_matrix[index_to_replace, :] = random_row_vector_5_1

    # step 7
    start_time = time.time()
    matrix_7 = np.linalg.inv(input_matrix)
    # step 8
    result_8 = np.dot(matrix_7, vector_2)

    # step 10
    equation_solver_parameter.replace_equation(index_to_replace, index_to_replace, random_row_vector_5_1, random_column_vector_5_2)
    result_11 = equation_solver_parameter.resolve(vector_2)

    print("Iteration:", i, " Are Numpy and new Algorithm results the same? :", np.allclose(result_8, result_11))
    print("Abs error:", max(abs(result_8 - result_11)))
    print("Rel error:", max(abs(result_8 - result_11) / abs(result_8)))

    return input_matrix

def test_add(input_matrix, equation_solver_parameter):
    print(' testing add equation')
    input_matrix_size = len(input_matrix)
    vector_2 = 10 * np.random.normal(size=input_matrix_size + 1)

    index_to_replace = random.randint(0, input_matrix_size - 1)

    random_row_vector_5_1 = 10 * np.random.normal(size=input_matrix_size + 1)
    random_column_vector_5_2 = 10 * np.random.normal(size=input_matrix_size + 1)

    # expand matrix by 1 row and 1 column
    matrix_2 = np.eye(input_matrix.shape[0] + 1)

    matrix_2[:index_to_replace, :index_to_replace] = input_matrix[:index_to_replace, :index_to_replace]
    matrix_2[:index_to_replace, index_to_replace + 1:] = input_matrix[:index_to_replace, index_to_replace:]
    matrix_2[index_to_replace + 1:, :index_to_replace] = input_matrix[index_to_replace:, :index_to_replace]
    matrix_2[index_to_replace + 1:, index_to_replace + 1:] = input_matrix[index_to_replace:, index_to_replace:]

    matrix_2[:, index_to_replace] = random_column_vector_5_2
    matrix_2[index_to_replace, :] = random_row_vector_5_1

    # step 7
    start_time = time.time()
    matrix_7 = np.linalg.inv(matrix_2)
    # step 8
    result_8 = np.dot(matrix_7, vector_2)
    print("--- %s inv seconds ---" % (time.time() - start_time))

    start_time = time.time()
    result_8  = np.linalg.solve(matrix_2, vector_2)
    # step 8
    print("--- %s solve seconds ---" % (time.time() - start_time))

    start_time = time.time()
    equation_solver_parameter.add_equation(index_to_replace, index_to_replace, random_row_vector_5_1, random_column_vector_5_2)

    result_11 = equation_solver_parameter.resolve(vector_2)
    print("--- %s update seconds ---" % (time.time() - start_time))

    print("Are Numpy and new Algorithm results the same? :", np.allclose(result_8, result_11))
    print("Abs error:", max(abs(result_8 - result_11)))
    print("Rel error:", max(abs(result_8 - result_11)/abs(result_8)))

    # print("results using numpy:\n",result_8)
    # print("results using add equation:\n",result_11)
    return matrix_2

def test_remove(input_matrix, equation_solver_parameter):
    print(' testing remove equation')

    input_matrix_size = len(input_matrix)

    vector_2 = 10 * np.random.normal(size=input_matrix_size - 1)

    index_to_replace = random.randint(0, input_matrix_size - 1)

    # removing row and column
    matrix_2 = np.zeros([len(input_matrix) - 1, len(input_matrix) - 1])
    matrix_2[:index_to_replace, :index_to_replace] = input_matrix[:index_to_replace, :index_to_replace]
    matrix_2[:index_to_replace, index_to_replace:] = input_matrix[:index_to_replace, index_to_replace + 1:]
    matrix_2[index_to_replace:, :index_to_replace] = input_matrix[index_to_replace + 1:, :index_to_replace]
    matrix_2[index_to_replace:, index_to_replace:] = input_matrix[index_to_replace + 1:, index_to_replace + 1:]

    # inverse matrix
    matrix_7 = np.linalg.inv(matrix_2)

    # dot on rhs
    result_8 = np.dot(matrix_7, vector_2)

    equation_solver_parameter.remove_equation(index_to_replace, index_to_replace)
    equation_solver_result = equation_solver_parameter.resolve(vector_2)
    print("Are Numpy and new Algorithm results the same? :", np.allclose(result_8, equation_solver_result))
    print("Abs error:", max(abs(result_8 - equation_solver_result)))
    print("Rel error:", max(abs(result_8 - equation_solver_result)/abs(result_8)))
    #
    # print('result_8              :',result_8)
    # print('equation_solver_result:',equation_solver_result)
    return matrix_2


#0 create test matrix

test_matrix = 10 * np.random.rand(matrix_size, matrix_size)
#1 inverse matrix

inverse_of_test_matrix = np.linalg.inv(test_matrix)
#2 input the inverse matrix to solver
equation_solver_test = generic_equation_solver(len(inverse_of_test_matrix) * 2)
equation_solver_test.set_inverse_matrix(inverse_of_test_matrix)

for i in range(times_to_run):
    # 3 in each iteration, take 2 arguments - original matrix before inverse, and equation equation_solver
    # 4 output of method is matrix that was changed using numpy operations
    # 5 next method takes the matrix from previous output and pass original equation solver instance to it

    test_matrix = test_replace(test_matrix, equation_solver_test)
    test_matrix = test_add(test_matrix, equation_solver_test)
    test_matrix = test_remove(test_matrix, equation_solver_test)