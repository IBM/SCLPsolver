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

# --------------------------------------------------------------------------
# Source file provided under Apache License, Version 2.0, January 2004,
# http://www.apache.org/licenses/
# (c) Copyright IBM Corp. 2018
# --------------------------------------------------------------------------

"""
Shows how to do optimization workflows by running several models.
"""
from doopl.factory import *

import os
from os.path import dirname, abspath, join

DATADIR = join(dirname(abspath(__file__)), 'data')
mod = join(DATADIR, "mulprod.mod")
dat = join(DATADIR, "mulprod.dat")

status = 127
capFlour = 20
best = .0
curr = float("inf")


Capacity = pd.DataFrame({'name' : ['flour', 'eggs'], 'value' : [20, 40]})

while (best != curr):
    best = curr
    with create_opl_model(model=mod, data=dat) as opl:
        opl.set_input("Capacity", Capacity)
        print("Solve with capFlour = " + str(capFlour))
        if opl.run():
            curr = opl.objective_value
            print("OBJECTIVE: " + str(curr))
        else:
            print("No solution!")
        capFlour += 1
Capacity.update(pd.DataFrame({'value' : [capFlour]}))