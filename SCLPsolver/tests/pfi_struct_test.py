import timeit
from subroutines.pivot_storage import *
from subroutines.experimental.pfi_struct import *

t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')

prim_names = np.asarray([1, 2, 3, 4])
exiting_names = np.asarray([-1, -2,-3,-4])
pivots = pivot_storage(prim_names,exiting_names)
pfi_instance = pfi_struct(np.asarray([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [1, 2, 3, 4]]), prim_names, np.asarray([5,6,7,8]), 2, np.asarray([[1, 2, 3, 4],[5, 6, 7, 8]]), np.asarray([[1, 2, 3, 4],[5, 6, 7, 8]]),pivots)
print(pfi_instance.get_dict_row_at(1, 2))
print(pfi_instance.get_dict_col_at(1, 6))
print(pfi_instance.get_prim_vars_at(1))
print(pfi_instance.get_dual_vars_at(1))

print('time taken in milliseconds =', t.timeit()/1000)