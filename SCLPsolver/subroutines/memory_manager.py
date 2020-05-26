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

import psutil
import math


class memory_manager():

    def __init__(self, K, J, I=0):
        self.matrix_size = (K+I) * J * 8
        mem = psutil.virtual_memory()
        self.max_bs = math.floor(mem.free / self.matrix_size - 5)
        self.magic_numbers = [1,1.5,2,2.75,4,6.17,10,16.88,29.34]

    def num_bases_to_remove(self):
        mem = psutil.virtual_memory()
        bs = math.floor(mem.free/self.matrix_size - 5)
        return -bs if bs < 0 else 0


