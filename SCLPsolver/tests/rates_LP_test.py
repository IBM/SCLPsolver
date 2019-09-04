import numpy as np
import time
from subroutines.SCLP_formulation import SCLP_formulation
from subroutines.parametric_line import parametric_line
from subroutines.LP_formulation import solve_LP_in_place
from doe.data_generators.MCQN import generate_MCQN_data

def alternativeImplementation():
    # start time
    start_time = time.time()
    # build matrix [[G 0 I]
    #               [H I 0]]

    number_of_rows_in_G = len(G)
    number_of_columns_in_G = len(G)
    matrix_column_size = number_of_columns_in_G*2+len(H)
    matrix_row_size = number_of_columns_in_G+len(H)
    new_matrix = np.zeros((matrix_row_size,matrix_column_size))

    new_matrix[:number_of_rows_in_G, :number_of_columns_in_G]=G
    new_matrix[number_of_rows_in_G:number_of_rows_in_G+len(H), :number_of_columns_in_G]=H
    new_matrix[:, number_of_columns_in_G:] = 0
    I = np.eye(len(H))
    new_matrix[number_of_rows_in_G:, number_of_columns_in_G:number_of_columns_in_G+len(H)] = I
    I = np.eye(len(G))
    new_matrix[:number_of_rows_in_G, number_of_columns_in_G+len(H):] = I

    matrix_B = []
    matrix_N = []

    # param_line.q_N is a vector
    # take columns where param_line.q_N == 0 + all columns from last I columns to matrix B
    # take columns where param_line.q_N > 0 to matrix N
    zero_indices = np.argwhere(param_line.q_N == 0)
    zero_indices = zero_indices.reshape(len(zero_indices))
    matrix_B = new_matrix[:,zero_indices]
    matrix_N = new_matrix[:,np.nonzero(param_line.q_N)[0]]

    matrix_B = np.column_stack((matrix_B, new_matrix[:,number_of_columns_in_G+len(H):]))

    # find inverse of B and calculate X = np.dot(inv(B), N)
    inverse_of_matrix_B = np.linalg.inv(matrix_B)
    matrix_X =  np.dot(inverse_of_matrix_B, matrix_N)
    # calculate np.dot(inv(B), np.concatenate(a, b))
    result = np.dot(inverse_of_matrix_B, np.concatenate((a, b), axis=None))
    # end time
    end_time = time.time()
    print('time taken for alternative implementation:',end_time - start_time)

    # check consistency np.allclose(LP_form.simplex_dict[1:,1:], X) exception if problem
    if not np.allclose(LP_form.simplex_dict[1:, 1:], matrix_X):
        raise Exception(err['result is not the same'])


tolerance = 0
num_trials = 100
K = 1000
i = 100
for seed in range(1000, 1000 + num_trials):
    G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_data(seed, K, i)
    formulation = SCLP_formulation(G, F, H, a, b, c, d, alpha, gamma, TT)
    param_line = parametric_line.get_SCLP_parametric_line(formulation, tolerance)
    # start time
    start_time = time.time()

    LP_form = formulation.formulate_ratesLP(param_line.x_0, param_line.q_N)
    err = solve_LP_in_place(LP_form, np.zeros_like(LP_form.simplex_dict), tolerance)
    # end time
    end_time = time.time()
    print('time taken for new implementation:', end_time - start_time)

    if err['result'] != 0:
        raise Exception(err['message'])
    # alternative way implement as function
    alternativeImplementation()

