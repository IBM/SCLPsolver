import time
from doopl.factory import *

from os import listdir
from os.path import join, isfile, split
import csv

def run_cplex_experiments(data_dir, mod_file, res_file, files = None):
    if files is None:
        files = [join(data_dir, f) for f in listdir(data_dir) if isfile(join(data_dir, f))]
    with open(res_file, 'a') as csvfile:
        reswriter = csv.writer(res_file)
        for dat_file in files:
            with create_opl_model(model=mod_file, data=dat_file) as opl:
                start_time = time.time()
                if opl.run():
                    obj = opl.objective_value
                    time_to_solve = time.time() - start_time
                    path, filename = split(dat_file)
                    reswriter.writerow([filename,obj,time_to_solve])
                    print("ExpName: " + filename + " OBJECTIVE: " + str(obj) + " Time: " + str(time_to_solve))
                else:
                    print("No solution!")
        csvfile.close()