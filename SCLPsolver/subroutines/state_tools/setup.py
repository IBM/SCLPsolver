from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import sys

if sys.platform == 'darwin':
    extra_compile_args = []#["-fopenmp"]
    extra_link_args = ["-lomp", "-stdlib=libc++"]
else:
    extra_compile_args = ["/openmp"]
    extra_link_args = ["/openmp"]

setup(
    name='state_tools lib',
    ext_modules=cythonize(
        [Extension("state_tools", ["state_tools.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=extra_compile_args,
                   extra_link_args=extra_link_args)]),
    zip_safe=False
)