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


def generate_workload_placement_data_new(a1, a2, b1, c1, c2, tau1, tau2, alpha1, alpha2, normalize=True):
    """
    Generate workload data, new format.
    This function currently works for a single server with two queues for servicing two job classes.

    Parameters
    ----------
    a1 : float
        task arrival rate of class 1 in tasks per unit time
    a2 : float
        task arrival rate of class 2 in tasks per unit time
    b1 : float
        cpu limit of server 1
    c1 : float
        cost per unit time of buffer 1
    c2 : float
        cost per unit time of buffer 2
    tau1 : float
        time to complete task of class 1
    tau2 : float
        time to complete task of class 2
    alpha1 : float
        initial quantity of buffer 1
    alpha2 : float
        initial quantity of buffer 2
    normalize : bool
        Generate a model where the decision variable is normalized to a fraction of the total server capacity (True),
        or is the actual flow rate (False).
        Default True.
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
    a = np.array((a1,a2))
    b = np.array((b1,))
    d = np.empty(0)
    alpha = np.array((alpha1, alpha2))
    gamma = np.zeros(2)
    mu1, mu2 = 1.0 / tau1, 1.0 / tau2
    if normalize:
        G = np.diag((1.0, 1.0))
        H = np.array(((tau1, tau2),))
    else:
        G = np.diag((mu1, mu2))
        H = np.array(((1.0, 1.0),))
    F = np.empty((2, 0))
    cost = np.array((c1, c2))
    total_buffer_cost = (np.inner(cost, alpha), np.inner(cost, a))
    c = np.matmul(cost, G)
    T = None

    return G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost

def generate_workload_placement_data_paper(a, b, c, tau, alpha, normalize=True):
    """
    Generate workload data, new format.
    This function currently works for a single server with two queues for servicing two job classes.

    Parameters
    ----------
    a : list of float
        task arrival rates by job buffer (vector of size K)
    b : list of float
        cpu limits per server (vector of size I)
    c : list of float
        holding cost per unit time per buffer (vector of size K)
    tau : list of float
        mean time to complete tasks by job class (vector of size J)
    alpha : alpha float
        initial quantity of buffers (vector of size K)
    normalize : bool
        Generate a model where the decision variable is normalized to a fraction of the total server capacity (True),
        or is the actual flow rate (False).
        Default True.
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
    I = len(b)
    K = len(tau)
    J = len(a)
    a = np.array(a)
    b = np.array(b)
    d = np.empty(0)
    alpha = np.array(alpha)
    gamma = np.zeros(K)
    tau = np.array(tau)
    mu = np.divide(np.ones(shape=tau.shape), tau)
    if normalize:
        G = np.eye(K) # no flows between buffers yet
        H = np.array([[j % I == i and tau[j] or 0 for j in range(J)] for i in range(I)])
    else:
        G = np.diag(mu)
        H = np.array([[j % I == i and 1 for j in range(J)] for i in range(I)])
    F = np.empty((K, 0))
    cost = np.array(c)
    total_buffer_cost = (np.inner(cost, alpha), np.inner(cost, a))
    c = np.matmul(cost, G)
    T = None

    return G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost