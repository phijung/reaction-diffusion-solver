from setuptools import setup, Extension
import pybind11
import sys

compile_args = ["-std=c++17", "-O3"]
link_args = []

if sys.platform != "darwin":
    compile_args += ["-fopenmp"]
    link_args += ["-fopenmp"]


ext_modules = [
    Extension(
        name="laplacian_pybind",
        sources=["src/rdsolver/solvers/euler_pybind.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=compile_args,
        extra_link_args=link_args,
    ),
]

setup(
    name="reaction-diffusion-solver",
    version="0.1.0",
    ext_modules=ext_modules,
)
