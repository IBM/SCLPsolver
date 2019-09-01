import numpy as np
from subroutines.SCLP_formulation import SCLP_formulation
from subroutines.parametric_line import parametric_line
from subroutines.LP_formulation import solve_LP_in_place
from doe.data_generators.MCQN import generate_MCQN_data
tolerance = 0
num_trials = 100
K = 1000
I = 100
for seed in range(1000, 1000 + num_trials):
    G, H, F, gamma, c, d, alpha, a, b, TT, buffer_cost = generate_MCQN_data(seed, K, I)
    formulation = SCLP_formulation(G, F, H, a, b, c, d, alpha, gamma, TT)
    param_line = parametric_line.get_SCLP_parametric_line(formulation, tolerance)
    # start time
    LP_form = formulation.formulate_ratesLP(param_line.x_0, param_line.q_N)
    err = solve_LP_in_place(LP_form, np.zeros_like(LP_form.simplex_dict), tolerance)
    # end time
    if err['result'] != 0:
        raise Exception(err['message'])
    # alternative way implement as function
    # start time
    # build matrix [[G 0 I]
    #               [H I 0]]
    # take columns where param_line.q_N == 0 + all columns from last I columns to matrix B
    # take columns where param_line.q_N > 0 to matrix N
    # find inverse of B and calculate X = np.dot(inv(B), N)
    # calculate np.dot(inv(B), np.concatenate(a, b))
    # end time
    # check consistency np.allclose(LP_form.simplex_dict[1:,1:], X) exception if problem
