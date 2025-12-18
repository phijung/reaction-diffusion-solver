from src.rdsolver.solvers.euler_base import ExplicitEulerBase

class ExplicitEulerNumbaParallel(ExplicitEulerBase):
    """
    Backend in parallelized numba.
    """

    def laplacian(self, conc):
        pass
