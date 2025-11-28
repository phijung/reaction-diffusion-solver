import numpy as np

def create_initial_conditions(size: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Create initial field for gray scott with a single v spot in the center.
    """

    u_conc = np.ones((size, size), dtype=float)
    v_conc = np.zeros((size, size), dtype=float)

    r = size // 10 # Size of the spot
    c = size // 2 # center of the grid

    u_conc[c-r:c+r, c-r:c+r] = 0.50
    v_conc[c-r:c+r, c-r:c+r] = 0.25

    return u_conc, v_conc