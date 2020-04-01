from .vector_list import vector_list
from .state_tools import get_right_loc_min, get_loc_min, get_prim_loc_mins, get_dual_loc_mins


class loc_min_storage():

    def __init__(self, dx, dq):
        self.dx_min = vector_list(get_right_loc_min(dx[:, 0]))
        self.dq_min = vector_list(get_right_loc_min(dq[:, 0]))

    def update_caseI(self, N1, N2, dx, dq):
        if N1 == -1:
            self.dx_min.delete(0, N2)
            self.dq_min.delete(0, N2 + 1)
            self.dq_min.insert(0, get_right_loc_min(dq[:, 0]))
        elif N2 is None:
            self.dx_min.delete(N1, len(self.dx_min.data))
            self.dq_min.delete(N1+1, len(self.dq_min.data))
            self.dx_min.insert(N1, get_right_loc_min(dx[:,-1]))
        else:
            self.dx_min.delete(N1, N2)
            self.dq_min.delete(N1+1, N2+1)
            self.dx_min.insert(N1, get_loc_min(dx[:, N1], dx[:, N1+1]))
            self.dq_min.insert(N1+1, get_loc_min(dq[:, N1+1], dq[:, N1]))

    def update_caseII(self, N1, N2, Nnew, dx, dq):
        if N1 == -1:
            self.dx_min.delete(0, N2)
            self.dq_min.delete(0, N2 + 1)
            ds, lens = get_prim_loc_mins(dx[:,:Nnew+1])
            for i, l in enumerate(lens):
                self.dx_min.insert(i, ds[:l,i])
            ds, lens = get_dual_loc_mins(dq[:, :Nnew+1])
            for i, l in enumerate(lens):
                self.dq_min.insert(i, ds[:l,i])
            self.dq_min.insert(0, get_right_loc_min(dq[:, 0]))
        elif N2 is None:
            self.dx_min.delete(N1, len(self.dx_min.data))
            self.dq_min.delete(N1+1, len(self.dq_min.data))
            self.dx_min.insert(N1, get_right_loc_min(dx[:,-1]))
            ds, lens = get_prim_loc_mins(dx[:,-Nnew-1:])
            for i, l in enumerate(lens):
                self.dx_min.insert(N1 + i, ds[:l,i])
            ds, lens = get_dual_loc_mins(dq[:,-Nnew-1:])
            for i, l in enumerate(lens):
                self.dq_min.insert(N1 + i + 1, ds[:l,i])
        else:
            self.dx_min.delete(N1, N2)
            self.dq_min.delete(N1 +1, N2+1)
            ds, lens = get_prim_loc_mins(dx[:,N1:N1+Nnew+2])
            for i, l in enumerate(lens):
                self.dx_min.insert(N1 + i, ds[:l,i])
            ds, lens = get_dual_loc_mins(dq[:,N1:N1+Nnew+2])
            for i, l in enumerate(lens):
                self.dq_min.insert(N1 + i + 1, ds[:l,i])

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