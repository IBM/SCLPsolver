import pytest

import os, sys
import numpy as np

proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)

from SCLPsolver.SCLP import SCLP, SCLP_settings
from SCLPsolver.doe.data_generators.WorkloadPlacement import *

from SCLPsolver.doe.doe import gen_uncertain_param


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


@pytest.mark.parametrize("mu1, mu2", [(60.0, 25.0), (50.0, 22.0)])
def test_generate_one_server_two_classes(mu1, mu2):
    TT = 10
    tau1, tau2 = 1.0/mu1, 1.0/mu2

    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(40.0, 20.0, 1.0, 1.0, 1.0, tau1, tau2, 100.0, 100.0, False)
    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau, maxT = solution.get_final_solution(True)

    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(40.0, 20.0, 1.0, 1.0, 1.0, tau1, tau2, 100.0, 100.0, True)
    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t1, x1, q1, u1, p1, pivots1, SCLP_obj1, err1, NN1, tau1, maxT1 = solution.get_final_solution(True)

    assert np.array_equal(t, t1)
    assert abs(SCLP_obj - SCLP_obj1) < 0.001

    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost,  a) * TT**2/2
    real_obj = tot_buf_cost - SCLP_obj
    print(f'real_obj={real_obj} SCLP_obj={SCLP_obj} t={t} u={u} u1={u1}')


@pytest.mark.parametrize("epsilon, mu1, mu2", [(0.1, 60.0, 25.0)])
def test_generate_one_server_two_classes_perturbed(epsilon, mu1, mu2, seed=1):

    np.random.seed(seed)

    TT = 10
    tau1, tau2 = 1.0/mu1, 1.0/mu2

    tau = np.array((tau1, tau2))
    mu = np.array((mu1, mu2))

    tau1_bar, tau2_bar = tau_bar = tau * (1 + 0.5*epsilon)
    mu1_bar, mu2_bar = mu_bar = mu / (1 - 0.5*epsilon)

    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(40.0, 20.0, 1.0, 1.0, 1.0, tau1_bar, tau2_bar, 100.0, 100.0, True)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)

    u1 = np.multiply(u[0:2,:].transpose(), tau_bar).transpose()

    eta = np.multiply(u[0:2,:].transpose(), tau * (1-0.5*epsilon)).transpose()
    print(f'from tau_bar: t={t} tau={tau} tau_bar={tau_bar} u={u} u1={u1} eta={eta}')

    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(40.0, 20.0, 1.0, 1.0, 1.0, 1/mu1_bar, 1/mu2_bar, 100.0, 100.0, True)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)

    print(f'from mu_bar: t={t} mu={mu} mu_bar={mu_bar} u={u}')
