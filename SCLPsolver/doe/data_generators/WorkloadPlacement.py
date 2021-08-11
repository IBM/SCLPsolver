# Copyright 2021 IBM Corporation
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


def generate_workload_placement_data(T, I, J, R, P, a, mu, x0, r, rprime):
    """Generate a random SCLP model of the Workload Placement problem.

    For now, only CPU no RAM.

    Suppose I = 2, J = 3
    Then K = 6
    H is I x K
    H = [[1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]] representing all classes on server 1 in 1st row, etc.

    suppose mu = (4, 5)
    G is J x K = 3x6
    G = [[-4, 0, 0, -5, 0, 0], [0, -4, 0, 0, -5, 0], [0, 0, -4 ,0, 0, -5]]

    Fprime is J x K = 3x6
    Fprime = [[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]

    F is J x (K-J) = 3x3
    F = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    alpha is J vector with initial number of jobs in each class

    Parameters
    ----------
    T : numeric
        Time horizon
    I : int
        Number of servers
    J : intֹ
        Number of job classes
    R : np.ndarray
        1D array of `int` (size I) containing the total RAM on servers
    P : np.ndarray
        1D array of `int` (size I) containing the total CPU rates (tasks per unit time) on servers
    a : np.ndarray
        1D array of `int` (size J) containing the task arrival rates by class
    mu : np.ndarray
        1D array of `int` (size J) containing the task service rates by class
    x0 : np.ndarray
        2D array of `int` (size I x J) containing the initial buffer quantity for server, class
    r : np.ndarray
        1D array of `int` (size J) containing the run-independent RAM requirements by class
    rprime : np.ndarray
        1D array of `int` (size J) containing the run-dependent RAM requirements by class

    Returns
    -------
    A tuple with the following values:
        G
        H
        F
        gamma
        c
        d
        alpha
        a
        b
        T
        total_buffer_cost
        cost
    """

    # K number of buffers / flows
    K = I * J

    # H is composed of 2 parts: CPU constraints and eventually plus RAM constraints
    H = np.array([np.repeat([ii == i for ii in range(I)], J) for i in range(I)], dtype="int")

    # b CPU per server and eventually RAM
    b = P.copy()

    # G Task flows between buffers
    G = np.array([[jj == j for jj in range(J)] * I for j in range(J)], dtype="int") * np.repeat(mu, J) * -1

    # F relates buffers belong to each server
    F = np.array([[jj == j for jj in range(J)] * (I-1) for j in range(J)], dtype="int")

    # alpha initial values of tasks in buffers
    alpha = x0.sum(axis=0)

    # gamma unit cost per unit time of CPU of server and class
    gamma = np.zeros(K)

    # d is cost per unit time per task per server in buffer
    d1 = np.ones(J)
    d2 = np.ones(K-J)
    d = np.matmul(d1, F) -d2

    # cost ?
    cost = np.ones(J) # cost per unit time processing by class, hard-coded to 1 for now

    # c is cost per unit time of the buffers on the controls for the objective function
    c = np.matmul(d1, G)

    # total_buffer_cost is for inverse transformation when there is no F
    # not needed for this model
    total_buffer_cost = (0, 0)

    return G,H,F,gamma,c,d,alpha,a,b,T,total_buffer_cost,cost



def generate_one_server_two_classes(a1,a2,b1,c1,c2,tau1,tau2,alpha1,alpha2,flag=True):
    a = np.array((a1,a2))
    b = np.array((b1,))
    d = np.empty(0)
    alpha = np.array((alpha1, alpha2))
    mu1, mu2 = 1.0/tau1, 1.0/tau2
    if flag:
        gamma = np.zeros(2)
        G = np.diag((1.0, 1.0))
        H = np.array(((tau1, tau2),))
    else:
        gamma = np.zeros(2)
        G = np.diag((mu1, mu2))
        H = np.array(((1.0, 1.0),))
    F = np.empty((2, 0))
    cost = np.array((c1, c2))
    total_buffer_cost = (np.inner(cost, alpha), np.inner(cost, a))
    c = np.matmul(cost, G)
    T = None

    return G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost