from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
from doe.results_producer import combine_results, write_results_to_csv
import os
from SCLP import SCLP_settings


solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False)
pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
DATADIRd = pu.get_CPLEX_data_path()
for I in [200,400,800]:
    for T in [100,10000]:
        settings = {'alpha_rate':  1, 'cost_scale':1, 'a_rate' : 0.05, 'sum_rate':0.95, 'nz': 0.5,
                    'gamma_rate':0, 'c_scale': 0, 'h_rate': 0.1}
        if I < 100:
            results, ftrials, files, raw_tau = run_experiment_series('MCQN', 10, I * 10, I, T, settings, 1000,
                                                                     solver_settings, True, False)

            cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                'doe/cplex_integration/mod_files/main1.mod'), files)
            results = combine_results(results, cplex_results, 1)
            cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main10.mod'), files)
            results = combine_results(results, cplex_results, 10)
            cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main100.mod'), files)
            results = combine_results(results, cplex_results, 100)
            if I < 80:
                cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                    'doe/cplex_integration/mod_files/main1000.mod'), files)
                results = combine_results(results, cplex_results, 1000)
            res_file = relative_to_project('results_long2.csv')
            write_results_to_csv(results, res_file)
        else:
            if I == 200:
                results, ftrials, files, raw_tau = run_experiment_series('MCQN', 2, I * 10, I, T,
                                                                         settings, 1006,
                                                                         solver_settings, True, False)

                cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                    'doe/cplex_integration/mod_files/main1.mod'), files)
                results = combine_results(results, cplex_results, 1)
                cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                    'doe/cplex_integration/mod_files/main10.mod'), files)
                results = combine_results(results, cplex_results, 10)
                if I < 800:
                    cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                        'doe/cplex_integration/mod_files/main100.mod'), files)
                    results = combine_results(results, cplex_results, 100)
                res_file = relative_to_project('results_long.csv')
                write_results_to_csv(results, res_file)
            if I > 200:
                results, ftrials, files, raw_tau = run_experiment_series('MCQN', 1, I * 10, I, T,
                                                                         settings, 1000,
                                                                         solver_settings, True, False)

                cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                    'doe/cplex_integration/mod_files/main1.mod'), files)
                results = combine_results(results, cplex_results, 1)
                cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                    'doe/cplex_integration/mod_files/main10.mod'), files)
                results = combine_results(results, cplex_results, 10)
                if I < 800:
                    cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
                        'doe/cplex_integration/mod_files/main100.mod'), files)
                    results = combine_results(results, cplex_results, 100)
                res_file = relative_to_project('results_long.csv')
                write_results_to_csv(results, res_file)
