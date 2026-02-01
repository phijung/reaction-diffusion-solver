from rdsolver import gray_scott


def spirals():
    _, _ = gray_scott(
        backend="numba",
        grid_size=500,
        steps=25_000,
        feed_rate=0.014,
        kill_rate=0.047,
        animation=True,
        animation_file_name="spiral.gif",
    )


if __name__ == "__main__":
    spirals()
