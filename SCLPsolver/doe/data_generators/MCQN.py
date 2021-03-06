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

# General Multi - Class Queueing Network:
# buffers numbered k = 1, ..., K.
# Each buffer is served by one of the I machines,
# buffer k served by machine i(k).
# we generate random constituencies of the machines.
# average service time m(k) = ~U(0, 3).
# M(i, k) = m(k) if i(k) = i, 0 else.

# fluid from buffer k goes to buffer l in proportion
# p(k, l), where the these are random, and sum to < 1,
# 1 - sum_l p(k, l) leaves the system.
#
# initial buffer levels are a(k) = ~U(0, 40), k = 1, ..., K
# random small input rate alpha(k) = ~U(0, 0.01)

# random holding costs cost(k) = ~U(0, 2).
# resource limits: b(i) = 1, with sum_k M(i, k) * u(k) <= b(i).

def generate_MCQN_data(seed, K, I, nz = 0.4, sum_rate=0.8, gdist=np.random.rand, gdist_params=(), h_rate = 0.6, hdist = np.random.rand,
                       hdist_params = (), alpha_rate = 40, alpha_dist = np.random.rand, alpha_dist_params = (), a_rate = 0.01, a_dist
                       = np.random.rand, a_dist_params = (), cost_scale = 2, cost_dist = np.random.rand,  cost_dist_params = (),
                       gamma_rate = 0, gamma_dist=np.random.rand, gamma_dist_params=(), c_scale = 0, c_dist = np.random.rand,  c_dist_params = ()):

    np.random.seed(seed)
    b = np.ones(I)

    # transition probabilities
    # ~nz of them are > 0,
    # they sum up to ~sum_rate so ~1-sum_rate flows out.

    if gdist is np.random.rand:
        P = gdist(K,K)
    else:
        P = gdist(*gdist_params, (K,K))
    P-= (1- nz) * np.ones((K,K)) + np.eye(K)
    P[P < 0] = 0
    P[0, K-1] += 0.1
    coeff = (1/sum_rate - 1) * 2
    P+= np.diag(np.full(K-1,0.1),-1)
    P /= np.outer(np.ones(K)+ coeff * np.random.rand(K), sum(P))
    G = np.eye(K) - P

    # construct random machine constituency matrix
    cols = np.arange(K)
    np.random.shuffle(cols)
    H = np.zeros((I, K))
    rows = np.concatenate((np.arange(I),np.random.choice(I,K-I,True)))
    H[rows,cols] = h_rate * hdist(*hdist_params, K)

    # initial fluid
    alpha = alpha_rate * alpha_dist(*alpha_dist_params, K)

    # exogenous input rate
    a = a_rate * a_dist(*a_dist_params, K)

    F = np.empty((K,0))
    d = np.empty(0)

    if gamma_rate==0:
        gamma = np.zeros(K)
    else:
        gamma = gamma_rate * gamma_dist(*gamma_dist_params, K)
    if c_scale != 0:
        c = c_scale * c_dist(*c_dist_params, K) * np.random.choice([-1,1],K,True)
    else:
        c = np.zeros(K)
    cost = None
    if cost_scale != 0:
        cost = cost_scale * cost_dist(*cost_dist_params, K)
        #this produce negative and positive costs!
        c += np.matmul(cost,  G)
        total_buffer_cost = (np.inner(cost,  alpha),np.inner(cost,  a))
    else:
        total_buffer_cost = (0,0)
    return G,H,F,gamma,c,d,alpha,a,b,None,total_buffer_cost, cost


def perturb_MCQN_data(seed, rel_perturbation, symmetric, G0, H0, F0, a0, b0, c0, d0, alpha0, gamma0):
    if seed:
        np.random.seed(seed)
    if symmetric:
        lower, upper = -1, 1
    else:
        lower, upper = 0, 1
    # F = 0
    # H, a, b, alpha >= 0
    G = G0 * (1 + rel_perturbation * np.random.uniform(lower, upper, size=G0.shape))
    np.fill_diagonal(G, 1)
    H = H0 * (1 - rel_perturbation * np.random.uniform(0, upper, size=H0.shape))
    F = F0 * (1 + rel_perturbation * np.random.uniform(lower, upper, size=F0.shape))
    a = a0 * (1 + rel_perturbation * np.random.uniform(0, upper, size=a0.shape))
    b = b0 * (1 + rel_perturbation * np.random.uniform(0, upper, size=b0.shape))
    c = c0 * (1 + rel_perturbation * np.random.uniform(lower, upper, size=c0.shape))
    d = d0 * (1 + rel_perturbation * np.random.uniform(lower, upper, size=d0.shape))
    alpha = alpha0 * (1 + rel_perturbation * np.random.uniform(0, upper, size=alpha0.shape))
    gamma = gamma0 * (1 + rel_perturbation * np.random.uniform(lower, upper, size=gamma0.shape))
    return G,H,F,a,b,c,d,alpha,gamma