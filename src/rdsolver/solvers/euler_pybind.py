from rdsolver.solvers.euler_base import ExplicitEulerBase
from laplacian_pybind import laplacian_serial

class ExplicitEulerPybind(ExplicitEulerBase):
    """
    Pybind backend
    """

    def laplacian(self, conc):
        return laplacian_serial(conc)
