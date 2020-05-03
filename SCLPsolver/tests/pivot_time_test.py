import sys
sys.path.append('C:\DataD\Work\CERBERO\CLP\SCLPsolver')
import os
import numpy as np
from subroutines.lp_tools.cy_lp_tools import copy_pivot


def relative_to_project(file_path):
    if os.path.isabs(file_path):
        return file_path
    else:
        proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
        return os.path.join(proj, file_path)
import time
A = np.load(relative_to_project('tests/data/DD.dat'), allow_pickle=True)
A = np.ascontiguousarray(A)
pn = np.load(relative_to_project('tests/data/pn.dat'), allow_pickle=True).astype(int)[:,0]
dn = np.load(relative_to_project('tests/data/dn.dat'), allow_pickle=True).astype(int)[:,0]
B=np.zeros_like(A)
pn1 = pn.copy()
dn1 = dn.copy()
start_time = time.time()
for i in range(2,22):
    if i in [2,4,6,8,10,12,14,16,18,20]:
        a,b= copy_pivot(A, pn, dn, i, i, B)
    else:
        a, b = copy_pivot(B, pn, dn, i, i, A)
print("--- %s seconds ---" % (time.time() - start_time))
# X = A.copy()

# A = np.load(relative_to_project('tests/data/DD.dat'), allow_pickle=True)
# B=np.zeros_like(A)
# #pn = np.load(relative_to_project('tests/data/pn.dat'), allow_pickle=True)[:,0]
# #dn = np.load(relative_to_project('tests/data/dn.dat'), allow_pickle=True)[:,0]
# start_time = time.time()
# for i in range(2,12):
#     if i in [2,4,6,8,10]:
#         a,b= copy_pivot3(A, pn, dn, i, i, B)
#     else:
#         a, b = copy_pivot3(B, pn, dn, i, i, A)
# print("--- %s seconds ---" % (time.time() - start_time))
# # print(np.any((A-X) >10E-10))
# print(np.any((A-X) < -10E-10))
# print(np.any((pn-pn1) >10E-10),np.any((dn-dn1) >10E-10), np.any((pn-pn1) <-10E-10),np.any((dn-dn1) <-10E-10))