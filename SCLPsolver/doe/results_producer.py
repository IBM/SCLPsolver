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
import csv


def combine_results(python_results, cplex_results, discr, dual=False, xobj=False):
    d = 'd' if dual else ''
    if xobj:
        prefix = 'cplex_x_'+d+str(discr)
    else:
        prefix = 'cplex_' + d + str(discr)
    for pres in python_results:
        for cres in cplex_results:
            if cres['file'] == pres['file']:
                if xobj:
                    pres[prefix+'_objective'] = pres['buffer_cost'] - cres['objective']
                    pres[prefix+ '_real_objective'] = cres['objective']
                else:
                    pres[prefix+'_objective'] = cres['objective']
                    pres[prefix + '_real_objective'] = pres['buffer_cost'] - cres['objective']
                pres[prefix+'_time'] = cres['time']
                if xobj:
                    optimality_gap = cres['objective'] - pres['real_objective']
                elif dual:
                    optimality_gap = cres['objective'] - pres['objective']
                else:
                    optimality_gap = pres['objective'] - cres['objective']
                pres[prefix + '_relative_objective'] = optimality_gap/abs(pres['objective'])
                pres[prefix + '_real_relative_objective'] = optimality_gap / abs(pres['real_objective'])
                pres[prefix + '_relative_time'] = cres['time'] / pres['time']
                if dual:
                    pres['cplex_' + str(discr) + '_duality_gap'] = cres['objective'] - pres['cplex_'+str(discr)+'_objective']
                    pres['cplex_' + str(discr) + '_relative_gap'] = (cres['objective'] - pres['cplex_'+str(discr)+'_objective']) / pres['objective']
    return python_results


def add_raw_tau(results, raw_tau):
    for pres in results:
        for cres in raw_tau:
            if cres['file'] == pres['file']:
                pres['raw_tau'] = str(cres['raw_tau'].tolist())[1:-1]
    return results


def write_results_to_csv(results, res_file, overwrite=False, raw_tau = None):
    if raw_tau is not None:
        results = add_raw_tau(results, raw_tau)
    if os.path.isfile(res_file) and not overwrite:
        csvfile = open(res_file, "a", newline='')
        reswriter = csv.writer(csvfile)
    else:
        csvfile = open(res_file, "w", newline='')
        reswriter = csv.writer(csvfile)
        reswriter.writerow(results[0].keys())
    for res in results:
        reswriter.writerow(res.values())
    csvfile.close()


def read_results_from_csv(res_file):
    with open(res_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        results = [row for row in reader]
    return results
