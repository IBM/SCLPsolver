from scipy.linalg import lu_factor
import numpy as np
import time

a = np.zeros((2000, 2000), dtype=np.double, order='C')
total_time1 = 0
total_time2 = 0
for i in range(1000):
    b = np.random.rand(1000, 1000)
    a[:1000, :1000] = b
    start_time = time.time()
    res1 = lu_factor(b)
    c  = np.zeros((1000, 1000), dtype=np.double, order='C')
    total_time1 += time.time() - start_time
    d = a[:1000, :1000]
    start_time = time.time()
    res2 = lu_factor(d)
    total_time2 += time.time() - start_time

print(total_time1, total_time2, (total_time1-total_time2))