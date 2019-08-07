from subroutines.matrix import matrix
import numpy as np

a = 8
b = 6
c = matrix(a,b)
print(c.get_matrix())

index = 0
row_vector = np.asarray([1, 2])
column_vector = np.asarray([3, 4])
c.insert(index,row_vector,column_vector)
print(c.get_matrix())

index = 1
row_vector = np.asarray([1,2,3])
column_vector = np.asarray([4,5,6])
c.insert(index,row_vector,column_vector)
print(c.get_matrix())

index = 1
c.delete(1)
print(c.get_matrix())