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