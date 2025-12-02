from src.rdsolver.solvers.euler_base import ExplicitEulerBase

class ExplicitEulerNumba(ExplicitEulerBase):
    """
    Backend in Numba.
    """

    def laplacian(self, conc):
        pass