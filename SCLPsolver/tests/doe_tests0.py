from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
from doe.results_producer import combine_results, write_results_to_csv
import os

results, ftrials, files, raw_tau = run_experiment_series('MCQN', 10, 1000, 100, 2000, {'alpha_rate':  4000},starting_seed =1000 )
pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
DATADIRd = pu.get_CPLEX_data_path()
cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main10.mod'), files)
results = combine_results(results, cplex_results, 10)
cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/dual10.mod'), files)
results = combine_results(results, cplex_results, 10, True)
# cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main100.mod'), files)
# results = combine_results(results, cplex_results, 100)
res_file = relative_to_project('results_test.csv')
write_results_to_csv(results, res_file, True, raw_tau=None)