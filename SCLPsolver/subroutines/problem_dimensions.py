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



class problem_dimensions():

    def __init__(self, KK, JJ, totalK=None, totalJ=None):
        self._j = JJ
        self._k = KK
        self._totalJ = totalJ
        self._totalK = totalK

    @property
    def JJ(self):
        return self._j

    @property
    def KK(self):
        return self._k

    @property
    def totalJ(self):
        if self._totalJ is None:
            return self._j
        else:
            return self._totalJ

    @property
    def totalK(self):
        if self._totalK is None:
            return self._k
        else:
            return self._totalK