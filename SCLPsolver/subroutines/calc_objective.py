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


def calc_objective(formulation, u, x, p, q, tau):

    NN = len(tau)
    t = np.cumsum(np.hstack((0., tau)))
    TT = t[NN]
    part1 = np.dot(np.dot(formulation.gamma, u[:formulation.J,:]), tau)
    ddtau = tau*(t[:-1] + t[1:])/2
    part2 = np.dot(np.dot(formulation.c, u[:formulation.J,:]), tau * TT - ddtau)
    if formulation.L == 0:
        part3 = 0
    else:
        part3 = np.dot(np.dot(formulation.d,  ((x[formulation.K:, :-1]+x[formulation.K:, 1:])/ 2)),tau)
    primobjective = part1 + part2 + part3
    part4 = np.dot(np.dot(formulation.alpha,p[:formulation.K,:]),tau)
    part5 = np.dot(np.dot(formulation.a,p[:formulation.K,:]), ddtau)
    if formulation.I == 0:
        part6 = 0
    else:
        part6 = np.dot(np.dot(formulation.b,  ((q[formulation.J:, :-1]+q[formulation.J:, 1:])/ 2)),tau)
    dualobjective = part4 + part5 + part6
    obj = (primobjective + dualobjective) / 2
    err = abs(dualobjective - primobjective)
    return obj, err