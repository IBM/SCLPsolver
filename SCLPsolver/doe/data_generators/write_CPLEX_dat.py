from scipy.io import mmwrite
from scipy.sparse import csr_matrix
import numpy as np
import os


def write_CPLEX_dat(file_name, T, G, H, alpha, a, b, gamma, c, buf_cost):
    f1 = file_name + 'g.mtx'
    mmwrite(f1, csr_matrix(G))
    f2 = file_name + 'h.mtx'
    mmwrite(f2, csr_matrix(H))
    fout = open(file_name, 'w')
    fout.write('T = {:f};\n'.format(T))
    fout.write('VarDimension = {:d};\n'.format(G.shape[1]))
    fout.write('ConstrDimensionH = {:d};\n'.format(H.shape[0]))
    fout.write('ConstrDimensionG = {:d};\n'.format(G.shape[0]))
    fout.write('G = {\n')
    with open(f1,'r') as fp:
        prev_line = fp.readline()
        line = prev_line
        while line:
            if prev_line[0] != '%':
                fout.write('<'+ line[:-1] +'>\n')
            prev_line = line
            line = fp.readline()
        fp.close()
    os.remove(f1)
    fout.write( '};\n\n')
    fout.write('H = {\n')
    with open(f2, 'r') as fp:
        prev_line = fp.readline()
        line = prev_line
        while line:
            if prev_line[0] != '%':
                fout.write('<' + line[:-1] + '>\n')
            prev_line = line
            line = fp.readline()
        fp.close()
    os.remove(f2)
    fout.write('};\n\n')
    fout.write('alpha = {\n')
    for i in np.nonzero(alpha)[0]:
        fout.write('<{:d} {:d} {:.16f}>\n'.format(i+1,1,alpha[i]))
    fout.write('};\n\n')
    fout.write('a = {\n')
    for i in np.nonzero(a)[0]:
        fout.write('<{:d} {:d} {:.16f}>\n'.format(i+1, 1, a[i]))
    fout.write('};\n\n')
    fout.write('b = {\n')
    for i in np.nonzero(b)[0]:
        fout.write('<{:d} {:d} {:.16f}>\n'.format(i+1, 1, b[i]))
    fout.write('};\n\n')
    fout.write('buf_cost = {\n')
    for i in np.nonzero(buf_cost)[0]:
        fout.write('<{:d} {:d} {:.16f}>\n'.format(i + 1, 1, buf_cost[i]))
    fout.write('};\n\n')
    fout.write('c = {\n')
    for i in np.nonzero(c)[0]:
        fout.write('<{:d} {:d} {:.16f}>\n'.format(i+1, 1, c[i]))
    fout.write('};\n\n')
    fout.write('gamma = {\n')
    for i in np.nonzero(gamma)[0]:
        fout.write('<{:d} {:d} {:.16f}>\n'.format(i+1, 1, gamma[i]))
    fout.write('};\n\n')
    fout.close()