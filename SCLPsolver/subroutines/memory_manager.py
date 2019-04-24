import psutil
import math


class memory_manager():

    def __init__(self, K, J, I=0):
        self.matrix_size = (K+I) * J * 8
        mem = psutil.virtual_memory()
        self.max_bs = math.floor(mem.free / self.matrix_size - 5)

    def num_bases_to_remove(self):
        mem = psutil.virtual_memory()
        bs = math.floor(mem.free/self.matrix_size - 5)
        return -bs if bs < 0 else 0


