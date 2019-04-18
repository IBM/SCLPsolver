import os
import csv

def combine_results(python_results, cplex_results, discr):
    for pres in python_results:
        for cres in cplex_results:
            if cres['file'] == pres['file']:
                pres['cplex_'+str(discr)+'_objective'] = cres['objective']
                pres['cplex_'+str(discr)+'_time'] = cres['time']
                pres['cplex_' + str(discr) + '_relative_objective'] = (pres['objective']-cres['objective'])/pres['objective']
                pres['cplex_' + str(discr) + '_relative_time'] = cres['time'] / pres['time']
    return python_results

def write_results_to_csv(results, res_file, overwrite=False):
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