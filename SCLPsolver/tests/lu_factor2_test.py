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

from scipy.linalg import lu_factor
import numpy as np
import time

total_time1 = 0
total_time2 = 0
for i in range(1000):
    b = np.random.rand(1000, 1000)
    start_time = time.time()
    res1 = lu_factor(b)
    total_time1 += time.time() - start_time
    c = np.zeros((900, 900), dtype=np.double, order='C')
    c[:,:] = b[:900,:900]
    start_time = time.time()
    res2 = lu_factor(c)
    total_time2 += time.time() - start_time

print(total_time1, total_time2, (total_time1-total_time2))