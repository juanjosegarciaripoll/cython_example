@echo off
for /R cython_example %%i in (*.pyd *.c) do del %%i 
for %%i in (build cython_example.egg-info dist) do if exist %%i del /S /Q %%i
pip uninstall -y cython_example 2>NUL

