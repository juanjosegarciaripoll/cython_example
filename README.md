# Cython sample module

This project is an example of a module that can be built using Cython. It is an upgrade from a similar model [developed by Arin Khare](https://levelup.gitconnected.com/how-to-deploy-a-cython-package-to-pypi-8217a6581f09).

## Structure

The structure of this project is as follows:
```
.
├── cython_example
│   ├── dataset
│   ├── __init__.pxd
│   ├── __init__.pyx
│   └── test_classification_library.py
├── MANIFEST.in
├── pyproject.toml
├── README.md
└── setup.py
```

Let me describe the individual components:
- `*.pyx` are files that will be compiled to native code from Cython/Python sources.
- `*.pyd` are Cython declarations that can be used by other projects using this library.
- `dataset` is an example of a file that will be installed raw.
- `MANIFEST.in` enumerates additional files that need to be installed in the package.
- `pyproject.toml` lists packages required to build this module (Cython, to start with), but which are not required for execution.
- `README.md` is this long description.
- `setup.py` is the Python program that builds the module and assists `pip` with the installation.

## Building and installing from sources

The canonical way to build and install the package is to use [setuptools with a build system](https://setuptools.pypa.io/en/latest/build_meta.html). In Anaconda, this means you have to install
```
conda install setuptools build
```
Then you can issue the command
```
python -m build
```
from within the directory of this project. This command will create a new environment only with the libraries indicated in `pyproject.toml` and build your extension there.

Alternatively, you can also use
```
python setup.py sdist bdist_wheel
```
provided you have already installed the build dependencies enumerated in `pyproject.toml`.

Both processes create a `dist` directory with two files. The file `cython_example*.tar.gz` contains the sources and all files to rebuild the extension in any other machine. The file `cython_example*.whl` contains the binaries for this particular computer.
