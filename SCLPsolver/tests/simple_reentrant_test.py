from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
from doe.results_producer import combine_results, write_results_to_csv
import os
import numpy as np
from SCLP import SCLP_settings


solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False, suppress_printing=True)
#pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
pu = path_utils("C:/DataD/SCLP_data")
DATADIRd = pu.get_CPLEX_data_path()
for I in [40]:
    results, ftrials, files, raw_tau = run_experiment_series('simple_reentrant', 10, I * 20, I, None, {"c_scale": 0, "cost_scale": 10, "alpha_rate1": 0.8, "alpha_rate2": 0.45}, 1000,
                                                             solver_settings, True, False)

    cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main1xobj.mod'), files)
    results = combine_results(results, cplex_results, 1, xobj=True)
    cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main10xobj.mod'), files)
    results = combine_results(results, cplex_results, 10, xobj=True)
    cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main100xobj.mod'), files)
    results = combine_results(results, cplex_results, 100, xobj=True)
    if I < 80:
        cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
            'doe/cplex_integration/mod_files/main1000xobj.mod'), files)
        results = combine_results(results, cplex_results, 1000, xobj=True)
    res_file = relative_to_project('results_reentrant_new2.csv')
    write_results_to_csv(results, res_file)
