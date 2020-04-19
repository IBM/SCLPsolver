import numpy as np
from .vector_list import vector_list
from .state_tools import get_right_loc_min, get_loc_min, get_prim_loc_mins, get_dual_loc_mins
from .state_tools import get_right_loc_min1, get_loc_min1, get_prim_loc_mins1, get_dual_loc_mins1


class loc_min_storage():

    def __init__(self, dx, dq):
        x_row_idx = np.zeros(dx.shape[0], dtype=np.int32, order="C")
        q_row_idx = np.zeros(dq.shape[0], dtype=np.int32, order="C")
        self.dx_min = vector_list(get_right_loc_min1(dx[:, 0], x_row_idx), x_row_idx)
        self.dq_min = vector_list(get_right_loc_min1(dq[:, 0], q_row_idx), q_row_idx)
        #self.dx_min = vector_list(get_right_loc_min(dx[:, 0]))
        #self.dq_min = vector_list(get_right_loc_min(dq[:, 0]))

    def update_caseI(self, N1, N2, dx, dq):
        if N1 == -1:
            self.dx_min.delete(0, N2)
            self.dq_min.delete(0, N2 + 1)
            #self.dq_min.insert(0, get_right_loc_min(dq[:, 0]))
            self.dq_min.insert(0, get_right_loc_min1(dq[:, 0], self.dq_min.row_idx))
        elif N2 is None:
            self.dx_min.delete(N1, len(self.dx_min.data))
            self.dq_min.delete(N1+1, len(self.dq_min.data))
            #self.dx_min.insert(N1, get_right_loc_min(dx[:,-1]))
            self.dx_min.insert(N1, get_right_loc_min1(dx[:, -1], self.dx_min.row_idx))
        else:
            self.dx_min.delete(N1, N2)
            self.dq_min.delete(N1+1, N2+1)
            # self.dx_min.insert(N1, get_loc_min(dx[:, N1], dx[:, N1+1]))
            # self.dq_min.insert(N1+1, get_loc_min(dq[:, N1+1], dq[:, N1]))
            self.dx_min.insert(N1, get_loc_min1(dx[:, N1], dx[:, N1+1], self.dx_min.row_idx))
            self.dq_min.insert(N1+1, get_loc_min1(dq[:, N1+1], dq[:, N1], self.dq_min.row_idx))
        # if dx.shape[1] != len(self.dx_min.data):
        #     raise Exception('update1')

    #'#@profile
    def update_caseII(self, N1, N2, Nnew, dx, dq):
        if N1 == -1:
            self.dx_min.delete(0, N2)
            self.dq_min.delete(0, N2 + 1)
            #ds, lens = get_prim_loc_mins(dx[:,:Nnew+1])
            ds, lens = get_prim_loc_mins1(dx[:, :Nnew + 1], self.dx_min.row_idx)
            for i, l in enumerate(lens):
                self.dx_min.insert(i, ds[:l,i])
            #ds, lens = get_dual_loc_mins(dq[:, :Nnew+1])
            ds, lens = get_dual_loc_mins1(dq[:, :Nnew + 1], self.dq_min.row_idx)
            for i, l in enumerate(lens):
                self.dq_min.insert(i, ds[:l,i])
            #self.dq_min.insert(0, get_right_loc_min(dq[:, 0]))
            self.dq_min.insert(0, get_right_loc_min1(dq[:, 0], self.dq_min.row_idx))
        elif N2 is None:
            self.dx_min.delete(N1, len(self.dx_min.data))
            self.dq_min.delete(N1+1, len(self.dq_min.data))
            #self.dx_min.insert(N1, get_right_loc_min(dx[:,-1]))
            #ds, lens = get_prim_loc_mins(dx[:,-Nnew-1:])
            self.dx_min.insert(N1, get_right_loc_min1(dx[:, -1], self.dx_min.row_idx))
            ds, lens = get_prim_loc_mins1(dx[:, -Nnew - 1:], self.dx_min.row_idx)
            for i, l in enumerate(lens):
                self.dx_min.insert(N1 + i, ds[:l,i])
            #ds, lens = get_dual_loc_mins(dq[:,-Nnew-1:])
            ds, lens = get_dual_loc_mins1(dq[:, -Nnew - 1:], self.dq_min.row_idx)
            for i, l in enumerate(lens):
                self.dq_min.insert(N1 + i + 1, ds[:l,i])
        else:
            self.dx_min.delete(N1, N2)
            self.dq_min.delete(N1 +1, N2+1)
            #ds, lens = get_prim_loc_mins(dx[:,N1:N1+Nnew+2])
            ds, lens = get_prim_loc_mins1(dx[:, N1:N1 + Nnew + 2], self.dx_min.row_idx)
            for i, l in enumerate(lens):
                self.dx_min.insert(N1 + i, ds[:l,i])
            #ds, lens = get_dual_loc_mins(dq[:,N1:N1+Nnew+2])
            ds, lens = get_dual_loc_mins1(dq[:, N1:N1 + Nnew + 2], self.dq_min.row_idx)
            for i, l in enumerate(lens):
                self.dq_min.insert(N1 + i + 1, ds[:l,i])
        # if dx.shape[1] != len(self.dx_min.data):
        #     raise Exception('update2')

    def update_primal(self, N1, N2, dv):
        if N1 ==-1:
            self.dx_min.delete(0, N2)
            if dv is not None:
                ds, lens = get_prim_loc_mins(dv)
                for i,l in enumerate(lens):
                    self.dx_min.insert(i, ds[:l])
        elif N2 is None:
            self.dx_min.delete(N1, len(self.dx_min.data))
            self.dx_min.insert(N1, get_right_loc_min(dv[:,-1]))
            if dv.shape[1] > 1:
                ds, lens = get_prim_loc_mins(dv[:,:-1])
                for i,l in enumerate(lens):
                    self.dx_min.insert(N1+i, ds[:l])
        else:
            self.dx_min.delete(N1, N2)
            ds, lens = get_prim_loc_mins(dv)
            for i, l in enumerate(lens):
                self.dx_min.insert(N1 + i, ds[:l])

    def update_dual(self, N1, N2, dv):
        if N1 == -1:
            self.dq_min.delete(0, N2 + 1)
            self.dq_min.insert(0, get_right_loc_min(dv[:,-1]))
            if dv.shape[1] > 1:
                ds, lens = get_dual_loc_mins(dv[:, :-1])
                for i, l in enumerate(lens):
                    self.dq_min.insert(i+1, ds[:l])
        elif N2 is None:
            self.dq_min.delete(N1, len(self.dq_min.data))
            if dv is not None:
                ds, lens = get_dual_loc_mins(dv)
                for i, l in enumerate(lens):
                    self.dq_min.insert(N1+i, ds[:l])
        else:
            self.dq_min.delete(N1, N2)
            ds, lens = get_dual_loc_mins(dv)
            for i, l in enumerate(lens):
                self.dq_min.insert(N1 + i, ds[:l])