import cython_example as ce
import numpy as np
from timeit import Timer

def timeit(stmt):
    t = Timer(stmt, globals=globals())
    n = t.autorange() # calibrate No. of iterations
    t.timeit(n[0]) # warm up
    return t.timeit(n[0]*2)/n[0]/2/1e-6

def norminfc(A):
    return np.max(np.sum(np.abs(A), -1))

A = np.random.randn(100, 100)

t = timeit('ce.matrix.norminf(A)')
print(f'norminf: {t:1.3g}mus/iteration (Cython version a)')

t = timeit('norminfc(A)')
print(f'norminf: {t:1.3g}mus/iteration (Numpy version)')

t = timeit('np.linalg.norm(A, ord=np.inf)')
print(f'norminf: {t:1.3g}mus/iteration (Numpy library version)')

t = timeit('ce.matrix.trace(A)')
print(f'trace: {t:1.3g}mus/iteration (Cython version)')

t = timeit('np.trace(A)')
print(f'trace: {t:1.3g}mus/iteration (Numpy version)')

