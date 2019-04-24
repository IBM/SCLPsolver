from .matlab_utils import *

#check indexing
def calc_order_ratio(v1,v2,N1,N2,klist,jlist,dx,dq,x,del_x,q,del_q,tau,dtau,delta):

    correct = True
    if v1 > 0 and v2 > 0:
        k1 = find(klist == v1)
        dx1 = dx[k1,N1]
        if dx1 > 0:
            correct = False
            print('Incorrect dx!', k1, N1)
        x1 = x[k1,N1+1] + delta*del_x[k1,N1+1]
        k2 = find(klist == v2)
        dx2 = dx[k2,N1]
        if dx2 > 0:
            correct = False
            print('Incorrect dx!', k2, N1)
        x2 = x[k2,N1+1] + delta*del_x[k2,N1+1]
        return (x1/dx1)/(x2/dx2), correct
    elif v1 < 0 and v2 < 0:
        j1 = find(jlist == -v1)
        dq1 = dq[j1,N2]
        if dq1 > 0:
            correct = False
            print('Incorrect dq!', j1, N2)
        q1 = q[j1,N2] + delta*del_q[j1,N2]
        j2 = find(jlist == -v2)
        dq2 = dq[j2,N2]
        if dq2 > 0:
            correct = False
            print('Incorrect dq!', j2, N2)
        q2 = q[j2,N2] + delta*del_q[j2,N2]
        return (q2/dq2)/(q1/dq1), correct
    elif v1 > 0 and v2 < 0:
        k1 = find(klist == v1)
        dx1 = dx[k1,N1]
        if dx1 > 0:
            correct = False
            print('Incorrect dx!', k1, N1)
        x1 = x[k1,N1+1] + delta*del_x[k1,N1+1]
        j2 = find(jlist == -v2)
        dq2 = dq[j2,N2]
        if dq2 > 0:
            correct = False
            print('Incorrect dq!', j2, N2)
        q2 = q[j2,N2] + delta*del_q[j2,N2]
        t_interval = np.sum(tau[N1+1:N2]) + delta*np.sum(dtau[N1+1:N2])
        return -(x1/dx1 + q2/dq2)/t_interval, correct
    elif v1 < 0 and v2 > 0:
        j1 = find(jlist == -v1)
        dq1 = dq[j1,N2]
        if dq1 > 0:
            correct =False
            print('Incorrect dq!', j1, N2)
        q1 = q[j1,N2] + delta*del_q[j1,N2]
        k2 = find(klist == v2)
        dx2 = dx[k2,N1]
        if dx2 > 0:
            correct = False
            print('Incorrect dx!', k2, N1)
        x2 = x[k2,N1+1] + delta*del_x[k2,N1+1]
        t_interval = np.sum(tau[N1+1:N2]) + delta*np.sum(dtau[N1+1:N2])
        return -t_interval/(q1/dq1 + x2/dx2), correct
