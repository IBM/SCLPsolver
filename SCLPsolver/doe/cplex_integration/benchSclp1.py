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




import time
from doopl.factory import *

import os
from os import listdir
from os.path import dirname, abspath, join, isfile
#from doe.doe_utils import path_utils

DATADIRm = join(dirname(abspath(__file__)), 'mod_files')
mod = join(DATADIRm, "main.mod")

#pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
#DATADIRd = pu.get_CPLEX_data_path()
DATADIRd=os.path.expanduser('~/Box/SCLP comparison/data/CPLEX')

onlyfiles = [f for f in listdir(DATADIRd) if isfile(join(DATADIRd, f))]
print("Test: ", onlyfiles)


status = 127
curr = float("inf")


#Capacity = pd.DataFrame({'name' : ['flour', 'eggs'], 'value' : [20, 40]})
file = open("results.csv","w")
file.write("ExpName,OBJECTIVE,Time")
file.write('\n')
#print("ExpName","OBJECTIVE","Time", end='\n', file='results.csv')
#print(value, ..., sep=' ', end='\n', file=sys.stdout)
for i in onlyfiles:
    dat = join(DATADIRd, i)
    with create_opl_model(model=mod, data=dat) as opl:
        #opl.set_input("Capacity", Capacity)
        start_time = time.time()
        if opl.run():
            obj = opl.objective_value
            time_to_solve = time.time() - start_time
            print("ExpName: " + str(i) + " OBJECTIVE: " + str(obj) + " Time: " + str(time_to_solve))
            file.write(str(i))
            file.write(',')
            file.write(str(obj))
            file.write(',')
            file.write(str(time_to_solve))
            file.write('\n')
        else:
            print("No solution!")

file.close()