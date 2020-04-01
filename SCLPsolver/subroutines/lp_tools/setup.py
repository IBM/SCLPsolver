from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import sys

if sys.platform == 'darwin':
    extra_compile_args = ["-fopenmp"]
    extra_link_args = ["-fopenmp"]
else:
    extra_compile_args = ["/openmp"]
    extra_link_args = ["/openmp"]


setup(
    name='pivot app',
    ext_modules=cythonize([Extension("pivot1", ["pivot1.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=extra_compile_args,
                extra_link_args=extra_link_args)]),
    zip_safe=False
)