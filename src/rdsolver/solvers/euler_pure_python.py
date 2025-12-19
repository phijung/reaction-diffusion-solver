from rdsolver.solvers.euler_base import ExplicitEulerBase

class ExplicitEulerPure(ExplicitEulerBase):
    """
    Backend in pure python code.
    """

    def laplacian(self, conc):
        size = self.grid_size
        grid_2d = [[0.0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                up = conc[max(i - 1, 0)][j]
                down = conc[min(i + 1, size - 1)][j]
                left = conc[i][max(j - 1, 0)]
                right = conc[i][min(j + 1, size - 1)]
                center = conc[i][j]
                grid_2d[i][j] = up + down + left + right - 4 * center
        return grid_2d
