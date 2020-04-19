

class vector_list():

    def __init__(self, vec=None, row_idx = None):
        if vec is None:
            self.data = []
            self.sizes = []
            self.total_size = 0
            self.row_idx = None
        else:
            self.data = [vec]
            self.sizes = [vec.size]
            self.total_size = vec.size
            self.row_idx = row_idx

    def insert(self, pos, vec):
        self.data.insert(pos, vec)
        self.sizes.insert(pos, vec.size)
        self.total_size += vec.size

    def delete(self, pos_from, pos_to):
        for i in range(pos_from, pos_to):
            del self.data[pos_from]
            self.total_size -= self.sizes.pop(pos_from)
