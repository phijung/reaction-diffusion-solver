from src.rdsolver.solvers.euler_base import ExplicitEulerBase
import laplacian_pybind
import numpy as np

class ExplicitEulerPybind(ExplicitEulerBase):
    """
    Pybind backend
    """

    def laplacian(self, conc):
        return laplacian_pybind.laplacian_pybind(conc)
