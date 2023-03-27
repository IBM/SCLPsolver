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

class in_out_pivot():

    __slots__ =['in_', 'out_']

    def __init__(self):
        self.in_ = set()
        self.out_ = set()

    def pivot(self, in_, out_):
        """Normalizes the in_ and out_ according the active pivot.

        Parameters
        ----------
        in_: int
            name of incoming variable for the basis.
        out_: int
            name of the outgoing variable for the basis.
        """
        if in_ in self.out_:
            self.out_.remove(in_)
        else:
            self.in_.add(in_)
        if out_ in self.in_:
            self.in_.remove(out_)
        else:
            self.out_.add(out_)

    def extr(self, set_out_, set_in_):
        """Update the internal in_ and out_ members with names of variables that changed.

        :param set_out_: set
            Set containing the names of the variables that left the basis
        :param set_in_: set
            Set containing the names of the variables that entered the basis
        """
        for p in self.out_:
            if p in set_in_:
                set_in_.remove(p)
            else:
                set_out_.add(p)
        for p in self.in_:
            if p in set_out_:
                set_out_.remove(p)
            else:
                set_in_.add(p)
        self.in_ = set_out_
        self.out_ = set_in_