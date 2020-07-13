import pytest
import numpy as np
import matplotlib.pyplot as plt

from doe.doe import gen_uncertain_param
from doe.data_generators.MCQN import generate_MCQN_data

with_plots = False

def test_random_service_times_0_1():

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
    H_prime = gen_uncertain_param(H, domain, codomain)

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

