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



class collision_info():

    def __init__(self, case, delta=None, N1=None, N2=None, v1=None, v2=None, rz = None, tol_coeff=1,
                 had_resolution=False, stable_iteration = True):
        self._N1 = N1
        self._N2 = N2
        self._rz = rz
        self._tol_coeff = tol_coeff
        if v1 is None:
            self._v1 = []
        else:
            self._v1 = v1
        if v2 is None:
            self._v2 = []
        else:
            self._v2 = v2
        self._case = case
        self._delta = delta
        self._Nnew = None
        self._rewind_info = None
        self._had_resolution = had_resolution
        self._ztau_ind = None
        self.from_ztau = False
        self.alternative = None
        self.stable_iteration = stable_iteration

    @property
    def N1(self):
        return self._N1

    @property
    def N2(self):
        return self._N2

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def case(self):
        return self._case

    @case.setter
    def case(self, value):
        self._case = value

    def __eq__(self, other):
        return self._N1 == other.N1 and self._N2 == other.N2 and self._v1 == other.v1 and self._v2 == other.v2 and self._case == other.case

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self, value):
        self._delta = value

    @property
    def Nnew(self):
        return self._Nnew

    @Nnew.setter
    def Nnew(self, value):
        self._Nnew = value

    @property
    def rewind_info(self):
        return self._rewind_info

    @rewind_info.setter
    def rewind_info(self, value):
        self._rewind_info = value

    @property
    def had_resolution(self):
        return self._had_resolution

    @had_resolution.setter
    def had_resolution(self, value):
        self._had_resolution = value

    @property
    def rz(self):
        return self._rz

    @property
    def tol_coeff(self):
        return self._tol_coeff

    @property
    def ztau_ind(self):
        return self._ztau_ind

    @ztau_ind.setter
    def ztau_ind(self, value):
        self._ztau_ind = value
