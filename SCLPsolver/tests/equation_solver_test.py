from subroutines.matrix import matrix
from subroutines.equation_solver import equation_solver
import numpy as np
import random
import time


matrix_size = 3
times_to_run = 5


print('\n test reverse_vector_order')

vector = [1,2,3]
order = [0, -1, 2, -1 ,1]

equation_solver_test = equation_solver(matrix_size*2)
print('result : ', equation_solver_test.reverse_vector_order(vector, order))


print('\n test replace_equation')

numpy_algorithm_time = 0
new_algorithm_time = 0
vector_2 = 10 * np.random.normal(size=matrix_size)

for i in range(times_to_run):

    if i == 0:
        matrix_1 = 10 * np.random.rand(matrix_size, matrix_size)

        matrix_3 = np.linalg.inv(matrix_1)
        result_4 = np.dot(matrix_3, vector_2)

        # step 9
        equation_solver_9 = equation_solver(matrix_size)
        equation_solver_9.set_inverse_matrix(matrix_3)

    index_to_replace = random.randint(0, matrix_size - 1)

    random_row_vector_5_1 = 10 * np.random.normal(size=matrix_size)
    random_column_vector_5_2 = 10 * np.random.normal(size=matrix_size)
    # step 6
    matrix_1[:, index_to_replace] = random_column_vector_5_2
    matrix_1[index_to_replace, :] = random_row_vector_5_1

    # step 7
    start_time = time.time()
    matrix_7 = np.linalg.inv(matrix_1)
    # step 8
    matrix_2 = np.dot(matrix_7, vector_2)
    numpy_algorithm_time += time.time() - start_time

    start_time = time.time()
    #step 10
    equation_solver_9._replace_equation(index_to_replace,index_to_replace,random_row_vector_5_1,random_column_vector_5_2)
    result_11 = equation_solver_9.resolve(vector_2)
    new_algorithm_time += time.time() - start_time

    print("Are Numpy and new Algorithm results the same? :", np.allclose(matrix_2, result_11))


print("Numpy algorithm took ", numpy_algorithm_time, " seconds")
print("New algorithm took ", new_algorithm_time, " seconds")

print('\n test add_equation')

numpy_algorithm_time = 0
new_algorithm_time = 0
vector_2 = 10 * np.random.normal(size=matrix_size+1)

matrix_1 = 10 * np.random.rand(matrix_size, matrix_size)

matrix_3 = np.linalg.inv(matrix_1)

index_to_replace = 0#random.randint(0, matrix_size - 1)


random_row_vector_5_1 = 10 * np.random.normal(size=matrix_size+1)
random_column_vector_5_2 = 10 * np.random.normal(size=matrix_size+1)

# expand matrix by 1 row and 1 column
matrix_2 = np.eye(matrix_1.shape[0]+1)

matrix_2[:index_to_replace, :index_to_replace] = matrix_1[:index_to_replace, :index_to_replace]
matrix_2[:index_to_replace, index_to_replace+1:] = matrix_1[:index_to_replace, index_to_replace:]
matrix_2[index_to_replace+1:, :index_to_replace] = matrix_1[index_to_replace:,:index_to_replace]
matrix_2[index_to_replace+1:,index_to_replace+1:] = matrix_1[index_to_replace:,index_to_replace:]
res22 = np.linalg.inv(matrix_2)
matrix_2[:,index_to_replace] = random_column_vector_5_2
matrix_2[index_to_replace,:] = random_row_vector_5_1

# step 7
start_time = time.time()
matrix_7 = np.linalg.inv(matrix_2)
# step 8
matrix_2 = np.dot(matrix_7, vector_2)
numpy_algorithm_time += time.time() - start_time

# step 9
equation_solver_9 = equation_solver(matrix_size*2)
equation_solver_9.set_inverse_matrix(matrix_3)

start_time = time.time()

random_5_1_mod = random_row_vector_5_1.copy()
v = random_5_1_mod[index_to_replace]
random_5_1_mod[index_to_replace:-1] = random_5_1_mod[index_to_replace+1:]
random_5_1_mod[-1] = v
random_5_2_mod = random_column_vector_5_2.copy()
v = random_5_2_mod[index_to_replace]
random_5_2_mod[index_to_replace:-1] = random_5_2_mod[index_to_replace+1:]
random_5_2_mod[-1] = v

equation_solver_9.add_equation(index_to_replace,index_to_replace,random_5_1_mod.copy(),random_5_2_mod.copy())
vector_2_mod = vector_2.copy()
v = vector_2_mod[index_to_replace]
vector_2_mod[index_to_replace:-1] = vector_2_mod[index_to_replace+1:]
vector_2_mod[-1] = v
result_11 = equation_solver_9.resolve(vector_2_mod.copy())

new_algorithm_time += time.time() - start_time

print("Are Numpy and new Algorithm results the same? :", np.allclose(matrix_2, result_11))


print("Numpy algorithm took ", numpy_algorithm_time, " seconds")
print("New algorithm took ", new_algorithm_time, " seconds")
size_comparison = numpy_algorithm_time/new_algorithm_time
print("** New algorithm is ",abs(round((size_comparison-1)*100,1)), "%" ,'faster' if (size_comparison >= 1) else 'slower')
#
# print("results using numpy:\n",result_8)
# print("results using add equation:\n",result_11)

# test remove equation

print('\n test remove_equation')

matrix_1 = 10 * np.random.rand(matrix_size, matrix_size)
vector_2 = 10 * np.random.normal(size=matrix_size-1)

matrix_3 = np.linalg.inv(matrix_1)

index_to_replace = random.randint(0, matrix_size - 1)

# removing row and column
matrix_2 = np.zeros([matrix_size-1,matrix_size-1])
matrix_2[:index_to_replace, :index_to_replace] = matrix_1[:index_to_replace, :index_to_replace]
matrix_2[:index_to_replace, index_to_replace:] = matrix_1[:index_to_replace, index_to_replace+1:]
matrix_2[index_to_replace:, :index_to_replace] = matrix_1[index_to_replace+1:,:index_to_replace]
matrix_2[index_to_replace:,index_to_replace:] = matrix_1[index_to_replace+1:,index_to_replace+1:]

# inverse matrix
matrix_7 = np.linalg.inv(matrix_2)

# dot on rhs
result_8 = np.dot(matrix_7, vector_2)

equation_solver_test = equation_solver(matrix_size)
equation_solver_test.set_inverse_matrix(matrix_3)
equation_solver_test.remove_equation(index_to_replace,index_to_replace)
equation_solver_result = equation_solver_test.resolve(vector_2_mod.copy())
print("Are Numpy and new Algorithm results the same? :", np.allclose(result_8, equation_solver_result))

print('result_8              :',result_8)
print('equation_solver_result:',equation_solver_result)


# test that do replace, add and remove several times
