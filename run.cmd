@echo off
call clean.cmd
rem
rem Uncomment the version (build / setuptools) you wish to use
rem 
rem python -m build
python setup.py bdist_wheel
for %%i in (dist\cython_example*.whl) do pip install %%i
python test/test.py
