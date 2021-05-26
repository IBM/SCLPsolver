import pytest

import os, sys
import numpy as np

proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)

from SCLPsolver.SCLP import SCLP, SCLP_settings
from SCLPsolver.doe.data_generators.WorkloadPlacement import generate_workload_placement_data

seeds = [1234]


@pytest.mark.parametrize("seed", seeds)
def test_generate_workload_placement_data(seed):

    T = 10 # 10 seconds
    I = 2 # servers
    J = 3 # classes
    K = I * J
    R = np.array([100,200])
    P = np.array([1000,2000])
    a = np.ones((I,J))
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
    assert np.array_equal(alpha, x0)

    assert b is not None

    assert TT is not None
    assert TT == T

    assert total_buffer_cost is not None

    assert cost is not None

