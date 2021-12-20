import cython_example as ce
import numpy as np
from timeit import Timer

def timeit(stmt):
    t = Timer(stmt, globals=globals())
    n = t.autorange()
    return t.timeit(n[0])

def norminfc(A):
    return np.max(np.sum(np.abs(A), -1))

A = np.random.randn(100, 100)

t = timeit('ce.matrix.norminf(A)')
print(f'norminf: {t} (Cython version a)')

t = timeit('ce.matrix.norminfb(A)')
print(f'norminf: {t} (Cython version b)')

t = timeit('norminfc(A)')
print(f'norminf: {t} (Numpy version)')

t = timeit('np.linalg.norm(A, ord=np.inf)')
print(f'norminf: {t} (Numpy library version)')

t = timeit('ce.matrix.trace(A)')
print(f'trace: {t} (Cython version)')

t = timeit('np.trace(A)')
print(f'trace: {t} (Numpy version)')

