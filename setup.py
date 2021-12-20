from setuptools import find_packages, setup, Extension

import numpy as np
from Cython.Build import cythonize

extensions = [
    # A single module that is stand alone and has no special requisites
    Extension('cython_example.hello', ['cython_example/hello.pyx']),

    # A module that is built from various functions, and which itself depends
    # on the numpy library (the C core of this library)
    Extension('cython_example.matrix', ['cython_example/matrix/matrix.pyx'],
        include_dirs=[np.get_include()])
    ]

setup(
    name='cython_example',
    version='0.0.1',
    packages=['cython_example'],
    author='Juan Jose Garcia-Ripoll',
    author_email='juanjose.garciaripoll@gmail.com',
    description="An example for a Cython-based package.",
    url='https://juanjose.garciaripoll.com',
    ext_modules=cythonize(extensions, 
                          compiler_directives={'language_level' : "3"}),
    include_dirs=np.get_include(),
    install_requires=[
        'numpy',
    ],
)