import numpy as np


def ismember(a,b):
    return np.isin(a, b, assume_unique=True)

def find(a):
    return np.where(a)[0]