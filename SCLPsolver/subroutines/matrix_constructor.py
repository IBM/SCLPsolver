import numpy as np
import math


class matrix_constructor():

    def __init__(self, data, indexes, row_num, align = 0, col_num = None):
        if col_num is None:
            col_num = row_num
        self._matrix = np.zeros(shape=(row_num, col_num), order='C')
        self._align = align
        if self._align == 0:
            self._left = math.floor(row_num/2)
        elif self._align == -1:
            self._left = 0
        elif self._align == 1:
            self._left = col_num - 1
        else:
            raise Exception('Incorrect alignment!')
        if data is not None:
            self._matrix[indexes,self._left] = data
            self._right = self._left + 1
        else:
            if self._align == 1:
                self._left = col_num
                self._right = col_num
            else:
                self._right = self._left

    #'#@profile
    def remove(self, from_, to_):
        if from_ <= 0:
            self._left += to_
        elif to_ >= self._right - self._left:
            self._right -= to_ - from_
        else:
            if self._align == 0:
                if self._left > self._matrix.shape[1] - self._right:
                    self._matrix[:, self._left + from_:self._right + from_ - to_] = self._matrix[:, self._left + to_:self._right]
                    self._right -= to_ - from_
                else:
                    self._matrix[:, self._left - from_ + to_:self._left + to_] = self._matrix[:, self._left:self._left + from_]
                    self._left = self._left - from_ + to_
            elif self._align == -1:
                self._matrix[:, from_:self._right + from_ - to_] = self._matrix[:,to_:self._right]
                self._right -= to_ - from_
            elif self._align == 1:
                self._matrix[:, self._left - from_ + to_:self._left+ to_] = self._matrix[:,self._left:self._left + from_]
                self._left = self._left - from_ + to_

    #'#@profile
    def get_sub_matrix(self, from_, to_, copy=True):
        if from_ <= 0:
            ret = self._matrix[:, self._left:self._left +to_]
        elif to_ >= self._right - self._left:
            ret = self._matrix[:, self._left + from_:self._right]
        else:
            ret = self._matrix[:, self._left + from_:self._left + to_]
        if copy:
            return ret.copy()
        else:
            return ret

    def _increase_col_num(self, where = 0, min_num = None):
        col_num = max(math.floor(self._matrix.shape[1] / 2), min_num * 2)
        mat = np.zeros(shape=(self._matrix.shape[0], self._matrix.shape[1] + col_num), order='C')
        if self._align == -1:
            mat[:,:self._right] = self._matrix[:,:self._right]
        elif self._align == 1:
            new_left = mat.shape[1] -(self._right-self._left)
            mat[:,new_left:] = self._matrix[:,self._left:]
            self._right = mat.shape[1]
            self._left = new_left
        else:
            new_left = math.floor((mat.shape[1] - (self._right-self._left))/2)
            new_right = new_left + self._right - self._left
            mat[:, new_left:new_right] = self._matrix[:,self._left:self._right]
            self._right = new_right
            self._left = new_left
        self._matrix = mat

    #'#@profile
    def append(self, dtuple):
        if self._right == self._matrix.shape[1]:
            self._increase_col_num(1)
        self._matrix[dtuple[1],self._right] = dtuple[0]
        self._right +=1

    #'#@profile
    def prepend(self, dtuple):
        if self._left == 0:
            self._increase_col_num(-1)
        self._left -=1
        self._matrix[dtuple[1], self._left] = dtuple[0]

    #'#@profile
    def replace_matrix(self, from_, to_, matrix):
        col_num = matrix.shape[1]
        if from_ <= 0:
            self._left += to_
            if col_num > self._left:
                self._increase_col_num(-1, col_num)
            self._matrix[:, self._left - col_num:self._left] = matrix
            self._left -= col_num
        elif to_ >= self._right - self._left:
            self._right -= to_ - from_
            if col_num > self._matrix.shape[1] - self._right:
                self._increase_col_num(1, col_num)
            self._matrix[:, self._right:self._right + col_num] = matrix
            self._right += col_num
        else:
            nnew = from_ - to_ + col_num
            if self._align == 0:
                t = self._left > self._matrix.shape[1] - self._right
                if (t and nnew > 0) or (not t and nnew < 0):
                    if nnew > self._left:
                        self._increase_col_num(-1, nnew)
                    self._matrix[:, self._left - nnew:self._left + to_ - col_num] = self._matrix[:, self._left:self._left + from_]
                    self._matrix[:, self._left + to_ - col_num: self._left + to_] = matrix
                    self._left -= nnew
                else:
                    if nnew > self._matrix.shape[1] - self._right:
                        self._increase_col_num(1, nnew)
                    self._matrix[:, self._left + from_ + col_num: self._right + nnew] = self._matrix[:, self._left +to_: self._right]
                    self._matrix[:, self._left + from_: self._left + from_ + col_num] = matrix
                    self._right += nnew
            elif self._align == -1:
                if nnew > self._matrix.shape[1] - self._right:
                    self._increase_col_num(1, nnew)
                self._matrix[:, from_+ col_num : self._right + nnew] = self._matrix[:,to_: self._right]
                self._matrix[:, from_: from_ + col_num] = matrix
                self._right += nnew
            elif self._align == 1:
                if nnew > self._left:
                    self._increase_col_num(-1, nnew)
                self._matrix[:, self._left - nnew:self._left + to_- col_num] = self._matrix[:, self._left:self._left + from_]
                self._matrix[:, self._left + to_- col_num: self._left + to_] = matrix
                self._left -= nnew

    #'#@profile
    def replace(self, from_, to_, data, indexes):
        if from_ <= 0:
            self._left += to_
            if self._left == 0:
                self._increase_col_num(-1, 1)
            self._matrix[:, self._left - 1] = 0
            self._matrix[indexes, self._left - 1] = data
            self._left -= 1
        elif to_ >= self._right - self._left:
            self._right -= to_ - from_
            if self._right == self._matrix.shape[1]:
                self._increase_col_num(1, 1)
            self._matrix[:, self._right] = 0
            self._matrix[indexes, self._right] = data
            self._right += 1
        else:
            nnew = from_ - to_ + 1
            if self._align == 0:
                t = self._left > self._matrix.shape[1] - self._right
                if (t and nnew > 0) or (not t and nnew < 0):
                    if nnew > self._left:
                        self._increase_col_num(-1, nnew)
                    self._matrix[:, self._left - nnew:self._left + to_ - 1] = self._matrix[:, self._left:self._left + from_]
                    self._matrix[:, self._left + to_ - 1] = 0
                    self._matrix[indexes, self._left + to_ - 1] = data
                    self._left -= nnew
                else:
                    if nnew > self._matrix.shape[1] - self._right:
                        self._increase_col_num(1, nnew)
                    self._matrix[:, self._left + from_ + 1: self._right + nnew] = self._matrix[:, self._left +to_: self._right]
                    self._matrix[:, self._left + from_] = 0
                    self._matrix[indexes, self._left + from_] = data
                    self._right += nnew
            elif self._align == -1:
                if nnew > self._matrix.shape[1] - self._right:
                    self._increase_col_num(1, nnew)
                self._matrix[:, from_+ 1 : self._right + nnew] = self._matrix[:,to_: self._right]
                self._matrix[:, from_] = 0
                self._matrix[indexes, from_] = data
                self._right += nnew
            elif self._align == 1:
                if nnew > self._left:
                    self._increase_col_num(-1, nnew)
                self._matrix[:, self._left - nnew:self._left + to_- 1] = self._matrix[:, self._left:self._left + from_]
                self._matrix[:, self._left + to_ - 1] = 0
                self._matrix[indexes, self._left + to_- 1] = data
                self._left -= nnew

    #'#@profile
    def get_matrix(self):
        return self._matrix[:,self._left:self._right]

    def get_raw_matrix(self):
        return self._matrix, self._left, self._right

    def get_vector(self, pos):
        if self._left + pos >= self._right:
            return None
        else:
            return self._matrix[:,self._left + pos]