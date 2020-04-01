from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    name='state_tools lib',
    ext_modules=cythonize(
        [Extension("state_tools", ["state_tools.pyx"], include_dirs=[numpy.get_include()], extra_compile_args=["/openmp"],
                   extra_link_args=["/openmp"])]),
    zip_safe=False
)