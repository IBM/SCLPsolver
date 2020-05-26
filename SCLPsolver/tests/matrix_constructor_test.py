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

from subroutines.matrix_constructor import matrix_constructor
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
c.remove(2,3)
print(c.get_matrix())
