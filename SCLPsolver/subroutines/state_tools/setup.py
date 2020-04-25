from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import sys

'''
To compile this (C++ code) in cython on Mac:

$ brew install cliutils/apple/libomp

$ export CC="/usr/bin/clang++ -Xpreprocessor -fopenmp -stdlib=libc++"
$ python setup.py build_ext --inplace
'''

if sys.platform == 'darwin':
    extra_compile_args = []
    extra_link_args = ["-lomp"]
else:
    extra_compile_args = ["/openmp"]
    extra_link_args = ["/openmp"]

setup(
    name='state_tools lib',
    ext_modules=cythonize(
        [Extension("state_tools", ["state_tools.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=extra_compile_args,
                   extra_link_args=extra_link_args),
         Extension("state_collide", ["state_collide.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=extra_compile_args,
                   extra_link_args=extra_link_args)]),
    zip_safe=False
)