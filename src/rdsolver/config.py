from typing import Dict, Any

def default_params():
    params: Dict[str, Any] = {
        "GRID_SIZE": 100,
        "TIME_STEP": 1e-2,
        "NUM_STEPS": 8000,
        "FEED_RATE": 0.035,
        "KILL_RATE": 0.065,
        "U_DIFFUSION": 0.16,
        "V_DIFFUSION": 0.08,

    }
    return params