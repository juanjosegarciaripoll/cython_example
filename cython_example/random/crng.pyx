# Congruential random number generator

import numpy as np
cimport numpy as cnp
import time

cdef class CRNG:

    def __init__(CRNG self, seed: None):
        if seed is None:
            seed = time.time()
        elif isinstance(seed, np.random.Generator):
            seed = seed.integers(0, 0xffffffffULL, 1)[0]
        else:
            seed = int(seed)
        self.seed(seed)

    cdef cnp.uint64_t seed(CRNG self, cnp.uint64_t seed) nogil:
        self.seed_ = seed
        self.mult_ = 6364136223846793005ULL
        self.add_  = 1442695040888963407ULL

    cdef cnp.uint64_t integer64(CRNG self) nogil:
        cdef cnp.uint64_t x = self.mult_ * self.seed_ + self.add_
        self.seed_ = x
        return x

    cdef cnp.uint32_t integer32(CRNG self) nogil:
        return self.integer64() >> 20

    cdef double random(CRNG self) nogil:
        """
        Generate a uniform random variable in [0,1)
        :return: (double) a random uniform number in [0,1)
        """
        return (self.integer64() >> 11) * (1.0/9007199254740992.0)