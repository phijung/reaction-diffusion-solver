from src.rdsolver.solvers.euler_base import ExplicitEulerBase

class ExplicitEulerPybind(ExplicitEulerBase):
    """
    Pybind backend
    """

    def laplacian(self, conc):
        pass