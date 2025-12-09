import numpy as np

def create_initial_conditions(size: int, noise_seed: int = None) -> tuple[np.ndarray, np.ndarray]:
    """
    Create initial field for Gray-Scott with a single v spot in the center,
    plus optional random noise.
    """
    if noise_seed is not None:
        np.random.seed(noise_seed)

    u_conc = np.ones((size, size), dtype=float)
    v_conc = np.zeros((size, size), dtype=float)

    r = size // 10  # Size of the spot
    c = size // 2   # Center of the grid

    u_conc[c-r:c+r, c-r:c+r] = 0.50
    v_conc[c-r:c+r, c-r:c+r] = 0.25

    # Add small random noise
    u_conc += 0.02 * np.random.rand(size, size)
    v_conc += 0.02 * np.random.rand(size, size)

    return u_conc, v_conc
