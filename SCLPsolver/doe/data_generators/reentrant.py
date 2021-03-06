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


# General Reentrant line:
# goes through machines in some random order.
# holding costs are geneal random.
# More initial fluid in buffer 1,
# random initial amounts in all the others buffers.

# We generate random problem instances as follows:
# system dynamics are:
# Fluid flows from step 1 to 2 ... to K and out.
#  a(1) = 100.
# initial buffer levels are a(k)= ~U(0,40), k=2,...,K
# average processing times of step k are m(k)= ~U(0,3)
# average input rates are alpha(k)= ~U(0,0.01)
# steps k at machines i(k), k=1,....
# M(i,k) = m(k) if step k on machine i, 0 else.
# resource limits:  b(i)=1,  with sum_k M(i,k)*u(k) <= b(i).
# holding costs rates for fluid in buffer k:
#  cost(k) = ~U(0,2) .

def generate_reentrant_data(seed, K, I, h_rate = 0.3, hdist = np.random.rand, hdist_params = (), first_alpha = 100, alpha_rate = 40,
                            alpha_dist = np.random.rand, alpha_dist_params = (), a_rate = 0.01, a_dist = np.random.rand, a_dist_params = (),
                            cost_scale = 2, cost_dist = np.random.rand,  cost_dist_params = (), gamma_rate=0,
                            gamma_dist=np.random.rand, gamma_dist_params=(), c_scale = 0, c_dist = np.random.rand,  c_dist_params = ()):

    np.random.seed(seed)
    b = np.ones(I)
    G = np.eye(K) - np.diag(np.ones(K - 1), -1)

    # construct random machine constituency matrix
    cols = np.arange(K)
    np.random.shuffle(cols)
    H = np.zeros((I, K))
    rows = np.concatenate((np.arange(I), np.random.choice(I, K-I, True)))
    H[rows, cols] = h_rate * hdist(*hdist_params, K)

    # initial fluid
    alpha = alpha_rate * alpha_dist(*alpha_dist_params, K)
    alpha[0] = first_alpha

    # exogenous input rate
    a = a_rate * a_dist(*a_dist_params, K)

    F = np.empty((K, 0))
    d = np.empty(0)

    if gamma_rate == 0:
        gamma = np.zeros(K)
    else:
        gamma = gamma_rate * gamma_dist(*gamma_dist_params, K)
    if c_scale != 0:
        c = c_scale * c_dist(*c_dist_params, K) * np.random.choice([-1, 1], K, True)
    else:
        c = np.zeros(K)
    cost = None
    if cost_scale != 0:
        cost = cost_scale * cost_dist(*cost_dist_params, K)
        # this produce negative and positive costs!
        c += np.matmul(cost, G)
        total_buffer_cost = (np.inner(cost, alpha), np.inner(cost, a))
    else:
        total_buffer_cost = (0, 0)
    return G, H, F, gamma, c, d, alpha, a, b, None, total_buffer_cost, cost