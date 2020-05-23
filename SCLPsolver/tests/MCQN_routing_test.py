from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.results_producer import combine_results, write_results_to_csv
from doe.doe_utils import path_utils
from SCLP import SCLP_settings

I = 40
K = I * 10
J = K * 2
seed = 1000

settings = {'J':J, 'alpha_rate':  10, 'cost_scale':2, 'a_rate' : 0.1, 'sum_rate':0.8, 'nz': 0.5,
                    'gamma_rate':0, 'c_scale': 0, 'h_rate': 4}

solver_settings = SCLP_settings(find_alt_line=False, check_intermediate_solution=False, suppress_printing=True, memory_management=False)
#pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
pu = path_utils("C:/DataD/SCLP_data")
DATADIRd = pu.get_CPLEX_data_path()

results, ftrials, files, raw_tau = run_experiment_series('MCQN_routing', 1, K, I, 200, settings, 1000,
                                                         solver_settings, True, False)

cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main1xobj.mod'), files)
results = combine_results(results, cplex_results, 1, xobj=True)
cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main10xobj.mod'), files)
results = combine_results(results, cplex_results, 10, xobj=True)
cplex_results = run_cplex_experiments(DATADIRd, relative_to_project('doe/cplex_integration/mod_files/main100xobj.mod'), files)
results = combine_results(results, cplex_results, 100, xobj=True)
# if I < 60:
#     cplex_results = run_cplex_experiments(DATADIRd, relative_to_project(
#         'doe/cplex_integration/mod_files/main1000xobj.mod'), files)
#     results = combine_results(results, cplex_results, 1000, xobj=True)
res_file = relative_to_project('results_10.csv')
write_results_to_csv(results, res_file)
