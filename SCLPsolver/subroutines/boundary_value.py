import numpy as np


class boundary_value():
    __slots__ = ['v', 'delta_v']

    def __init__(self, v, delta_v=None):
        self.v = v
        self.delta_v = delta_v

    def get_delta(self):
        if self.delta_v is not None:
            rz = np.divide(-self.delta_v, self.v, where=self.v > 0, out=np.zeros_like(self.v))
            zz_ind = np.argmax(rz)
            zz = rz[zz_ind]
        else:
            zz = 0
            zz_ind = None
        return 1.0/zz, zz_ind