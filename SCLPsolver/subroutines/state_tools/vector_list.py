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



class vector_list():

    def __init__(self, vec=None):
        if vec is None:
            self.data = []
            self.sizes = []
            self.total_size = 0
        else:
            self.data = [vec]
            self.sizes = [vec.size]
            self.total_size = vec.size

    def insert(self, pos, vec):
        self.data.insert(pos, vec)
        self.sizes.insert(pos, vec.size)
        self.total_size += vec.size

    def delete(self, pos_from, pos_to):
        for i in range(pos_from, pos_to):
            del self.data[pos_from]
            self.total_size -= self.sizes.pop(pos_from)
