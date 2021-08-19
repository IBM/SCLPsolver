import pytest

import os, sys
import numpy as np

proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)

from SCLPsolver.SCLP import SCLP, SCLP_settings
from SCLPsolver.doe.data_generators.WorkloadPlacement import *

from SCLPsolver.doe.doe import *


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


def integrate(f, low, up, intervals=100):
    tt = np.linspace(low, up, intervals+1)
    y = [f(t) for t in tt]
    F = (0.5*(y[0]+y[-1]) + np.sum(y[1:-1]))*(up-low)/intervals
    return F
integrate_m = np.vectorize(integrate)


def test_integrate():
    assert abs(integrate(lambda x: 1, 0, 4) - 4) < 0.001
    assert abs(integrate(lambda x: x, 2, 6) - 16) < 0.001
    assert abs(integrate(lambda x: np.sin(x), 0, np.pi/2.0) - 1) < 0.001


def test_integrate_m():
    H1 = np.array((lambda x: 1,))
    assert abs(integrate_m(H1, 0, 4) - 4) < 0.001
    H2 = np.array(((lambda x: 1, lambda x: x),(lambda x: np.pi*np.sin(np.pi*x), lambda x: np.pi*np.sin(2*np.pi*x))))
    assert np.allclose(integrate_m(H2, 0, 1, intervals=1000), np.array(((1.0, 0.5), (2.0, 0.0))))

@pytest.mark.parametrize("epsilon, mu1, mu2, seed", [(0.2, 60.0, 25.0, 12)])
def test_generate_one_server_two_classes_perturbed(epsilon, mu1, mu2, seed):

    np.random.seed(seed)

    TT = 10
    tau1, tau2 = 1.0/mu1, 1.0/mu2

    tau = np.array((tau1, tau2))
    mu = np.array((mu1, mu2))

    a1, a2 = 40.0, 20.0           # arrival rates tasks per unit time
    b1 = 1.0                      # cpu limit
    c1, c2 = 1.0, 1.0             # cost per unit time of buffers
    alpha1, alpha2 = 100.0, 100.0 # initial buffer quantities

    # 1. Model 1, eta is control var
    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(a1,
                                                                                                         a2,
                                                                                                         b1,
                                                                                                         c1,
                                                                                                         c2,
                                                                                                         tau1,
                                                                                                         tau2,
                                                                                                         alpha1,
                                                                                                         alpha2,
                                                                                                         False)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
    real_obj1 = tot_buf_cost - SCLP_obj

    eta = u[0:2,:]
    u = np.multiply(eta.transpose(), mu).transpose()
    u_m1 = u.copy()
    t_m1 = t.copy()

    print(f'Step 1 (Model 1): t={t} tau={tau} mu={mu} u={u} eta={eta}')

    # 2. Model 2, u is control var
    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(a1,
                                                                                                         a2,
                                                                                                         b1,
                                                                                                         c1,
                                                                                                         c2,
                                                                                                         tau1,
                                                                                                         tau2,
                                                                                                         alpha1,
                                                                                                         alpha2,
                                                                                                         True)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
    real_obj2 = tot_buf_cost - SCLP_obj

    u = u[0:2,:]
    eta = np.multiply(u.transpose(), tau).transpose()

    print(f'Step 2 (Model 2): t={t} tau={tau} mu={mu} u={u} eta={eta}')

    # 3. make sure objectives of 1,2 are the same
    print(f'Step 3: objectives obj1={real_obj1}  obj2={real_obj2}')

    assert abs(real_obj1 - real_obj2) < 0.001

    # 4. Define tau_j(t)
    tau_t = gen_uncertain_param(tau, (0, TT), (-epsilon / 2.0, epsilon / 2.0), uncertain_func=sin_uncertainty_low)

    t_print = tuple(range(0, TT+1, 2))

    print(f'Step 4: uncertain tau({t_print})={np.array([(tau_t[0](t), tau_t[1](t)) for t in t_print]).transpose()}')

    # 5. Robust model with Box uncertainty Model 2 with tau_bar
    tau1_bar, tau2_bar = tau_bar = tau * (1 + 0.5*epsilon)

    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(a1,
                                                                                                         a2,
                                                                                                         b1,
                                                                                                         c1,
                                                                                                         c2,
                                                                                                         tau1_bar,
                                                                                                         tau2_bar,
                                                                                                         alpha1,
                                                                                                         alpha2,
                                                                                                         True)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
    real_obj5 = tot_buf_cost - SCLP_obj

    u = u[0:2,:]
    eta = np.multiply(u.transpose(), tau).transpose()

    print(f'Step 5 (Model 2 with tau_bar): t={t} tau_bar={tau_bar} mu={mu} u={u} eta={eta}')
    print(f'     Objectives: model 2: {real_obj2} model 5: {real_obj5}')
    assert real_obj5 >= real_obj2

    t_index = lambda x: min([i-1 for i, ti in enumerate(t) if ti > x] + [len(t)-2])
    eta_t = np.array([
        lambda x: u[0, t_index(x)] * tau[0] * (1 - 0.5 * epsilon),
        lambda x: u[1, t_index(x)] * tau[1] * (1 - 0.5 * epsilon)
    ])

    print(f'eta={eta}')
    print(f'eta_t({[t for t in range(0,TT+1,2)]}) = {np.array([(eta_t[0](t), eta_t[1](t)) for t in t_print]).transpose()}')

    u_t = np.array([
        lambda x: eta_t[0](x) / tau_t[0](x),
        lambda x: eta_t[1](x) / tau_t[1](x)
    ])
    print(f'u_t({[t for t in range(0,TT+1,2)]}) = {np.array([(u_t[0](t), u_t[1](t)) for t in t_print]).transpose()}')

    x_R_t = np.array([
        lambda x: alpha1 + a1 * x - integrate(u_t[0], 0, x),
        lambda x: alpha2 + a2 * x - integrate(u_t[1], 0, x)
    ])
    print(f'x_R_t({[t for t in range(0,TT+1,2)]}) = {np.array([(x_R_t[0](t), x_R_t[1](t)) for t in t_print]).transpose()}')

    obj_5 = np.sum([
        integrate(x_R_t[0], 0, TT),
        integrate(x_R_t[1], 0, TT)
    ])
    print(f'Step 5: real_obj2={real_obj2} real_obj5={real_obj5} obj_5={obj_5}')

    # 6. Robust model with Box uncertainty Model 1 with mu_bar
    mu1_bar, mu2_bar = mu_bar = mu / (1 - 0.5*epsilon)
    tau1_bar_bar, tau2_bar_bar = 1 / mu1_bar, 1 / mu2_bar

    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_new(a1,
                                                                                                         a2,
                                                                                                         b1,
                                                                                                         c1,
                                                                                                         c2,
                                                                                                         tau1_bar_bar,
                                                                                                         tau2_bar_bar,
                                                                                                         alpha1,
                                                                                                         alpha2,
                                                                                                         False)

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
    real_obj6 = tot_buf_cost - SCLP_obj

    eta = u[0:2, :]
    u = np.multiply(eta.transpose(), mu).transpose()

    print(f'Step 6 (Model 1 with mu_bar): t={t} mu_bar={mu_bar} mu={mu} u={u} eta={eta}')
    print(f'     Objectives: model 1: {real_obj1} model 6: {real_obj6}')
    assert real_obj6 <= real_obj1

    t_index = lambda x: min([i-1 for i, ti in enumerate(t) if ti > x] + [len(t)-2])
    eta_t = np.array([
        lambda x: u[0, t_index(x)] * tau[0] * (1 - 0.5 * epsilon),
        lambda x: u[1, t_index(x)] * tau[1] * (1 - 0.5 * epsilon)
    ])

    print(f'eta={eta}')
    print(f'eta_t({[t for t in range(0,TT+1,2)]}) = {np.array([(eta_t[0](t), eta_t[1](t)) for t in t_print]).transpose()}')

    u_t = np.array([
        lambda x: eta_t[0](x) / tau_t[0](x),
        lambda x: eta_t[1](x) / tau_t[1](x)
    ])
    print(f'u_t({[t for t in range(0,TT+1,2)]}) = {np.array([(u_t[0](t), u_t[1](t)) for t in t_print]).transpose()}')

    x_R_t = np.array([
        lambda x: alpha1 + a1 * x - integrate(u_t[0], 0, x),
        lambda x: alpha2 + a2 * x - integrate(u_t[1], 0, x)
    ])
    print(f'x_R_t({[t for t in range(0,TT+1,2)]}) = {np.array([(x_R_t[0](t), x_R_t[1](t)) for t in t_print]).transpose()}')

    obj_6 = np.sum([
        integrate(x_R_t[0], 0, TT),
        integrate(x_R_t[1], 0, TT)
    ])
    print(f'Step 6: real_obj1={real_obj1} real_obj6={real_obj6} obj_6={obj_6}')

    # 7. Model 1 again

    t = t_m1.copy()
    u = u_m1.copy()
    t_index = lambda x: min([i-1 for i, ti in enumerate(t) if ti > x] + [len(t)-2])

    print('Step 7: u={u}')

    # 8. Compute optimistic model

    u_t = np.array([
        lambda x: u[0, t_index(x)] * tau[0] / tau_t[0](x),
        lambda x: u[1, t_index(x)] * tau[1] / tau_t[1](x)
    ])

    print(f'u_t({[t for t in range(0,TT+1,2)]}) = {np.array([(u_t[0](t), u_t[1](t)) for t in t_print]).transpose()}')

    x_R_t = np.array([
        lambda x: max(alpha1 + a1 * x - integrate(u_t[0], 0, x), 0),
        lambda x: max(alpha2 + a2 * x - integrate(u_t[1], 0, x), 0)
    ])
    print(f'x_R_t({[t for t in range(0,TT+1,2)]}) = {np.array([(x_R_t[0](t), x_R_t[1](t)) for t in t_print]).transpose()}')

    obj_8 = np.sum([
        integrate(x_R_t[0], 0, TT),
        integrate(x_R_t[1], 0, TT)
    ])

    print(f'Step 8: real_obj1={real_obj1} real_obj6={real_obj6} obj_5={obj_5} obj_6={obj_6} obj_8={obj_8}')


