import os

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

    def get_CPLEX_data_file_name(self, exp_type, **kwargs):
        path = self.home_path + '/CPLEX/' + exp_type + '_'
        if kwargs is not None:
            for k,v in kwargs.items():
                path += str(k) + str(v) + '_'
        return path + 'data.dat'


