from typing import Dict, Any

def default_params():
    params: Dict[str, Any] = {
        "GRID_SIZE": 250,
        "TIME_STEP": 1,
        "NUM_STEPS": 20_000,
        "FEED_RATE": 0.014,
        "KILL_RATE": 0.047,
        "U_DIFFUSION": 0.16,
        "V_DIFFUSION": 0.08,
        "ANIMATION": True,
        "ANIMATION_FILE_NAME": "pattern.gif",

    }
    return params