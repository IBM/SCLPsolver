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



class rewind_info():

    def __init__(self, pivots, dx, dq):
        self._pivots = pivots
        self._dx = dx
        self._dq = dq

    @property
    def pivots(self):
        return self._pivots

    @property
    def dx(self):
        return self._dx

    @property
    def dq(self):
        return self._dq