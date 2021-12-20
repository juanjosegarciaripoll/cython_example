from setuptools import find_packages, setup

import numpy as np
from Cython.Build import cythonize

setup(
    name='cython_example',
    version='0.0.1',
    packages=find_packages(),
    author='Juan Jose Garcia-Ripoll',
    description="An example for a Cython-based package.",
    url='https://juanjose.garciaripoll.com',
    ext_modules=cythonize(["cython_example/__init__.pyx"]),
    include_dirs=np.get_include(),
    install_requires=[
        'numpy',
    ],
)