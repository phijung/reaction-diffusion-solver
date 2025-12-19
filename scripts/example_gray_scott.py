from rdsolver import gray_scott
import matplotlib.pyplot as plt

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
        steps=50_000,
        feed_rate=0.014,
        kill_rate=0.047,
    )

    """
    plt.figure(figsize=(10, 10))
    plt.imshow(v, cmap="inferno", vmin=0, vmax=1)
    plt.axis("off")
    plt.show()
    """

if __name__ == "__main__":
    #mitosis()
    #solitons()
    #flower()
    #u_skate()
    #mazes()
    spirals()