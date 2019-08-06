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
for I in [10,20,40,80,100,200,400,800]:
    for T in [100,1000,10000]:
        for alpha_rate in [10,5,1,0.5,0.1]:
            for a_rate in [0.1,0.05,0.01,0.005,0.001]:
                for h_rate in [0.6,0.3,0.06,0.03,0.006]:
                    for nz in [0.4,0.5,0.6]:
                        for sum_rate in [0.9,0.95,0.99]:
                            settings = {'alpha_rate':  alpha_rate, 'cost_scale':1, 'a_rate' : a_rate, 'sum_rate':sum_rate, 'nz': nz,
                                        'gamma_rate':0, 'c_scale': 0, 'h_rate': h_rate}
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
                                res_file = relative_to_project('results_long.csv')
                                write_results_to_csv(results, res_file)
                            else:
                                for n in [0,2,4,8]:
                                    results, ftrials, files, raw_tau = run_experiment_series('MCQN', 2, I * 10, I, T,
                                                                                             settings, 1000+n,
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