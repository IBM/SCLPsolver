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

default_translation_table = {'sum_rate': 'sr', 'gdist':'gd', 'gdist_params':'gdp', 'h_rate': 'hr', 'hdist': 'hd', 'hdist_params' :'hdp',
                             'alpha_rate': 'alpr', 'alpha_dist': 'alpd', 'alpha_dist_params': 'alpdp', 'a_rate': 'ar', 'a_dist' : 'ad',
                             'a_dist_params': 'adp', 'cost_scale': 'cs', 'cost_dist': 'cd',  'cost_dist_params': 'cdp', 'gamma_rate': 'gmr',
                             'gamma_dist' : 'gmd', 'gamma_dist_params': 'gmdp', 'c_scale': 'ccs', 'c_dist' : 'ccd', 'c_dist_params': 'ccdp'}

def reverse_translation_table(table):
    result = dict()
    for k,v in table.items():
        result[v] = k

class path_utils:

    def __init__(self, home_path):
        if home_path is None:
            self.home_path = os.path.expanduser('~/Box/SCLP comparison/data')
        else:
            self.home_path = home_path

    def get_experiment_type_path(self, exp_type):
        return self.home_path + '/' + exp_type

    def get_experiment_path_old(self, exp_type, K, I, seed):
        return self.get_experiment_type_path(exp_type) + '/K'+str(K)+'/I' + str(I)+ '/seed' + str(seed)

    def get_experiment_path(self, exp_type, **kwargs):
        path = self.get_experiment_type_path(exp_type)
        if kwargs is not None:
            for k,v in kwargs.items():
                path += '/' + str(k) + str(v)
        return path

    def get_CPLEX_data_file_name(self, exp_type, translation_table = None, **kwargs):
        path = self.home_path + '/CPLEX/' + exp_type + '_'
        if kwargs is not None:
            kwargs = self.translate_param_names(translation_table, **kwargs)
            for k,v in kwargs.items():
                path += str(k) + str(v) + '_'
        return path + 'data.dat'

    def get_tmp_data_file_name(self, exp_type, translation_table = None, **kwargs):
        path = self.home_path + '/tmp/' + exp_type + '_'
        if kwargs is not None:
            kwargs = self.translate_param_names(translation_table, **kwargs)
            for k,v in kwargs.items():
                path += str(k) + str(v) + '_'
        return path

    def get_CPLEX_data_path(self):
        return self.home_path + '/CPLEX'

    def translate_param_names(self, translation_table=None, **kwargs):
        if translation_table is None:
            translation_table = default_translation_table
        result = dict()
        if kwargs is not None:
            for k,v in kwargs.items():
                if k in translation_table.keys():
                    result[translation_table[k]] = v
                else:
                    result[k] = v
        return result


