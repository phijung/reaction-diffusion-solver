from src.rdsolver.solvers.euler_base import ExplicitEulerBase

class ExplicitEulerParallel(ExplicitEulerBase):
    """
    Parallelized backend.
    """

    def laplacian(self, conc):
        pass