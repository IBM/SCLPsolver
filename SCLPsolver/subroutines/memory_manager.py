import psutil
import math


class memory_manager():

    def __init__(self, K, J):
        self.matrix_size = K * J * 8

    def get_max_bases_num(self):
        mem = psutil.virtual_memory()
        return math.floor(mem.free/self.matrix_size - 5)


