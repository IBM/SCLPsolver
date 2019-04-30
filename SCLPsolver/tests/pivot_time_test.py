import sys
sys.path.append('C:\DataD\Work\CERBERO\CLP\SCLPsolver')
import os
import numpy as np


def relative_to_project(file_path):
    if os.path.isabs(file_path):
        return file_path
    else:
        proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
        return os.path.join(proj, file_path)
import time
A = np.load(relative_to_project('tests/data/DD.dat'))
start_time = time.time()
for i in range(2,12):
    p = A[i, i]
    if p == 0:
        raise Exception('pivot on zero')
    rp = A[i, :] / p
    c = A[:, i].copy()
    A -= np.outer(c, rp)
    # A = dger(-1.0, c, rp, a=A, overwrite_a= 1)
    A[i, :] = rp
    A[:, i] = c / -p
    A[i, i] = 1. / p
print("--- %s seconds ---" % (time.time() - start_time))
X = A.copy()
A = np.load(relative_to_project('tests/data/DD.dat'))
start_time = time.time()
B=np.zeros_like(A)
start_time = time.time()
for i in range(2,12):
    p = A[i, i]
    if p == 0:
        raise Exception('pivot on zero')
    rp = A[i, :] / p
    c = A[:, i].copy()
    A -= np.outer(c, rp, out=B)
    # A = dger(-1.0, c, rp, a=A, overwrite_a= 1)
    A[i, :] = rp
    A[:, i] = c / -p
    A[i, i] = 1. / p
print("--- %s seconds ---" % (time.time() - start_time))
print(np.any((A-X) >10E-10))
print(np.any((A-X) < -10E-10))