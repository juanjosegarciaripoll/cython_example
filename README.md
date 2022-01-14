# Cython sample module

This project is an example of a module that can be built using Cython. It is an upgrade from a similar model [developed by Arin Khare](https://levelup.gitconnected.com/how-to-deploy-a-cython-package-to-pypi-8217a6581f09).

## Structure

The structure of this project is as follows:
```
.
├── cython_example
│   ├── dataset
│   ├── hello.pyx
│   ├── matrix
|   |   ├── matrix.pyx
|   |   ├── norminf.pyx
|   |   ├── random.pyx
|   |   └── trace.pyx
│   └── random
|       ├── __init__.py
|       ├── crng.pxd
|       └── crng.pyx
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── test
│   └── test.py
├── clean.cmd
├── run.cmd
└── setup.py
```

Let me describe the individual components:
- `*.pyx` are files that will be compiled to native code from Cython/Python sources.
- `dataset` is an example of a file that will be installed raw.
- `hello.pxd` is a Cython file that will be compiled to a module with the path `cython_example.hello`
- `matrix.pyx` is a Cython file that joins three other files, `norminf.pyx`, `trace.pyx` and `random.pyx`, which will be joined under the same submodule, `cython_example.matrix`. It exemplifies how to join multiple files, how to export a module with multiple components and no `__init__.py` and how to call Cython functions/classes from other files.
- `random/*` is a Python module with a Cython component `crng.pyx` that defines a Cython class for random number generation. It exemplifies how to define a class that only contains C methods and can be used from other Cython files, in this case `matrix/random.pyx`, and illustrates a very useful case in which we do not want to use Numpy (RNG can be expensive if you have to go through Python calls).
- `MANIFEST.in` enumerates additional files that need to be installed in the package.
- `pyproject.toml` lists packages required to build this module (Cython, to start with), but which are not required for execution.
- `README.md` is this long description.
- `setup.py` is the Python program that builds the module and assists `pip` with the installation.
- `test/test.py` is a Python program that uses `cython_example` once built and installed, timing how fast the compiled functions are.
- `run.cmd` is a script to clean, compile, install and test the execution of this module, using `test.py`.

## C compilers

Using Cython requires a C compiler. In Unix platforms search for your package manager to find out how to specifically install the compiler that your Python distribution supports.

In Windows, as of 2022, you must install Microsoft Visual Build Tools 2017, available from [this link](https://aka.ms/vs/15/release/vs_buildtools.exe). If you use Anaconda, Microsoft C compiler must be installed *before* you install Python's `setuptools`, because this package will look for the C compiler when it is installed.

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
Note that if you already installed a previous version, you can use the argument `--force` after `install` to force reinstalling the package. Alternatively, you may just uninstall the package prior to reinstalling it again
```
pip uninstall -y cython_example
```

### Using setuptools

Another way to build the package is to directly use `setuptools` in your current Python environment. In this case, you use
```
python setup.py sdist bdist_wheel
```
to build the package, and then install `dist/cython_example*.whl`.

Note that this requires that you have already installed the build dependencies enumerated in `pyproject.toml`. If you use Anaconda, you may create a specific environment for this, following these steps:
```
conda create -n cython_env
conda activate cython_env
conda install setuptools cython numpy
```

## Trying out the package

The file `test/test.py` contains an example of a program that invokes all functions from all modules installed in `cython_example`. Note how the functions `norm1` and `test` are directly available form within the `matrix` submodule, because of the inline structure.
```
# cd test
# python ./test.py
norminf: 5.33 mus/iteration (Cython version a)
norminf: 14.6 mus/iteration (Numpy version)
norminf: 11.7 mus/iteration (Numpy library version)
trace: 0.487 mus/iteration (Cython version)
trace: 2.94 mus/iteration (Numpy version)
random: 6.72e+03 mus/iteration (Cython version)
random: 4.28e+03 mus/iteration (Numpy version)
```