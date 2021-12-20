from setuptools import find_packages, setup, Extension

import numpy as np
from Cython.Build import cythonize
import Cython.Compiler.Options

extensions = [
    # A single module that is stand alone and has no special requisites
    Extension('cython_example.hello', ['cython_example/hello.pyx']),

    # A module that is built from various functions, and which itself depends
    # on the numpy library (the C core of this library)
    Extension('cython_example.matrix', ['cython_example/matrix/matrix.pyx'],
        include_dirs=[np.get_include()])
    ]

# See https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
# for a deeper explanation of the choices here
Cython.Compiler.Options.docstring = False
Cython.Compiler.Options.error_on_uninitialized = True
directives = {
    'language_level': '3', # We assume Python 3 code
    'boundscheck': False, # Do not check array access
    'wraparound': False, # a[-1] does not work
    'embedsignature': False, # Do not save typing / docstring
    'always_allow_keywords': False, # Faster calling conventions
}

setup(
    name='cython_example',
    version='0.0.1',
    packages=['cython_example'],
    author='Juan Jose Garcia-Ripoll',
    author_email='juanjose.garciaripoll@gmail.com',
    description="An example for a Cython-based package.",
    url='https://juanjose.garciaripoll.com',
    ext_modules=cythonize(extensions, 
                          compiler_directives=directives),
    include_dirs=np.get_include(),
    install_requires=[
        'numpy',
    ],
)