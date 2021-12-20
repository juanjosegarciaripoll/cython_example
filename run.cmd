@echo off
call clean.cmd
rem
rem Uncomment the version (build / setuptools) you wish to use
rem 
python -m build
rem python setup.py bdist_wheel
for %%i in (dist\cython_example*.whl) do pip install --force %%i
python test/test.py
