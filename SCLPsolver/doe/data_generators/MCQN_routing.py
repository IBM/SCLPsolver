import numpy as np
from subroutines.matlab_utils import find

# General Multi-Class Queueing Network, with rouitng:
# buffers numbered k=1,...,K.
# flows numbered j=1,...,J
# Each flow empties one buffer, and feeds some of the others.
# Each flow is served by one of the I machines,
#  flow j empties buffer k(j).
#  flow j is served by macine i(j).
# we generate random constituencies of flows our of buffers.

# we generate random constituencies of the machines.
# average service time  m(j)= ~U(0,3).
# M(i,j) = m(j) if i(j)=i, 0 else.

# fluid from buffer k(j) goes to buffer l in proportion
# p(k(j),l), where these are random, and sum to <1,
# 1-sum_l p(k(j),l) leaves the system.
#
# initial buffer levels are a(k)= ~U(0,40), k=1,...,K
# random small input rate   alpha(k)= ~U(0,0.01)

# random holding costs  cost(k) = ~U(0,2) .
# in addition we add small random costs for each flow,
#  c = cost*G + ~U(0,0.02).
# this additional costs avoids degeneracy.
# resource limits:  b(i)=1,  with sum_k M(i,k)*u(k) <= b(i).
#
#
# We solve this problem for a finite time horizon T
# T is calculated to be approximately the draining time of the sysem

def generate_MCQN_routing_data(seed, K, I, J, nz = 0.4, sum_rate=0.8, gdist=np.random.rand, gdist_params=(), h_0 = 0,
                               h_rate = 3, hdist = np.random.rand, hdist_params = (), alpha_rate = 40, alpha_dist =
                               np.random.rand, alpha_dist_params = (), a_rate = 0.01, a_dist = np.random.rand, a_dist_params =
                               (), cost_scale = 2, cost_dist = np.random.rand,  cost_dist_params = (), gamma_rate=0,
                               gamma_dist=np.random.rand, gamma_dist_params=(), c_scale = 0, c_dist = np.random.rand,  c_dist_params = ()):


    np.random.seed(seed)
    b = np.ones(I)

    # transition probabilities
    # ~nz of them are > 0,
    # they sum up to ~sum_rate so ~1-sum_rate flows out.
    if gdist is np.random.rand:
        P = gdist(K, J)
    else:
        P = gdist(*gdist_params, (K,J))
    P -= (1 - nz) * np.ones((K, J))
    P[P < 0] = 0

    #TODO: check if correct, understand whats this!
    #div = sum(P) + ones(1, J). * (sum(P) == 0)
    #P = P. / ((ones(K, 1) + 0.5 * rand(K, 1)) * div)
    div = sum(P)
    np.add(div, np.ones(J), where = div == 0, out = div)
    coeff = (1 / sum_rate - 1) * 2
    P /= np.outer(np.ones(K) + coeff * np.random.rand(K), div)
    G = - P

    #construct random buffer/flow assignments
    cols = np.arange(J)
    np.random.shuffle(cols)
    rows = np.concatenate((np.arange(K), np.random.choice(K, J-K, True)))
    G[rows, cols] = 1
    cols = find(sum(G) - 1 >=  - 1E-11)
    for i in cols:
        G[np.random.choice(find(sum(G) - 1 <= - 1E-11),1),i] = - sum_rate
    # construct random machine constituency matrix
    cols = np.arange(J)
    np.random.shuffle(cols)
    H = np.zeros((I, J))
    rows = np.concatenate((np.arange(I), np.random.choice(I, J-I, True)))
    H[rows, cols] = h_0 + h_rate * hdist(*hdist_params, J)

    # initial fluid
    alpha = alpha_rate * alpha_dist(*alpha_dist_params, K)

    # exogenous input rate
    a = a_rate * a_dist(*a_dist_params, K) + a_rate

    F = np.empty((K, 0))
    d = np.empty(0)

    if gamma_rate == 0:
        gamma = np.zeros(J)
    else:
        gamma = gamma_rate * gamma_dist(*gamma_dist_params, J)
    if c_scale != 0:
        c = c_scale * c_dist(*c_dist_params, J) * np.random.choice([-1,1],J,True)
    else:
        c = np.zeros(J)
    if cost_scale != 0:
        cost = cost_scale * cost_dist(*cost_dist_params, K)
        #this produce negative and positive costs!
        c += np.matmul(cost,  G)
        buffer_cost = (np.inner(cost,  alpha),np.inner(cost,  a))
    else:
        buffer_cost = (0,0)

    # Calculating a value for T
    #  ~0.2 is probability of leaving system at each service
    #  so each item in the system takes average ~5 steps.
    #  average service time is  ~1.5  per operation.
    #  total items in system to start with:  ~K*20.
    #  ignore the rate 0.005 exogenous input rate
    #  total average number of operations required:  ~K*20*5
    #  they are served by I machines, providing service rate I/1.5 .
    #  total time to do the work  ~K*20*5*1.5 / I
    #
    #  This assumes that machines are fully occupied, but the system is not optimized.
    #
    #  we shall take T as 1.2 that value

    T = 1.2*(150*K/I)

    return G, H, F, gamma, c, d, alpha, a, b, T, buffer_cost