import pandas as pd
import pytest
from scipy.integrate import quad
import matplotlib.pyplot as plt

import os, sys
import numpy as np

proj = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
sys.path.append(proj)

from SCLPsolver.SCLP import SCLP, SCLP_settings
from SCLPsolver.doe.data_generators.WorkloadPlacement import *

from SCLPsolver.doe.doe import *

seeds = [1234]


# def integrate(f, low, up, intervals=200):
#     tt = np.linspace(low, up, intervals+1)
#     y = [f(t) for t in tt]
#     F = (0.5*(y[0]+y[-1]) + np.sum(y[1:-1]))*(up-low)/intervals
#     return F

def integrate(f, low, up):
    val, est_err = quad(f,low,up)
    return val

integrate_m = np.vectorize(integrate)


def test_integrate():
    assert abs(integrate(lambda x: 1, 0, 4) - 4) < 0.001
    assert abs(integrate(lambda x: x, 2, 6) - 16) < 0.001
    assert abs(integrate(lambda x: np.sin(x), 0, np.pi/2.0) - 1) < 0.001


def test_integrate_m():
    H1 = np.array((lambda x: 1,))
    assert abs(integrate_m(H1, 0, 4) - 4) < 0.001
    H2 = np.array(((lambda x: 1, lambda x: x),(lambda x: np.pi*np.sin(np.pi*x), lambda x: np.pi*np.sin(2*np.pi*x))))
    assert np.allclose(integrate_m(H2, 0, 1), np.array(((1.0, 0.5), (2.0, 0.0))))

np.random.seed(1234)

TT = 100
I = 10      # num servers
K = 100     # num buffers
J = K       # num flows

aa = np.random.uniform(2.0, 5.0, K)  # arrival rates at buffers tasks per unit time
bb = np.ones(I)  # cpu limit
cc = np.random.uniform(1.0, 2.0, K)  # cost per unit time of buffers
alpha0 = np.random.uniform(10.0, 20.0, K)  # initial buffer quantities
mu = np.random.uniform(5.0, 25.0, K) # mean job service rates

ntests = 100

epsilons = [(0.02), (0.04), (0.1), (0.2), (0.4)]

means_df = pd.DataFrame({'epsilon': [], 'MeanSOA': [], 'MeanSEP':[], 'MeanRelDiff':[]})

@pytest.mark.parametrize("epsilon", epsilons)
def test_perturbed(epsilon):

    #np.random.seed(seed)

    tau = np.divide(1, mu)

    # 1. Model 1, eta is control var
    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_paper(aa,
                                                                                                           bb,
                                                                                                           cc,
                                                                                                           tau,
                                                                                                           alpha0,
                                                                                                           False)
    print(f'Model 1 G={G} H={H}')

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
    real_obj1 = tot_buf_cost - SCLP_obj

    eta = u[0:J, :]
    u = np.multiply(eta.transpose(), mu).transpose()
    u_m1 = u.copy()
    t_m1 = t.copy()

    print(f'Step 1 (Model 1): t={t} tau={tau} mu={mu} u={u} eta={eta}')

    # 2. Model 2, u is control var
    G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_paper(aa,
                                                                                                           bb,
                                                                                                           cc,
                                                                                                           tau,
                                                                                                           alpha0,
                                                                                                           True)

    print(f'Model 2 G={G} H={H}')

    solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
    t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
    tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
    real_obj2 = tot_buf_cost - SCLP_obj

    u = u[0:J, :]
    eta = np.multiply(u.transpose(), tau).transpose()

    print(f'Step 2 (Model 2): t={t} tau={tau} mu={mu} u={u} eta={eta}')

    # 3. make sure objectives of 1,2 are the same
    print(f'Step 3: objectives obj1={real_obj1}  obj2={real_obj2}')

    assert abs(real_obj1 - real_obj2) < 0.001

    t_print = tuple(range(0, TT + 1))

    tau_t_1 = gen_uncertain_param(tau, (0, TT), (-epsilon / 2.0, epsilon / 2.0), uncertain_func=sin_uncertainty_low)
    tau_t_2 = gen_uncertain_param(tau, (0, TT), (-epsilon / 2.0, epsilon / 2.0), uncertain_func=sin_uncertainty_low)

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times','Palatino', 'New Century Schoolbook', 'Bookman', 'Computer Modern Roman']
    plt.rcParams['text.usetex'] = True
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['axes.labelsize'] = 12

    plt.clf()
    plt.plot(t_print, [(tau_t_1[0](t), tau_t_2[0](t)) for t in t_print])
    plt.ylim(tau[0] * (1-0.25), tau[0]*(1+0.25))
    plt.xlabel('Time $t$')
    plt.ylabel(r'Mean Service Time $\tau(t)$')
    #plt.title(rf'Example randomized arrival rates for $\epsilon=${epsilon}')
    plt.grid(True)
    plt.savefig(f'tau_t_{epsilon}.pdf')
    #plt.show()

    # return

    results = list()

    for nt in range(ntests):

        ## Bertsimas State of the Art
        #
        #
        # 4. Define tau_j(t)
        tau_t = gen_uncertain_param(tau, (0, TT), (-epsilon / 2.0, epsilon / 2.0), uncertain_func=sin_uncertainty_low)

        # print(f'Step 4: uncertain tau({t_print})={np.array([list(tau_t[j](t) for j in range(J)) for t in t_print]).transpose()}')


        # 5. Robust model with Box uncertainty Model 2 with tau_bar
        tau_bar = tau * (1 + 0.5*epsilon)

        G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_paper(aa,
                                                                                                           bb,
                                                                                                           cc,
                                                                                                           tau_bar,
                                                                                                           alpha0,
                                                                                                           True)

        solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
        t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
        tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
        real_obj5 = tot_buf_cost - SCLP_obj

        u = u[0:J,:]
        eta = np.multiply(u.transpose(), tau).transpose()

        # print(f'Step 5 (Model 2 with tau_bar): t={t} tau_bar={tau_bar} mu={mu} u={u} eta={eta}')
        # print(f'     Objectives: model 2: {real_obj2} model 5: {real_obj5}')
        assert real_obj5 >= real_obj2

        t_index = lambda x: min([i-1 for i, ti in enumerate(t) if ti > x] + [len(t)-2])

        def make_eta_t(k):
            return lambda t: u[k, t_index(t)] * tau[k] * (1 - 0.5 * epsilon)
        eta_t = np.array([make_eta_t(k) for k in range(K)])

        # print(f'eta={eta}')
        # print(f'eta_t({[t for t in range(0,TT+1,2)]}) = {np.array([list(eta_t[j](t) for j in range(J)) for t in t_print]).transpose()}')

        u_mat = np.array([[eta_t[k]((t+5.0)/10.0)/tau_t[k]((t+5.0)/10.0) for t in range(TT*10)] for k in range(K)])
        # def make_u_t(k):
        #      return lambda t: eta_t[k](t) / tau_t[k](t)

        #u_t = np.array([make_u_t[k] for k in range(K)])

        # print(f'u={u}')
        # print(f'u_t({[t for t in range(0,TT+1,2)]}) = {np.array([list(u_t[j](t) for j in range(J)) for t in t_print]).transpose()}')

        def make_x_R_t(k):
            # return lambda t: alpha[k] + a[k] * t - integrate(u_t[k], 0, t)
            return lambda t: alpha[k] + a[k] * t - np.sum(u_mat[k,0:round(t*10)])/10.0

        x_R_t = np.array([make_x_R_t(k) for k in range(K)])
        # print(f'x_R_t({[t for t in range(0,TT+1,2)]}) = {np.array([list(x_R_t[j](t) for j in range(J)) for t in t_print]).transpose()}')

        obj_5 = np.sum([integrate(x_R_t[k], 0, TT) * cost[k] for k in range(K)])
        print(f'run {nt} Step 5: real_obj2={real_obj2} real_obj5={real_obj5} obj_5={obj_5}')

        # Server effort proportion model
        #
        # 6. Robust model with Box uncertainty Model 1 with mu_bar
        mu_bar = mu / (1 - 0.5*epsilon)
        tau_bar_bar = np.divide(1, mu_bar)

        G, H, F, gamma, c, d, alpha, a, b, T, total_buffer_cost, cost = generate_workload_placement_data_paper(aa,
                                                                                                           bb,
                                                                                                           cc,
                                                                                                           tau_bar_bar,
                                                                                                           alpha0,
                                                                                                           False)

        solution, STEPCOUNT, param_line, res = SCLP(G, H, F, a, b, c, d, alpha, gamma, TT)
        t, x, q, u, p, pivots, SCLP_obj, err, NN, tau_intervals, maxT = solution.get_final_solution(True)
        tot_buf_cost = np.inner(cost, alpha * TT) + np.inner(cost, a) * TT ** 2 / 2
        real_obj6 = tot_buf_cost - SCLP_obj

        eta = u[0:J, :]
        u = np.multiply(eta.transpose(), mu).transpose()

        # print(f'Step 6 (Model 1 with mu_bar): t={t} mu_bar={mu_bar} mu={mu} u={u} eta={eta}')
        # print(f'     Objectives: model 1: {real_obj1} model 6: {real_obj6}')
        assert real_obj6 <= real_obj1

        t_index = lambda x: min([i-1 for i, ti in enumerate(t) if ti > x] + [len(t)-2])

        # print(f'eta={eta}')
        # print(f'eta_t({[t for t in range(0,TT+1,2)]}) = {np.array([(eta_t[0](t), eta_t[1](t)) for t in t_print]).transpose()}')
        #
        # print(f'u_t({[t for t in range(0,TT+1,2)]}) = {np.array([(u_t[0](t), u_t[1](t)) for t in t_print]).transpose()}')
        #
        # print(f'x_R_t({[t for t in range(0,TT+1,2)]}) = {np.array([(x_R_t[0](t), x_R_t[1](t)) for t in t_print]).transpose()}')

        u_mat2 = np.array([[eta[k,t_index((t+5.0)/10.0)]/tau_t[k]((t+5.0)/10.0) for t in range(TT*10)] for k in range(K)])
        # def make_u2_t(k):
        #     return lambda x: eta[k, t_index(x)] / tau_t[k](x)
        #
        # u2_t = np.array([make_u2_t(k) for k in range(K)])

        # print(f'u={u}')
        # print(f'u_t({[t for t in range(0,TT+1,2)]}) = {np.array([list(u_t[j](t) for j in range(J)) for t in t_print]).transpose()}')


        def make_x_R2_t(k):
            # return lambda x: alpha[k] + a[k] * x - integrate(u2_t[k], 0, x)
            return lambda t: alpha[k] + a[k] * t - np.sum(u_mat2[k,0:round(t*10)])/10.0

        x_R2_t = np.array([make_x_R2_t(k) for k in range(K)])

        obj_6 = np.sum([integrate(x_R2_t[k], 0, TT) * cost[k] for k in range(K)])
        print(f'Run {nt} Step 6: real_obj1={real_obj1} real_obj6={real_obj6} obj_6={obj_6}')

        results.append([nt, real_obj1, real_obj5, real_obj6, obj_5, obj_6])

    results_df = pd.DataFrame(results, columns=['Iteration', 'Obj', 'RO_SOA', 'RO_SEP', 'Obj_SOA', 'Obj_SEP'])
    assert(all(results_df['Obj_SOA'] > results_df['Obj_SEP']))

    plt.clf()
    #fig, (soa, sep) = plt.subplots(1,2)
    plt.hist(results_df['Obj_SOA'], bins=10)
    plt.xlabel(f'State of the Art')
    plt.savefig(f'obj_hist_soa_{epsilon}.pdf')

    plt.clf()
    plt.hist(results_df['Obj_SEP'], bins=10)
    plt.xlabel(f'Server Effort Proportion')
    plt.savefig(f'obj_hist_sep_{epsilon}.pdf')
    #fig.suptitle(f'Objective Distribution $\epsilon=${epsilon}')

    results_df['RelDiff'] = (results_df['Obj_SOA'] - results_df['Obj_SEP']) / results_df['Obj_SOA'] * 100

    results_df.to_csv(f'results_{epsilon}.csv')

    means_df.loc[len(means_df.index)] = [epsilon, np.mean(results_df['Obj_SOA']), np.mean(results_df['Obj_SEP']), np.mean(results_df['RelDiff'])]
    means_df.to_csv('summary.csv')

    plt.clf()
    plt.hist(results_df['RelDiff'])
    #plt.title(f'Relative Improvement of SEP for $\epsilon=${epsilon}')
    plt.xlabel('Percent improvement of objective value')
    plt.savefig(f'rel_diff_hist_{epsilon}.pdf')

    plt.clf()
    plt.scatter(means_df['epsilon']/2, means_df['MeanRelDiff'])
    plt.xlabel('Uncertainty $\epsilon$')
    plt.ylabel('Percent improvement')
    plt.xticks(np.arange(0.0, 0.21, 0.02))
    plt.savefig(f'mean_rel_diff.pdf')
