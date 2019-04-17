


import time
from doopl.factory import *

import os
from os import listdir
from os.path import dirname, abspath, join, isfile

DATADIRm = join(dirname(abspath(__file__)), 'mod_files')
mod = join(DATADIRm, "main.mod")

DATADIRd = join(dirname(abspath(__file__)), 'data')

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