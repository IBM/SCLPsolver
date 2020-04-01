import numpy as np
from subroutines.state_tools.loc_min_storage import loc_min_storage


dx = np.random.rand(10,20) - 0.5
dq = np.random.rand(20,20) - 0.5
ins_dx = np.random.rand(10,5) - 0.5
ins_dq = np.random.rand(20,5) - 0.5

def old(dx, dq):
    sdx = np.ones((dx.shape[0], dx.shape[1] + 2))
    sdq = np.ones((dq.shape[0], dq.shape[1] + 2))
    np.sign(dx, out=sdx[:, 1:-1])
    np.sign(dq, out=sdq[:, 1:-1])
    dx_locmin_state = np.logical_and((sdx == 1)[:, 1:], (sdx == -1)[:, :-1])
    dq_locmin_state = np.logical_and((sdq == 1)[:, :-1], (sdq == -1)[:, 1:])
    return dx_locmin_state[:,1:], dq_locmin_state[:, :-1]


def compare(dx_loc, dq_loc, loc_st):
    if loc_st.dx_min.total_size != np.sum(dx_loc):
        return False
    if loc_st.dq_min.total_size != np.sum(dq_loc):
        return False
    dx_rc = np.where(dx_loc.T)
    old_r = -1
    j = 0
    for i, r in enumerate(dx_rc[0]):
        if old_r != r:
            old_r = r
            j = 0
        if loc_st.dx_min.data[r][j] != dx_rc[1][i]:
            return False
        j +=1
    dq_rc = np.where(dq_loc.T)
    old_r = -1
    j = 0
    for i, r in enumerate(dq_rc[0]):
        if old_r != r:
            old_r = r
            j = 0
        if loc_st.dq_min.data[r][j] != dq_rc[1][i]:
            return False
        j +=1
    return True


a = loc_min_storage(dx[:,1:2],dq[:,1:2])
a.update_caseII(-1,0,1,dx, dq)
dx_loc, dq_loc = old(dx[:,0:2], dq[:,0:2])
print(compare(dx_loc, dq_loc, a))
a.update_caseII(1,None,10, dx[:,:12], dq[:,:12])
dx_loc, dq_loc = old(dx[:,:12], dq[:,:12])
print(compare(dx_loc, dq_loc, a))
ddx = np.hstack((dx[:,:6],ins_dx[:, 0:3],dx[:,6:12]))
ddq = np.hstack((dq[:,:6],ins_dq[:, 0:3],dq[:,6:12]))
a.update_caseII(5,6,3,ddx, ddq)
dx_loc, dq_loc = old(ddx, ddq)
print(compare(dx_loc, dq_loc, a))
a.update_caseI(-1,2,ddx[:,2:],ddq[:,2:])
dx_loc, dq_loc = old(ddx[:,2:], ddq[:,2:])
print(compare(dx_loc, dq_loc, a))
a.update_caseI(10,None,ddx[:,2:-2],ddq[:,2:-2])
dx_loc, dq_loc = old(ddx[:,2:-2], ddq[:,2:-2])
print(compare(dx_loc, dq_loc, a))
ddx = np.hstack((ddx[:,2:6],ddx[:,7:-2]))
ddq = np.hstack((ddq[:,2:6],ddq[:,7:-2]))
a.update_caseI(3,5,ddx,ddq)
dx_loc, dq_loc = old(ddx, ddq)
print(compare(dx_loc, dq_loc, a))