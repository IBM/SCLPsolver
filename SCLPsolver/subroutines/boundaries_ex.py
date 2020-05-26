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





class boundaries():
    __slots__ = ['x0', 'u0', 'uN', 'xN', 'q0', 'qN', 'p0', 'pN']

    def __init__(self, x0=None, u0=None, uN=None, xN=None, q0=None, p0=None, qN=None, pN=None):
        self.x0 = x0
        self.u0 = u0
        self.uN = uN
        self.xN = xN
        self.q0 = q0
        self.p0 = p0
        self.qN = qN
        self.pN = pN