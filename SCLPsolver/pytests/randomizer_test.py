import pytest
import numpy as np
import matplotlib.pyplot as plt

from doe.doe import gen_uncertain_param

with_plots = False

def test_gen_uncertain_param():
    """Test that the gen_uncertain_param function works"""
    domain = (left, right) = (0, 100)
    perturbation = (low, high) = (0, 0.1)
    shape = (5, 5)
    params = np.eye(shape[0], dtype=np.float32)
    p = gen_uncertain_param(params, domain, perturbation, seed=1)
    assert p.shape == shape
    # for i, f in np.ndenumerate(p):
    #     for t in range(*domain):
    #         if f(t) < low or f(t) > high:
    #             print(f'i={i} t={t} f(t)={f(t)}')
    # assert all([low <= f(t) <= high for i, f in np.ndenumerate(p) for t in range(*domain)])

    if with_plots:
        xs = np.linspace(left, right, 50)
        y1 = [p[(0,0)](x) for x in xs]
        y2 = [p[(1,1)](x) for x in xs]
        y3 = [p[(2,2)](x) for x in xs]
        y4 = [p[(3,3)](x) for x in xs]

        plt.axhline(y=1, xmin=0.1, xmax=0.9)
        if low != 0:
            plt.axhline(y=(1 + low), xmin=0.1, xmax=0.9, linestyle='dotted')
        if high != 0:
            plt.axhline(y=(1 + high), xmin=0.1, xmax=0.9, linestyle='dotted')
        plt.plot(xs, y1)
        plt.plot(xs, y2)
        plt.plot(xs, y3)
        plt.plot(xs, y4)
        plt.show()

def test_gen_uncertain_param_seed():
    """Test that seed parameter of gen_uncertain_param() works"""
    domain = (left, right) = (0, 100)
    codomain = (low, high) = (1, 3.5)
    shape = (5, 5)
    params = np.ones(shape, dtype=np.float32)
    p0 = gen_uncertain_param(params, domain, codomain, seed=1)
    p1 = gen_uncertain_param(params, domain, codomain, seed=1)
    p2 = gen_uncertain_param(params, domain, codomain)

    assert np.array_equal(p0[(1,1)](0), p1[(1,1)](0)) == True
    assert np.array_equal(p0[(1,1)](0), p2[(1,1)](0)) == False

