import pytest
import numpy as np
import matplotlib.pyplot as plt

from doe.doe import gen_uncertain_param

with_plots = False

def test_gen_uncertain_param():
    """Test that the gen_uncertain_param function works"""
    np.random.seed(123)
    domain = (left, right) = (0, 100)
    perturbation = (low, high) = (0, 0.1)
    shape = (5, 5)
    params = np.eye(shape[0], dtype=np.float32)
    p = gen_uncertain_param(params, domain, perturbation, seed=1)
    assert p.shape == shape

    assert all([low * params[i] <= f(t) - params[i] <= high * params[i] for i, f in np.ndenumerate(p)
                for t in range(*domain)])

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


@pytest.mark.parametrize("low, high, budget", [(0, 0.1, 0.1), (0, 0.1, 0.03)])
def test_gen_uncertain_param_budget(low, high, budget):
    """Test that the gen_uncertain_param function works with budget parameter"""
    np.random.seed(123)
    domain = (left, right) = (0, 100)
    perturbation = (low, high)
    I = 10 # number of servers
    K = 10 # number of job classes
    J = K # number of flows

    shape = (I, J)
    params = np.random.random(I * J).reshape(shape)

    p = gen_uncertain_param(params, domain, perturbation, budget=[budget]*I, seed=1)

    if with_plots:
        xs = np.linspace(left, right, 50)
        y1 = [p[(0,0)](x) for x in xs]
        y2 = [p[(1,1)](x) for x in xs]
        y3 = [p[(2,2)](x) for x in xs]
        y4 = [p[(3,3)](x) for x in xs]

        plt.axhline(y=params[0, 0], xmin=0.1, xmax=0.9)
        plt.axhline(y=params[1, 1], xmin=0.1, xmax=0.9)
        plt.axhline(y=params[2, 2], xmin=0.1, xmax=0.9)
        plt.axhline(y=params[3, 3], xmin=0.1, xmax=0.9)
        if low != 0:
            plt.axhline(y=params[0, 0]*(1 + low), xmin=0.1, xmax=0.9, linestyle='dotted')
            plt.axhline(y=params[1, 1] * (1 + low), xmin=0.1, xmax=0.9, linestyle='dotted')
            plt.axhline(y=params[2, 2] * (1 + low), xmin=0.1, xmax=0.9, linestyle='dotted')
            plt.axhline(y=params[3, 3] * (1 + low), xmin=0.1, xmax=0.9, linestyle='dotted')
        if high != 0:
            plt.axhline(y=params[0, 0]*(1 + high), xmin=0.1, xmax=0.9, linestyle='dotted')
            plt.axhline(y=params[1, 1] * (1 + high), xmin=0.1, xmax=0.9, linestyle='dotted')
            plt.axhline(y=params[2, 2] * (1 + high), xmin=0.1, xmax=0.9, linestyle='dotted')
            plt.axhline(y=params[3, 3] * (1 + high), xmin=0.1, xmax=0.9, linestyle='dotted')
        plt.plot(xs, y1)
        plt.plot(xs, y2)
        plt.plot(xs, y3)
        plt.plot(xs, y4)
        plt.show()

    assert p.shape == shape

    param_rows = params.sum(axis=1)
    assert(param_rows.shape[0] == I)

    for t in range(*domain):
        for i, f in np.ndenumerate(p):
            # print(f'i={i} t={t} f(t)={f(t)} high={high} params={params[i]} param_rows={param_rows[i[0]]}')
            assert low * params[i] <= f(t) - params[i]
            assert f(t) - params[i] <= high * params[i]

    assert all([low * params[i] <= f(t) - params[i] for i, f in np.ndenumerate(p) for t in range(*domain)])
    assert all([f(t) - params[i] <= high * params[i] for i, f in np.ndenumerate(p) for t in range(*domain)])

    for t in range(*domain):
        for i in range(I):
            f_row_t = sum(f(t) for f in p[i,:])
            # print(f'i={i} t={t} f_row(t)={f_row_t} budget={budget} param_rows={param_rows[i]}')
            assert f_row_t - param_rows[i] <= budget * param_rows[i] + 1e-9

