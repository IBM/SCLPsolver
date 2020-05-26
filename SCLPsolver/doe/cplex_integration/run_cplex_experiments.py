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