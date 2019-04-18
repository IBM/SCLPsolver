from doe.doe import run_experiment_series
from subroutines.utils import relative_to_project
from doe.cplex_integration.run_cplex_experiments import run_cplex_experiments
from doe.doe_utils import path_utils
import csv
import os

results, ftrials, files = run_experiment_series('MCQN', 1, 200, 20, 500, {'alpha_rate':  1000},starting_seed =1009 )