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
from enum import Enum
from subroutines.parametric_line import parametric_line


class line_type(Enum):
    SCLP_main = 0
    SCLP_sub = 1
    SCLP_orthogonal = 2
    MCLP_dual = 3
    MCLP_primal = 4
    MCLP_both = 5

class parametric_line_ex(parametric_line):

    def __init__(self, x_0, q_N, theta_bar, T=0, del_T=1, del_x_0=None, del_q_N=None, gamma=None, del_gamma=None, alpha=None,
                 del_alpha = None, xlambda = None, mu = None, Kset_0=None, Jset_N=None, B1=None, B2=None, ltype=line_type.SCLP_main):
        super().__init__(x_0, q_N, theta_bar, T, del_T, del_x_0, del_q_N, Kset_0, Jset_N, B1, B2, ltype)
        self._gamma = gamma
        self._alpha = alpha
        self._del_gamma = del_gamma
        self._del_alpha = del_alpha
        self._xlambda = xlambda
        self._mu = mu

    def is_main(self):
        return self._ltype == line_type.SCLP_main

    def is_sub(self):
        return self._ltype == line_type.SCLP_sub

    def is_orthogonal(self):
        return self._ltype == line_type.SCLP_orthogonal

    def is_SCLP(self):
        return self._ltype in [line_type.SCLP_main, line_type.SCLP_sub, line_type.SCLP_orthogonal]

    def is_MCLP_dual(self):
        return self._ltype == line_type.MCLP_dual

    def is_MCLP_primal(self):
        return self._ltype == line_type.MCLP_primal

    def is_MCLP_both(self):
        return self._ltype == line_type.MCLP_both

    def _forward_to(self, delta):
        if not self.is_SCLP():
            if self._gamma is not None and self._del_gamma is not None:
                self._gamma += self._del_gamma * delta
            if self._alpha is not None and self._del_alpha is not None:
                self._alpha += self._del_alpha * delta
            if self._xlambda is not None:
                self._xlambda -= self._xlambda * delta
            if self._mu is not None:
                self._mu -= self._mu * delta
        super()._forward_to(delta)

    def _backward_to(self, delta):
        if not self.is_SCLP():
            if self._gamma is not None and self._del_gamma is not None:
                self._gamma -= self._del_gamma * delta
            if self._alpha is not None and self._del_alpha is not None:
                self._alpha -= self._del_alpha * delta
            if self._xlambda is not None:
                self._xlambda += self._xlambda * delta
            if self._mu is not None:
                self._mu += self._mu * delta
        super()._forward_to(delta)

