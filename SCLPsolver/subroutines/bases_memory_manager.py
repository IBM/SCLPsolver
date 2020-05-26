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


class bases_memory_manager():

    def __init__(self, pl, dl, max_bases = 3):
        self.max_bases = max_bases
        self._bases = []
        self.ps = np.zeros(pl, dtype=np.int32, order='C')
        self.ds = np.zeros(dl, dtype=np.int32, order='C')

    def add(self, bases):
        for i in range(min(len(bases), self.max_bases - len(self._bases))):
            self._bases.append(bases[i])

    def pop(self):
        if len(self._bases) > 0:
            return self._bases.pop(0)
        else:
            return None