def trace(double[:,::1] matrix):
    cdef Py_ssize_t m
    cdef double E = 0.0
    for m in range(matrix.shape[0]):
        E += matrix[m,m]
    return E
