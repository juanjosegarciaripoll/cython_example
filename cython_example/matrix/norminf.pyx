def norminf(double[:,::1] matrix):
    cdef Py_ssize_t m
    cdef double norm = 0.0, aux
    for m in range(matrix.shape[0]):
        aux = 0
        for n in range(matrix.shape[1]):
            aux += abs(matrix[m,n])
        norm = max(aux, norm)
    return norm

