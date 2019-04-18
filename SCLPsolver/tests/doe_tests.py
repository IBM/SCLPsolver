from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
import csv
import os

results, ftrials, files = run_experiment_series('MCQN', 10, 2000, 200, 500, {'alpha_rate':  1000},starting_seed =1000 )

res_file= relative_to_project("python_results.csv")
if os.path.isfile(res_file):
    csvfile = open(res_file,"a")
    reswriter = csv.writer(csvfile)
else:
    csvfile = open(res_file, "w")
    reswriter = csv.writer(csvfile)
    reswriter.writerow(results[0].keys())
for res in results:
    reswriter.writerow(res.values())
csvfile.close()
res_file= relative_to_project("cplex_results.csv")
if os.path.isfile(res_file):
    csvfile = open(res_file,"a")
else:
    csvfile = open(res_file, "w")
    csvfile.write('ExpName,OBJECTIVE,Time\n')
csvfile.close()
pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
DATADIRd = pu.get_CPLEX_data_path()
run_cplex_experiments(DATADIRd, 'doe/cplex_integration/mod_files/main.mod', res_file, files)