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

import numpy as np


class boundary_value():
    __slots__ = ['v', 'delta_v']

    def __init__(self, v, delta_v=None):
        self.v = v
        self.delta_v = delta_v

    def get_delta(self):
        if self.delta_v is not None:
            rz = np.divide(-self.delta_v, self.v, where=self.v > 0, out=np.zeros_like(self.v))
            zz_ind = np.argmax(rz)
            zz = rz[zz_ind]
        else:
            zz = 0
            zz_ind = None
        return 1.0/zz, zz_ind