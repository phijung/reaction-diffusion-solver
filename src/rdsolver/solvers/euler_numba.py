from numba import njit
import numpy as np
from rdsolver.solvers.euler_base import ExplicitEulerBase

@njit
def laplacian_numba(conc):
    size_x, size_y = conc.shape
    lap = np.zeros_like(conc)
    for i in range(size_x):
        for j in range(size_y):
            up = conc[i-1, j] if i > 0 else conc[i, j]
            down = conc[i+1, j] if i < size_x-1 else conc[i, j]
            left = conc[i, j-1] if j > 0 else conc[i, j]
            right = conc[i, j+1] if j < size_y-1 else conc[i, j]
            lap[i, j] = up + down + left + right - 4.0 * conc[i, j]
    return lap

class ExplicitEulerNumba(ExplicitEulerBase):
    """
    Backend in Numba.
    """

    def laplacian(self, conc):
        conc = np.asarray(conc, dtype=float)
        return laplacian_numba(conc)
