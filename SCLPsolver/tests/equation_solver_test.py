from subroutines.matrix import matrix
from subroutines.equation_solver import equation_solver
import numpy as np
import random
import time

matrix_size = 300
times_to_run = 5
# comparing numpy inverse speed to new algorithm speed
# 1st testing the numpy implementation
# matrix_1 = 10*np.random.rand(matrix_size, matrix_size)
# vector_2 = 10*np.random.normal(size=matrix_size)
# matrix_3 = np.linalg.inv(matrix_1)
# result_4 = np.dot(matrix_3,vector_2)
#
# index_to_replace = random.randint(0,matrix_size-1)
#
# random_row_vector_5_1 = 10 * np.random.normal(size=matrix_size)
# random_column_vector_5_2 =10 * np.random.normal(size=matrix_size)#matrix_1[:, index_to_replace]#
# #random_row_vector_5_1[index_to_replace] =  matrix_1[index_to_replace,index_to_replace]



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
    result_8 = np.dot(matrix_7, vector_2)
    numpy_algorithm_time += time.time() - start_time

    start_time = time.time()
    #step 10
    equation_solver_9._replace_equation(index_to_replace,index_to_replace,random_row_vector_5_1,random_column_vector_5_2)
    #result10 = equation_solver_9.get_inverse()
    #print(np.allclose(result10, matrix_7))
    result_11 = equation_solver_9.resolve(vector_2)
    new_algorithm_time += time.time() - start_time

    print("Are Numpy and new Algorithm results the same? :", np.allclose(result_8, result_11))


print("Numpy algorithm took ", numpy_algorithm_time, " seconds")
print("New algorithm took ", new_algorithm_time, " seconds")
size_comparison = numpy_algorithm_time/new_algorithm_time
print("** New algorithm is ",abs(round((size_comparison-1)*100,1)), "%" ,'faster' if (size_comparison >= 1) else 'slower')

#print(result_8)
#print(result_11)


vector_col_order = np.asarray([4,2,-1,9])
original_result_vector = np.asarray([1, 2, 3, 4])
argsort_indices = vector_col_order.argsort()
sorted_col_order = vector_col_order[argsort_indices]
sorted_result_vector = original_result_vector[argsort_indices]

index = np.searchsorted(sorted_col_order, -1, side='right')
clean_up_result = sorted_result_vector[index:]
print("sorting_result ", clean_up_result)











