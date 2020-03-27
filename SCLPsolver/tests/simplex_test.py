import sys
sys.path.append('C:\DataD\Work\CERBERO\CLP\SCLPsolver')
from subroutines.lp_tools.simplex_procedures import simplex_procedures
import os
import numpy as np


def relative_to_project(file_path):
    if os.path.isabs(file_path):
        return file_path
    else:
        proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
        return os.path.join(proj, file_path)

A = np.load(relative_to_project('tests/data/DD.dat'))
pn = np.hstack(np.load(relative_to_project('tests/data/pn.dat')))
dn = np.hstack(np.load(relative_to_project('tests/data/dn.dat')))
ps = np.hstack(np.load(relative_to_project('tests/data/ps.dat')))
ds = np.hstack(np.load(relative_to_project('tests/data/ds.dat')))
import time
start_time = time.time()
A, pn, dn, ps, ds, err = simplex_procedures(A, pn, dn, ps, ds, 0)
print("--- %s seconds ---" % (time.time() - start_time))
print(A)
print(np.setdiff1d(pn, np.hstack(np.load(relative_to_project('tests/data/pn1.dat'))), assume_unique=True))
print(np.setdiff1d(dn, np.hstack(np.load(relative_to_project('tests/data/dn1.dat'))), assume_unique=True))
print(np.setdiff1d(np.hstack(np.load(relative_to_project('tests/data/pn1.dat'))),pn, assume_unique=True))
print(np.setdiff1d(np.hstack(np.load(relative_to_project('tests/data/dn1.dat'))),dn, assume_unique=True))
print(np.load(relative_to_project('tests/data/DD1.dat')))