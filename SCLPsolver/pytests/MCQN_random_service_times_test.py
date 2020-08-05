import pytest
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

from doe.doe import gen_uncertain_param
from doe.data_generators.MCQN import generate_MCQN_data
from SCLP import SCLP, SCLP_settings

with_plots = False

@pytest.mark.parametrize("perturbation", [0.0, 0.01, 0.05, 0.1])
def test_random_service_times(perturbation):
    """Test that the gen_uncertain_param function works on MCQN
        and can be used to generate service TIME realizations with uncertainty"""

    seed = 1000

    T = 10.0
    I = 10
    K = 15
    J = K

    settings = {'alpha_rate': 1, 'cost_scale': 2, 'a_rate': 0.05, 'sum_rate': 0.95, 'nz': 0.5,
                'gamma_rate': 0, 'c_scale': 0, 'h_rate': 0.2}

    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)

    assert (H >= 0).all()
    assert (H <= settings['h_rate']).all()

    domain = (0, T)
    H_prime = gen_uncertain_param(H, domain, (0, perturbation), seed=1)

    H_0 = np.zeros(shape=H.shape)
    H_T = np.zeros(shape=H.shape)
    H_T2 = np.zeros(shape=H.shape)

    for index, h in np.ndenumerate(H_prime):
        if H[index] == 0: continue
        H_0[index] = h(0)
        H_T[index] = h(T)
        H_T2[index] = h(T/2.0)
        res_min = minimize_scalar(h, method="bounded", bounds=(0,T))
        h_min = res_min.fun
        g = lambda t: -h(t)
        res_max = minimize_scalar(g, method="bounded", bounds=(0,T))
        h_max = -res_max.fun
        assert h_min - H[index] >= -1e-10
        assert h_max - H[index] * (1+perturbation) <= 1e-10

    # check that when H == 0 then output function is 0
    assert np.array_equal(H == 0, H_0 == 0)
    assert np.array_equal(H == 0, H_T == 0)
    assert np.array_equal(H == 0, H_T2 == 0)

    # check that output is less than perturbation given
    assert (H_0 <= (1 + perturbation) * H).all()
    assert (H_T <= (1 + perturbation) * H).all()
    assert (H_T2 <= (1 + perturbation) * H).all()

    # check that output is greater than nominal
    assert (H_0 >= H).all()
    assert (H_T >= H).all()
    assert (H_T2 >= H).all()

    if with_plots:
        plt.hist(H.flatten())
        plt.show()

@pytest.mark.parametrize("perturbation", [0.0, 0.01, 0.05, 0.1])
def test_random_service_rates(perturbation):
    """Test that the gen_uncertain_param function works on MCQN
        and can be used to generate service RATE realizations with uncertainty"""

    seed = 1000

    T = 10.0    # max time
    I = 10      # number of servers
    K = 15      # number of job classes
    J = K       # number of flows from buffer to buffer

    settings = {'alpha_rate': 1, 'cost_scale': 2, 'a_rate': 0.05, 'sum_rate': 0.95, 'nz': 0.5,
                'gamma_rate': 0, 'c_scale': 0, 'h_rate': 0.2}

    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)

    # H is I x J

    assert (H >= 0).all()
    assert (H <= settings['h_rate']).all()


    X = np.where(H==0, 0, 1/H)

    domain = (0, T)
    X_prime = gen_uncertain_param(X, domain, (0, perturbation), seed=1)

    H_0 = np.zeros(shape=H.shape)
    H_T = np.zeros(shape=H.shape)
    H_T2 = np.zeros(shape=H.shape)

    for index, x in np.ndenumerate(X_prime):
        if X[index] == 0: continue
        h = lambda t: 1.0/x(t) if x(t) > 0. else 0.
        H_0[index] = h(0)
        # print(f'pert={perturbation} i={index} H={H[index]} X={X[index]} H0={H_0[index]}')
        H_T[index] = h(T)
        H_T2[index] = h(T/2.0)
        res_min = minimize_scalar(h, method="bounded", bounds=(0,T))
        h_min = res_min.fun
        g = lambda t: -h(t)
        res_max = minimize_scalar(g, method="bounded", bounds=(0,T))
        h_max = -res_max.fun

    # check that when H == 0 then output function is 0
    assert np.array_equal(H == 0, H_0 == 0)
    assert np.array_equal(H == 0, H_T == 0)
    assert np.array_equal(H == 0, H_T2 == 0)

    if with_plots:
        plt.hist((H_T2 - H).flatten())
        plt.show()

@pytest.mark.parametrize("perturbation", [0.0])
def test_random_service_times_feasible(perturbation):
    """Test that the gen_uncertain_param function works on MCQN
        and the service TIME realizations are feasible"""

    starting_seed = 1000

    T = 10.0
    I = 20
    K = 30
    J = K

    settings = {'alpha_rate': 1, 'cost_scale': 2, 'a_rate': 0.05, 'sum_rate': 0.95, 'nz': 0.5,
                'gamma_rate': 0, 'c_scale': 0, 'h_rate': 0.2}

    G0, H0, F0, gamma0, c0, d0, alpha0, a0, b0, TT0, buffer_cost0, xcost0 = generate_MCQN_data(starting_seed, K, I,
                                                                                               **settings)

    # Create the nominal solution
    solver_settings = SCLP_settings()
    solution0, STEPCOUNT0, param_line0, res0 = SCLP(G0, H0, F0, a0, b0, c0, d0, alpha0, gamma0, T, solver_settings)
    t0, x0, q0, u0, p0, pivots0, obj0, err0, NN0, tau0, maxT0 = solution0.get_final_solution()

    # get the control variables
    u = u0[0:J,]
    N = u.shape[1]

    # verify constraint for unperturbed H0
    for i in range(I):
        H0_i = H0[i,:]
        for n in range(N):
            u_n = u[:,n]
            f = H0_i.dot(u_n)
            assert f - 1.0 <= 1e-10

    # Random realization of H (service times)
    domain = (0, T)
    H = gen_uncertain_param(H0, domain, (0, perturbation), seed=1)

    # check if perturbed H passes constraint
    f_max = np.zeros(shape=(I, N))
    x_max = np.zeros(shape=(I, N))
    for i in range(I):
        H_i = H[i,:]
        for n in range(N):
            u_n = u[:,n]
            assert len(H_i) == len(u_n)
            f = lambda t: np.dot([h_i(t) for h_i in H_i], u_n)
            g = lambda t: -f(t)
            t_min, t_max = t0[n], t0[n+1]
            res = minimize_scalar(g, method='bounded', bounds=(t_min, t_max))
            assert res.x > t_min
            assert res.x < t_max
            f_max[i, n] = -res.fun
            # print(f'i={i} n={n} t={res.x} f={f_max[i,n]} t_min={t_min} t_max={t_max}')
    assert np.all(f_max >= -1e-10)
    assert np.all(f_max - 1 <= 1e-10)

@pytest.mark.parametrize("perturbation", [0.0, 1e-5])
def test_random_service_rates_feasible(perturbation):
    """Test that the gen_uncertain_param function works on MCQN
        and the service RATE realizations are feasible"""

    starting_seed = 1000

    T = 10.0
    I = 20
    K = 30
    J = K

    settings = {'alpha_rate': 1, 'cost_scale': 2, 'a_rate': 0.05, 'sum_rate': 0.95, 'nz': 0.5,
                'gamma_rate': 0, 'c_scale': 0, 'h_rate': 0.2}

    G0, H0, F0, gamma0, c0, d0, alpha0, a0, b0, TT0, buffer_cost0, xcost0 = generate_MCQN_data(starting_seed, K, I,
                                                                                               **settings)

    # rate is the inverse of time H
    X0 = np.where(H0==0, 0, 1/H0)

    # Create the nominal solution
    solver_settings = SCLP_settings()
    solution0, STEPCOUNT0, param_line0, res0 = SCLP(G0, H0, F0, a0, b0, c0, d0, alpha0, gamma0, T, solver_settings)
    t0, x0, q0, u0, p0, pivots0, obj0, err0, NN0, tau0, maxT0 = solution0.get_final_solution()

    # get the control variables
    u = u0[0:J,]
    N = u.shape[1]

    # Random realization of X (service rates)
    domain = (0, T)
    X = gen_uncertain_param(X0, domain, (0, perturbation), seed=1)

    # check if perturbed H passes constraint
    f_max = np.zeros(shape=(I, N))
    x_max = np.zeros(shape=(I, N))
    for i in range(I):
        X_i = X[i,:]
        for n in range(N):
            u_n = u[:,n]
            assert len(X_i) == len(u_n)
            # need to invert 1/x(t) = h(t)
            f = lambda t: np.dot([1/x_i(t) if x_i(t) != 0. else 0. for x_i in X_i], u_n)
            g = lambda t: -f(t)
            t_min, t_max = t0[n], t0[n+1]
            res = minimize_scalar(g, method='bounded', bounds=(t_min, t_max))
            assert res.x > t_min
            assert res.x < t_max
            f_max[i, n] = -res.fun
            # print(f'i={i} n={n} t={res.x} f={f_max[i,n]}')
    assert np.all(f_max >= -1e-10)
    assert np.all(f_max - 1 <= 1e-10)