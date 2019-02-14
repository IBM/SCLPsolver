import numpy as np


def array_by_row(*args):
    return np.array((args))

print(array_by_row([1,2],[3,4],[5,6]))