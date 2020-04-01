from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    name='pivot app',
    ext_modules=cythonize([Extension("pivot1", ["pivot1.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=["/openmp"],
                extra_link_args=["/openmp"])]),
    zip_safe=False
)