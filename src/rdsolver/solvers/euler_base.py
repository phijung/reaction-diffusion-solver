from abc import ABC, abstractmethod
from rdsolver import config
from rdsolver.utils.pattern_plotting import pattern_plot
import numpy as np
from tqdm import tqdm


class ExplicitEulerBase(ABC):
    """
    Abstract base class for an euler solvers.
    """

    def __init__(self, params:dict) -> None:
        self.params: dict = params
        self.default_params: dict = config.default_params()

        self.time_step = self.params["TIME_STEP"]
        self.num_steps = self.params["NUM_STEPS"]
        self.kill_rate = self.params["KILL_RATE"]
        self.feed_rate = self.params["FEED_RATE"]
        self.u_diff = self.params["U_DIFFUSION"]
        self.v_diff = self.params["V_DIFFUSION"]
        self.grid_size = self.params["GRID_SIZE"]
        self.animation = self.params["ANIMATION"]

    @abstractmethod
    def laplacian(self, conc):
        """
        Compute the Laplacian of X, with a backend specified method.
        """
        pass

    def euler_step(self, u_conc, v_conc):
        """
        Single euler step
        """

        u_conc = np.asarray(u_conc, dtype=float)
        v_conc = np.asarray(v_conc, dtype=float)

        u_laplacian = np.asarray(self.laplacian(u_conc), dtype=float)
        v_laplacian = np.asarray(self.laplacian(v_conc), dtype=float)

        u_conc_new = (u_conc + self.time_step *
                      (self.u_diff * u_laplacian -
                       u_conc * v_conc**2 + self.feed_rate * (1 - u_conc)))

        v_conc_new = (v_conc + self.time_step *
                      (self.v_diff * v_laplacian +
                       u_conc * v_conc**2 - v_conc*(self.feed_rate + self.kill_rate)))

        return u_conc_new, v_conc_new

    def solve(self, u_conc, v_conc):
        """
        Run the solver for a given amount of time steps.
        """

        if self.animation:
            for i in range(self.num_steps):
                u_conc, c_conc = self.euler_step(u_conc, v_conc)
                if i%50 == 0:
                    pattern_plot(v_conc)
        else:
            for _ in tqdm(range(self.num_steps)):
                u_conc, v_conc = self.euler_step(u_conc, v_conc)

        return u_conc, v_conc
