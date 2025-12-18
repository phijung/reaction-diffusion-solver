from src.rdsolver.solvers.euler_base import ExplicitEulerBase
from laplacian_pybind import laplacian_parallel

class ExplicitEulerPybindParallel(ExplicitEulerBase):
    """
    Pybind backend with openMP
    """

    def laplacian(self, conc):
        return laplacian_parallel(conc)