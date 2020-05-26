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



class bs_test():

    def __init__(self, bases, places):
        self._bases = bases
        self._places =  places

    def clear(self, numBasesToRemove):
        NN = 100
        basesActive = len(self._places)
        if (numBasesToRemove > 0):
            orderedSequence = sorted(self._places)
            order = sorted(range(len(self._places)), key=lambda i: self._places[i])
            diffSeq = [orderedSequence[1]] + [orderedSequence[i + 2] - p for i, p in
                                              enumerate(orderedSequence[:-2])] + [NN - orderedSequence[-2]]
            if 2 * numBasesToRemove < basesActive:
                candidates = sorted(range(len(diffSeq)), key=lambda i: diffSeq[i])[:2 * numBasesToRemove + 1]
                to_remove = [candidates[0]]
                for i in range(1, len(candidates)):
                    if candidates[i] - candidates[i - 1] > 1 or candidates[i - 1] not in to_remove:
                        to_remove.append(candidates[i])
                    if len(to_remove) >= numBasesToRemove:
                        break
                self._bases = [self._bases[p] for i,p in enumerate(order) if i not in to_remove]
                self._places = [self._places[p] for i,p in enumerate(order) if i not in to_remove]
        print(self._places, self._bases)

    @property
    def bases(self):
        return self._bases

    @property
    def places(self):
        return self._places

import numpy as np
nums = np.random.choice(100, 10, replace=False)
places = [x for x in nums]
bases = [[x] for x in nums]
print(bases, places)
tt = bs_test(bases, places)
tt.clear(2)
