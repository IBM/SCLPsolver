# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from scipy.sparse import coo_matrix


class sparse_matrix_constructor():

    def __init__(self, data, indexes, row_num, copy=False):
        if data is None:
            self._data = []
            self._indexes = []
        else:
            if copy:
                self._data = data.copy()
                self._indexes = indexes.copy()
            else:
                self._data = [data]
                self._indexes = [indexes]
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

    #'#@profile
    def insert(self, after, data, indexes):
        if after == -1:
            self._data = data + self._data
            self._indexes = indexes + self._indexes
        elif after >= len(self._data) -1:
            self._data = self._data + data
            self._indexes = self._indexes + indexes
        else:
            self._data = self._data[:after + 1] + data + self._data[after + 1:]
            self._indexes = self._indexes[:after + 1] + indexes + self._indexes[after + 1:]

    #'#@profile
    def remove(self, from_, to_):
        if from_ <= 0:
            self._data = self._data[to_:]
            self._indexes = self._indexes[to_:]
        elif to_ >= len(self._data)-1:
            self._data = self._data[:from_]
            self._indexes = self._indexes[:from_]
        else:
            self._data = self._data[:from_] + self._data[to_:]
            self._indexes = self._indexes[:from_] + self._indexes[to_:]

    #'#@profile
    def replace(self, from_, to_, data, indexes):
        if from_ <= 0:
            self._data = data + self._data[to_:]
            self._indexes = indexes + self._indexes[to_:]
        elif to_ >= len(self._data):
            self._data = self._data[:from_] + data
            self._indexes = self._indexes[:from_] + indexes
        else:
            self._data = self._data[:from_] + data + self._data[to_:]
            self._indexes = self._indexes[:from_] + indexes + self._indexes[to_:]

    #'#@profile
    def get_sub_matrix(self, from_, to_):
        if from_ <= 0:
            return sparse_matrix_constructor(self._data[:to_], self._indexes[:to_], self._row_num, True)
        elif to_ >= len(self._data):
            return sparse_matrix_constructor(self._data[from_:], self._indexes[from_:], self._row_num, True)
        else:
            return sparse_matrix_constructor(self._data[from_:to_], self._indexes[from_:to_], self._row_num, True)

    #'#@profile
    def insert_matrix(self, after, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
            self.insert(after, other.data, other.indexes)

    #'#@profile
    def append(self, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
            self._data = self._data + other.data
            self._indexes = self._indexes + other.indexes

    #'#@profile
    def prepend(self, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
            self._data = other.data + self._data
            self._indexes = other.indexes + self._indexes

    #'#@profile
    def replace_matrix(self, from_, to_, other):
        if isinstance(other, sparse_matrix_constructor):
            if other.row_num != self._row_num:
                raise ValueError('Row numbers must be equal!')
        self.replace(from_, to_, other.data, other.indexes)

    #'#@profile
    def get_coo_matrix(self):
        col_num = len(self._indexes)
        if col_num > 1:
            cols = np.concatenate([np.full_like(p,i) for i,p in enumerate(self._indexes)])
            data = np.concatenate(self._data, axis=0)
            rows = np.concatenate(self._indexes, axis=0)
            return coo_matrix((data,(rows,cols)),shape=(self._row_num,col_num))
        else:
            return coo_matrix((self._data[0], (self._indexes[0], np.zeros(len(self._indexes[0])))), shape=(self._row_num, col_num))

    #'#@profile
    def get_matrix(self):
        return self.get_coo_matrix().toarray()