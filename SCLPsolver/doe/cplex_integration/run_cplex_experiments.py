import time
from doopl.factory import *

from os import listdir
from os.path import join, isfile, split

def run_cplex_experiments(data_dir, mod_file, files = None):
    results = []
    if files is None:
        files = [join(data_dir, f) for f in listdir(data_dir) if isfile(join(data_dir, f))]
    #reswriter = csv.writer(csvfile)
    for dat_file in files:
        with create_opl_model(model=mod_file, data=dat_file) as opl:
            start_time = time.time()
            if opl.run():
                obj = opl.objective_value
                time_to_solve = time.time() - start_time
                path, filename = split(dat_file)
                #reswriter.writerow([filename, obj, time_to_solve])
                results.append({'file': filename, 'objective': obj, 'time': time_to_solve})
                print("ExpName: " + filename + " OBJECTIVE: " + str(obj) + " Time: " + str(time_to_solve))
            else:
                print("No solution!")
    return results