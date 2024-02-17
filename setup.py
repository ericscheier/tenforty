"""Setup for tenforty package."""

from Cython.Build import cythonize
from setuptools import Extension, setup

setup(
    ext_modules=cythonize([Extension("tenforty.otslib", ["tenforty/otslib/ots.pyx"])])
)
