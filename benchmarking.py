import timeit
from src.rdsolver import gray_scott
import pandas as pd
import gc


def benchmark(grid_sizes: list[int], backends: list[str], repeats: int):
    """
    Simple benchmarking function.
    """

    data: list = []
    # timeit should disable the garbage collector, but it seems, this does not work properly?
    gc.disable()

    for grid_size in grid_sizes:

        for backend in backends:

            # Warmup
            gray_scott(grid_size=grid_size, backend=backend, steps=100)

            # Benchmarking
            times = timeit.repeat(stmt=lambda: gray_scott(grid_size=grid_size, backend=backend, steps=100),
                                  repeat=repeats,
                                  number= 1
            )

            row = {"grid_size": grid_size, "backend": backend}
            for i, t in enumerate(times, start=1):
                row[f"time_run_{i}"] = t

            data.append(row)

    gc.enable()

    df = pd.DataFrame(data)
    df.set_index(["grid_size", "backend"], inplace=True)
    df.to_pickle("benchmark.pkl")
    print(df)


if __name__ == "__main__":

    benchmark([25, 50, 100],
              ["python", "numpy", "numba"],
              5)