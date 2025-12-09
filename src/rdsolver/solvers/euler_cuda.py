from src.rdsolver.solvers.euler_base import ExplicitEulerBase

class ExplicitEulerCuda(ExplicitEulerBase):
    """
    Backend for the GPU.
    """

    def laplacian(self, conc):
        pass