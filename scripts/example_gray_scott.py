from rdsolver import gray_scott

def mitosis():
    u, v = gray_scott(
        backend="pybind_parallel",
        grid_size=500,
        steps=50_000,
        feed_rate=0.035,
        kill_rate=0.065,
    )

def solitons():
    u, v = gray_scott(
        backend="pybind_parallel",
        grid_size=500,
        steps=50_000,
        feed_rate=0.03,
        kill_rate=0.06,
    )

def flower():
    u, v = gray_scott(
        backend="pybind_parallel",
        grid_size=500,
        steps=50_000,
        feed_rate=0.055,
        kill_rate=0.062,
    )

def u_skate():
    u, v = gray_scott(
        backend="pybind_parallel",
        grid_size=500,
        steps=50_000,
        feed_rate=0.062,
        kill_rate=0.061,
    )

def mazes():
    u, v = gray_scott(
        backend="pybind_parallel",
        grid_size=500,
        steps=50_000,
        feed_rate=0.029,
        kill_rate=0.057,
    )

def spirals():
    u, v = gray_scott(
        backend="numba",
        grid_size=500,
        steps=25_000,
        feed_rate=0.014,
        kill_rate=0.047,
        animation=True,
        animation_file_name="spiral.gif",
    )

if __name__ == "__main__":
    #mitosis()
    #solitons()
    #flower()
    #u_skate()
    #mazes()
    spirals()
