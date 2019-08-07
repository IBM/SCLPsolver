from subroutines.matrix import matrix
import numpy as np

a = 8
b = 6
c = matrix(a,b)
print(c.get_matrix())

index = 0
row_vector = np.asarray([1, 1])
column_vector = np.asarray([1, 1])
c.insert(index,row_vector,column_vector)
print(c.get_matrix())

index = 1
row_vector = np.asarray([2,2,2])
column_vector = np.asarray([2,2,2])
c.insert(index,row_vector,column_vector)
print(c.get_matrix())

index = 2
row_vector = np.asarray([3,3,3,3])
column_vector = np.asarray([3,3,3,3])
c.insert(index,row_vector,column_vector)
print(c.get_matrix())

index = 3
c.delete(index)
print(c.get_matrix())

index = 1
row_vector = np.asarray([4,4,4])
column_vector = np.asarray([4,4,4])
c.overwrite(index,row_vector,column_vector)
print(c.get_matrix())
