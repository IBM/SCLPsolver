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

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import sys

'''
To compile this (C code) in cython on Mac:

$ $ brew install gcc

$ export CC=/usr/local/bin/gcc-9
$ python setup.py build_ext --inplace
'''


if sys.platform == 'darwin':
    extra_compile_args = []#["-fopenmp"]
    extra_link_args = ["-lomp"]
else:
    extra_compile_args = ["/openmp"]
    extra_link_args = ["/openmp"]


setup(
    name='eq tools',
    ext_modules=cythonize([Extension("eq_tools", ["eq_tools.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=extra_compile_args,
                extra_link_args=extra_link_args)]),
    zip_safe=False
)