import numpy as np
cimport numpy as cnp
from .random.crng cimport CRNG
from typing import Optional

def random(shape, rng: Optional[np.random.Generator] = None) -> np.ndarray:
    cdef:
        double[::1] view
        CRNG crng = CRNG(rng)
    output = np.empty(shape, dtype=np.double)
    view = output.flatten()
    for n in range(view.size):
        view[n] = crng.random()
    return output
