import pytest

import os, sys
import numpy as np

proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)

from SCLPsolver.SCLP import SCLP, SCLP_settings
from SCLPsolver.doe.data_generators.WorkloadPlacement import generate_workload_placement_data


def test_generate_workload_placement_data():
    """ Test generating data from Workload Placement model for SCLP
    """

    T = 10 # 10 seconds
    I = 2 # servers
    J = 3 # classes
    K = I * J
    R = np.array([100,200])
    P = np.array([1000,2000])
    a = np.ones(J)
    mu = np.array([4,5])
    x0 = np.zeros((I,J))
    r = np.ones(J)
    rprime = np.ones(J)

    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, cost = generate_workload_placement_data(T, I, J, R, P, a, mu, x0, r, rprime)

    assert G is not None
    assert np.array_equal(G, np.array([[-4, 0, 0, -5, 0, 0], [0, -4, 0, 0, -5, 0], [0, 0, -4 ,0, 0, -5]]))

    assert H is not None
    assert np.array_equal(H, np.array([[1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]]))

    assert F is not None
    assert np.array_equal(F, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    assert gamma is not None
    assert np.array_equal(gamma, np.zeros(K))

    assert c is not None
    assert c.shape == (K,)

    assert d is not None
    assert d.shape == (K-J,)

    assert alpha is not None

    assert b is not None

    assert TT is not None
    assert TT == T

    assert total_buffer_cost is not None

    assert cost is not None


seeds = [1234]


@pytest.mark.parametrize("seed", seeds)
def test_workload_placement_to_sclp(seed):
    """
    Generate random workload placement model and run SCLP
    Parameters
    ----------
    seed : int
        Seed for np.random

    """

    # Observe: 1) initial number of tasks in each of the K buffers
    #          2) task arrival events
    #     Ask: 3) what am I estimating?
    #          4) what are the statistical properties of the solution given the randomness in a and x0
    #          5) how do I interpret u?
    #          6) should we normalize u to 1's?
    #          7) what are the statistical properties of u given a and x0
    #          8) has anyone analyzed this for sclp?
    #          9) has anyone used this for other optimization algorithms?

    np.random.seed(seed)

    T = 10 # 10 seconds
    I = 2 # servers
    J = 3 # classes
    K = I * J
    R = np.array([100,200])
    P = np.array([1000,2000])
    a = np.random.normal(1, 0.1, J)
    mu = np.array([4,5])
    x0 = np.random.uniform(1, 3, (I,J))
    r = np.ones(J)
    rprime = np.ones(J)

    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, cost = generate_workload_placement_data(T, I, J, R, P, a, mu, x0, r, rprime)

    solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False, memory_management=False,
                                    suppress_printing=False)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT, solver_settings)

    assert solution is not None

    t, x, q, u, p, pivots, obj, err, NN, tau, maxT = solution.get_final_solution(True)

    assert t is not None