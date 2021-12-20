# Cython sample module

This project is an example of a module that can be built using Cython. It is an upgrade from a similar model [developed by Arin Khare](https://levelup.gitconnected.com/how-to-deploy-a-cython-package-to-pypi-8217a6581f09).

## Structure

The structure of this project is as follows:
```
.
├── cython_example
│   ├── dataset
│   ├── hello.pyx
│   └── matrix
|       ├── matrix.pyx
|       ├── norm1.pyx
|       └── trace.pyx
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── test
│   └── test.py
└── setup.py
```

Let me describe the individual components:
- `*.pyx` are files that will be compiled to native code from Cython/Python sources.
- `dataset` is an example of a file that will be installed raw.
- `hello.pxd` is a Cython file that will be compiled to a module with the path `cython_example.hello`
- `matrix.pyx` is a Cython file that joins two other files, `norm1.pyx` and `trace.pyx`, which will be joined under the same submodule, `cython_example.matrix`
- `MANIFEST.in` enumerates additional files that need to be installed in the package.
- `pyproject.toml` lists packages required to build this module (Cython, to start with), but which are not required for execution.
- `README.md` is this long description.
- `setup.py` is the Python program that builds the module and assists `pip` with the installation.


## Building and installing from sources

### Using a virtual environment

The canonical way to build and install the package is to use [setuptools with a build system](https://setuptools.pypa.io/en/latest/build_meta.html). In Anaconda, this means you have to install
```
conda install setuptools build
```
Then you can issue the command
```
python -m build
```
from within the directory of this project. This command will create a new environment only with the libraries indicated in `pyproject.toml` and build your extension there.

The binary of this build process will be stored as `dist/cython_example-*.whl`, with some intermediate characters in '*' that represent the version of python and operating system or platform it was built for. You can install this binary on your system using
```
pip install dist/cython_example*.whl
```
Note that if you already installed a previous version, you can use the argument `--force` after `install` to force reinstalling the package.

### Using setuptools

Alternatively, you can use
```
python setup.py sdist bdist_wheel
```
This requires that you have already installed the build dependencies enumerated in `pyproject.toml`.

## Trying out the package

The file `test/test.py` contains an example of a program that invokes all functions from all modules installed in `cython_example`. Note how the functions `norm1` and `test` are directly available form within the `matrix` submodule, because of the inline structure.