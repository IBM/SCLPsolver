# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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