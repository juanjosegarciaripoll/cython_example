python -m build
for %%i in (dist\cython_example*.whl) do pip install --force %%i
python test/test.py
