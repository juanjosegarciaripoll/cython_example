cimport numpy as cnp

cdef class CRNG:

    cdef cnp.uint64_t seed_, mult_, add_

    cdef cnp.uint64_t seed(CRNG self, cnp.uint64_t seed) nogil
    cdef cnp.uint64_t integer64(CRNG self) nogil
    cdef cnp.uint32_t integer32(CRNG self) nogil
    cdef double random(CRNG self) nogil
