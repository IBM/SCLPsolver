import pytest
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

from doe.doe import gen_uncertain_param
from doe.data_generators.MCQN import generate_MCQN_data
from SCLP import SCLP, SCLP_settings

with_plots = False


def test_random_service_times_0_1():
    """Test that the gen_uncertain_param function works on MCQN
        and can be used to generate service time realizations with uncertainty"""

    seed = 1000
    perturbation = 0.1

    T = 10.0
    I = 100
    K = 1000

    settings = {'alpha_rate': 1, 'cost_scale': 2, 'a_rate': 0.05, 'sum_rate': 0.95, 'nz': 0.5,
                'gamma_rate': 0, 'c_scale': 0, 'h_rate': 0.2}

    G, H, F, gamma, c, d, alpha, a, b, TT, total_buffer_cost, buffer_cost = generate_MCQN_data(seed, K, I, **settings)

    assert (H >= 0).all()
    assert (H <= settings['h_rate']).all()

    domain = (0, T)
    codomain = ((1 - perturbation) * settings['h_rate'], (1 + perturbation) * settings['h_rate'])
    H_prime = gen_uncertain_param(H, domain, codomain, seed=1)

    H_0 = np.zeros(shape=H.shape)
    H_T = np.zeros(shape=H.shape)
    H_T2 = np.zeros(shape=H.shape)
    for index, h in np.ndenumerate(H_prime):
        H_0[index] = h(0)
        H_T[index] = h(T)
        H_T2[index] = h(T/2.0)

    assert np.array_equal(H == 0, H_0 == 0)
    assert np.array_equal(H == 0, H_T == 0)
    assert np.array_equal(H == 0, H_T2 == 0)

    assert (H_0 <= (1 + perturbation) * settings['h_rate']).all()
    assert (H_T <= (1 + perturbation) * settings['h_rate']).all()
    assert (H_T2 <= (1 + perturbation) * settings['h_rate']).all()

    assert np.array_equal(H > 0, H_0 >= (1 - perturbation) * settings['h_rate'])
    assert np.array_equal(H > 0, H_T >= (1 - perturbation) * settings['h_rate'])
    assert np.array_equal(H > 0, H_T2 >= (1 - perturbation) * settings['h_rate'])

    if with_plots:
        plt.hist(H.flatten())
        plt.show()

def test_random_service_times_feasible():
    """Test that the gen_uncertain_param function works on MCQN
        and the service time realizations are feasible"""

    starting_seed = 1000
    perturbation = 0.01

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

    # Random realization of H (service times)
    domain = (0, T)
    codomain = ((1 - perturbation) * settings['h_rate'], (1 + perturbation) * settings['h_rate'])
    H = gen_uncertain_param(H0, domain, codomain, seed=1)

    u = u0[0:J,]
    N = u.shape[1]

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
            f_max[i, n] = f(res.x)
            print(f'i={i} n={n} t={res.x} f={f_max[i,n]} t_min={t_min} t_max={t_max}')
    assert np.all(f_max >= 0)
    assert np.all(f_max <= 1)

