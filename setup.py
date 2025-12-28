from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        name="laplacian_pybind",
        sources=["src/rdsolver/solvers/euler_pybind.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-std=c++17", "-O2", "-march=native", "-fopenmp"],
        extra_link_args=["-fopenmp"],
    ),
]

setup(
    name="reaction-diffusion-solver",
    version="0.1.0",
    ext_modules=ext_modules,
    python_requires=">=3.11",
)
