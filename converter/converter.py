import os
from os.path import isfile, join

path = 'C:/EclipseWorkSpaces/CERBERO/M-CLP-solver/SCLP - Gideon'

def create_file_list(mypath):
    for root, dirs, files in os.walk(mypath):
        for name in files:
            if name.endswith('.m'):
                print(join(root, name))

create_file_list(path)





