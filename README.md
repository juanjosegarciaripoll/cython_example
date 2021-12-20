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

## Installing from sources

Let us assume that this folder is available in your system and you want to install the library. The canonical step to do so is
```
python setup.py install
```
