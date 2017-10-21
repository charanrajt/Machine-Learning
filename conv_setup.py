from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("cython_conv.pyx"),)

#python conv_setup.py build_ext --inplace
