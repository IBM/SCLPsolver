from subroutines.matrix_constructor8 import matrix_constructor
import numpy as np

a = np.asarray([3,5,7])
b = np.asarray([0,1,3])
c = matrix_constructor(a, b, 4)
print(c.get_matrix())
d = np.asarray([[1,2],[3,4],[5,6],[7,8]])
c.replace_matrix(0,0,d)
print(c.get_matrix())
c.replace_matrix(1,1,d)
print(c.get_matrix())
c.replace_matrix(0,5,d+5)
print(c.get_matrix())
c.replace(3,3,a,b)
print(c.get_matrix())
c.remove(1,2)
print(c.get_matrix())
