# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from doe.doe_utils import path_utils


pu = path_utils(os.path.expanduser('~/Box/SCLP comparison/data'))
exp_path = pu.get_experiment_path('MCQN',K=100,I=200,seed=300)
print(exp_path)
x= {'K':100,'I':200,'seed':300}
exp_path = pu.get_experiment_path('MCQN',**x)
print(exp_path)