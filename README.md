# Python Benchmarking with the Gray Scott Model

This repository contains the final project of the course "VU Software Solutions for HPC", a modular Python library,
for solving a reaction diffusion PDE (the Gray Scott model) with a strong focus on performant python implementations.
Multiple backends are provided, including NumPy, Numba, and pybind11 based C++ implementations with optional OpenMP
parallelization, allowing direct performance comparison against a pure Python/NumPy reference.

## Requirements

- Python >=3.11
- C++ compiler
- openMP

## Installation

To use this library, first clone the repository. Then create and activate a virtual environment in the root directory:

```bash
python -m venv .venv  
source ./.venv/bin/activate
```
Next, install the library using:
```bash
pip install .
```
his will automatically install all required Python dependencies and compile the C++ code.

This library was developed and tested on Linux and should run on most Linux distributions. On macOS,
the core Python functionality is available, however, the pybind based backends are not supported.
During installation on macOS, the C++ components are not compiled, and attempting to use the pybind backends
will result in errors.

Support for other operating systems has not been tested. Users running unsupported or nonstandard platforms should
expect potential compatibility issues.

## Usage

An example script demonstrating how to use the library is provided in the `scripts` folder as `example_gray_scott.py`.
This script shows a typical workflow for running a Gray–Scott simulation. All the parameters are optional,
if none are given, the solver falls back to default parameters. It does this also, when only a few parameters are given,
the others are used from the fallback option.

The main parameters to control the simulation are:

- `backend`: The computational backend to use (`python`, `numpy`, `numba`, `pybind` or `pybind_parallel`).
- `grid_size`: The size of the 2D simulation grid.
- `steps`: Number of time steps to simulate.
- `feed_rate` and `kill_rate`: Reaction parameters that determine the pattern formation.
- `animation` and `animation_file_name`: Control if a visual output is produced.

There are additional parameters available in the configuration:

- `time_step`: The size of the timestep.
- `u_diffusion`: The diffusion parameter for u.
- `v_diffusion`: The diffusion parameter for V

**Warning:** Changing the timestep or the diffusion coefficients is not recommended, as it may lead to numerical
instability.

A benchmarking script is also included in the `scripts` directory as `benchmarking.py`.
This can be used to compare the performance of different backends and grid sizes.

The following parameter combinations produce characteristic patterns in the Gray–Scott model:

| Pattern    | Feed rate | Kill rate  |
|------------|-----------|------------|
| Mitosis    | 0.035     | 0.065      |
| Solitons   | 0.030     | 0.060      |
| Flower     | 0.055     | 0.062      |
| U-Skate    | 0.062     | 0.061      |
| Mazes      | 0.029     | 0.057      |

## Example results

The library was benchmarked across multiple backends and grid sizes. A full table of the benchmarking results is 
available in [`results/benchmark_results.pdf`](results/benchmark_results.pdf). 
This includes measured runtimes for the backends (NumPy, Numba, pybind, pybind + OpenMP) on various grid sizes.

## License

This project is licensed under the MIT License.
