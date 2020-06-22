import pytest
from doe.doe import gen_uncertain_param
import numpy as np
import matplotlib.pyplot as plt

def test_gen_uncertain_param():
    domain = (left, right) = (0, 100)
    codomain = (low, high) = (1, 3.5)
    shape = (5, 5)
    params = np.zeros(shape, dtype=np.float32)
    p = gen_uncertain_param(params, domain, codomain)
    assert p.shape == shape
    # for i, f in np.ndenumerate(p):
    #     for t in range(*domain):
    #         if f(t) < low or f(t) > high:
    #             print(f'i={i} t={t} f(t)={f(t)}')
    assert all([low <= f(t) <= high for i, f in np.ndenumerate(p) for t in range(*domain)])

    xs = np.linspace(left, right, 50)
    y1 = [p[(0,0)](x) for x in xs]
    y2 = [p[(1,0)](x) for x in xs]
    y3 = [p[(2,1)](x) for x in xs]
    y4 = [p[(3,4)](x) for x in xs]

    plt.plot(xs, y1)
    plt.plot(xs, y2)
    plt.plot(xs, y3)
    plt.plot(xs, y4)
    plt.show()
