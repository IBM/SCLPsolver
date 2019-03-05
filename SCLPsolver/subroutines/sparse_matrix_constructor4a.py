import numpy as np
from scipy.sparse import csc_matrix


class sparse_matrix_constructor():

    def __init__(self, data, indexes, row_num, indptr=None, copy=False):
        if data is None:
            self._data = []
            self._indexes = []
            self._indptr = [0]
        else:
            if copy:
                self._data = data.copy()
                self._indexes = indexes.copy()
                self._indptr = indptr.copy()
            else:
                self._data = [data]
                self._indexes = [indexes]
                self._indptr = [0, len(indexes)-1]
        self._row_num = row_num

    @property
    def data(self):
        return self._data

    @property
    def indexes(self):
        return self._indexes

    @property
    def row_num(self):
        return self._row_num

    @property
    def indptr(self):
        return self._indptr

    ###@profile
    def insert(self, after, data, indexes, indptr = None):
        if after == -1:
            self._data = data + self._data
            self._indexes = indexes + self._indexes
            if indptr is None:
                idx = map(len, indexes)
                sidx = sum(idx) -1
                self._indptr = [0]+[i-1 for i in idx][:-1]+[i+ sidx for i in self._indptr]
            else:
                sx = indptr[-1]
                self._indptr = indptr + [x + sx for x in self._indptr[1:]]
        elif after >= len(self._data) -1:
            self._data = self._data + data
            self._indexes = self._indexes + indexes
            if indptr is None:
                idx = map(lambda x: len(x)+self._indptr[-1], indexes)
                self._indptr += idx
            else:
                sx = self._indptr[-1]
                self._indptr += [x + sx for x in indptr[1:]]
        else:
            self._data = self._data[:after + 1] + data + self._data[after + 1:]
            self._indexes = self._indexes[:after + 1] + indexes + self._indexes[after + 1:]
            if indptr is None:
                idx = map(lambda x: len(x) + self._indptr[after], indexes)
                sidx = sum(map(len, indexes)) - 1
                self._indptr = self._indptr[:after + 1] + idx + [i+ sidx for i in self._indptr[after + 1:]]
            else:
                sx = self._indptr[after + 1]
                sxx = indptr[-1]
                self._indptr = self._indptr[:after + 1]+[x + sx for x in indptr] + [i+ sxx for i in self._indptr[after + 1:]]

    ###@profile
    def remove(self, from_, to_):
        if from_ <= 0:
            self._data = self._data[to_:]
            self._indexes = self._indexes[to_:]
            sx = self._indptr[to_]
            self._indptr = [x - sx for x in self._indptr[to_:]]
        elif to_ >= len(self._data):
            self._data = self._data[:from_]
            self._indexes = self._indexes[:from_]
            self._indptr = self._indptr[:from_+1]
        else:
            self._data = self._data[:from_] + self._data[to_:]
            self._indexes = self._indexes[:from_] + self._indexes[to_:]
            sx =  self._indptr[from_ +1] - self._indexes[to_-1]
            self._indptr = self._indptr[:from_ + 1] + [x - sx for x in self._indptr[to_:]]

    ###@profile
    def replace(self, from_, to_, data, indexes, indptr = None):
        if from_ <= 0:
            self._data = data + self._data[to_:]
            self._indexes = indexes + self._indexes[to_:]
            if indptr is None:
                idx = map(len, indexes)
                sidx = sum(idx) - 1 - self._indptr[to_]
                self._indptr = [0] + [i - 1 for i in idx] + [i + sidx for i in self._indptr[to_+1:]]
            else:
                sx = indptr[-1]
                self._indptr = indptr + [x + sx for x in self._indptr[to_+1:]]
        elif to_ >= len(self._data):
            self._data = self._data[:from_] + data
            self._indexes = self._indexes[:from_] + indexes
            if indptr is None:
                idx = map(lambda x: len(x) + self._indptr[-1], indexes)
                self._indptr = self._indptr[:from_ + 1] + idx
            else:
                sx = self._indptr[from_]
                self._indptr = self._indptr[:from_ + 1]+[x + sx for x in indptr[1:]]
        else:
            self._data = self._data[:from_] + data + self._data[to_:]
            self._indexes = self._indexes[:from_] + indexes + self._indexes[to_:]
            if indptr is None:
                idx = map(lambda x: len(x) + self._indptr[from_+1], indexes)
                sidx = sum(map(len, indexes)) - 1
                sx = self._indptr[from_ + 1] - self._indexes[to_ - 1]
                self._indptr = self._indptr[:from_ + 1] + idx + [x + sidx - sx for x in self._indptr[to_:]]
            else:
                sx = self._indptr[from_]
                sxx = indptr[-1]
                self._indptr = self._indptr[:from_ + 1]+[x + sx for x in indptr[1:]] + [i+ sxx for i in self._indptr[from_ + 1:]]

    ###@profile
    def get_sub_matrix(self, from_, to_):
        if from_ <= 0:
            return sparse_matrix_constructor(self._data[:to_], self._indexes[:to_], self._row_num, self._indptr[:to_+1], True)
        elif to_ >= len(self._data):
            return sparse_matrix_constructor(self._data[from_:], self._indexes[from_:], self._row_num, [x-self._indptr[from_] for x in self._indptr[from_:]], True)
        else:
            indptr = [x-self._indptr[from_] for x in self._indptr[from_:to_+1]]
            return sparse_matrix_constructor(self._data[from_:to_], self._indexes[from_:to_], self._row_num, indptr, True)

    ###@profile
    def insert_matrix(self, after, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
            self.insert(after, other.data, other.indexes, other.indptr)

    ###@profile
    def append(self, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
            self._data = self._data + other.data
            self._indexes = self._indexes + other.indexes
            sx = self._indptr[-1]
            self._indptr += [x+sx for x in other.indptr[1:]]

    ###@profile
    def prepend(self, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
            self._data = other.data + self._data
            self._indexes = other.indexes + self._indexes
            sx = other.indptr[-1]
            self._indptr = other.indptr + [x + sx for x in self._indptr[1:]]

    ###@profile
    def replace_matrix(self, from_, to_, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
        self.replace(from_, to_, other.data, other.indexes, other.indptr)

    ###@profile
    def get_csc_matrix(self):
        col_num = len(self._indexes)
        if col_num > 1:
            data = np.concatenate(self._data, axis=0)
            rows = np.concatenate(self._indexes, axis=0)
            return csc_matrix((data,rows,self._indptr),shape=(self._row_num,col_num))
        else:
            return csc_matrix((self._data[0], self._indexes[0], self._indptr), shape=(self._row_num, col_num))

    ###@profile
    def get_matrix(self):
        return self.get_csc_matrix().toarray()