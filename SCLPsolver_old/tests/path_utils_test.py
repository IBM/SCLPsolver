import os
from doe.doe_utils import path_utils


pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
exp_path = pu.get_experiment_path('MCQN',K=100,I=200,seed=300)
print(exp_path)
x= {'K':100,'I':200,'seed':300}
exp_path = pu.get_experiment_path('MCQN',**x)
print(exp_path)