from src.rdsolver.solvers.euler_base import ExplicitEulerBase
import numpy as np

class ExplicitEulerNumPy(ExplicitEulerBase):
    """
    Backend in numpy.
    """

    def laplacian(self, conc):
        padded = np.pad(conc, pad_width=1, mode='edge')

        up = padded[2:, 1:-1]
        down = padded[:-2, 1:-1]
        left = padded[1:-1, 2:]
        right = padded[1:-1, :-2]
        center = padded[1:-1, 1:-1]

        laplacian = up + down + left + right - 4.0 * center

        return laplacian
