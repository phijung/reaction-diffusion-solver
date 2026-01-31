"""
API for the solver.
"""

from rdsolver.solvers.euler_numba import ExplicitEulerNumba
from rdsolver.config import default_params
from rdsolver.solvers.euler_pure_python import ExplicitEulerPure
from rdsolver.solvers.euler_numpy import ExplicitEulerNumPy
from rdsolver.model.initial_conditions import create_initial_conditions


try:
    from rdsolver.solvers.euler_pybind import ExplicitEulerPybind
    from rdsolver.solvers.euler_pybind_parallel import ExplicitEulerPybindParallel
except ImportError:
    import warnings

    warnings.warn(
        "Pybind backends are currently not available on your operating system!"
    )


PARAM_MAP = {
    "grid_size": "GRID_SIZE",
    "steps": "NUM_STEPS",
    "time_step": "TIME_STEP",
    "feed_rate": "FEED_RATE",
    "kill_rate": "KILL_RATE",
    "u_diff": "U_DIFFUSION",
    "v_diff": "V_DIFFUSION",
    "animation": "ANIMATION",
    "animation_file_name": "ANIMATION_FILE_NAME",
}


def gray_scott(backend="numpy", params=None, **kwargs):
    """
    Main API function.
    """

    p = default_params()

    if params is not None:
        p.update(params)

    for key, internal_key in PARAM_MAP.items():
        if key in kwargs and kwargs[key] is not None:
            p[internal_key] = kwargs[key]

    u_initial, v_initial = create_initial_conditions(size=p["GRID_SIZE"])

    if backend == "python":
        u_initial = u_initial.tolist()
        v_initial = v_initial.tolist()
        solver = ExplicitEulerPure(p)
        return solver.solve(u_initial, v_initial)

    if backend == "numpy":
        solver = ExplicitEulerNumPy(p)

        return solver.solve(u_initial, v_initial)

    if backend == "numba":
        solver = ExplicitEulerNumba(p)

        return solver.solve(u_initial, v_initial)

    if backend == "pybind":
        solver = ExplicitEulerPybind(p)

        return solver.solve(u_initial, v_initial)

    if backend == "pybind_parallel":
        solver = ExplicitEulerPybindParallel(p)

        return solver.solve(u_initial, v_initial)

    else:
        raise ValueError(f"Unknown backend: {backend}")


__all__ = ["gray_scott"]
