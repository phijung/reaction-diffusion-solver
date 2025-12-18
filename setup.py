from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        name="laplacian_pybind",
        sources=["src/rdsolver/solvers/euler_pybind.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-std=c++11", "-O3", "-march=native", "-ffast-math"],
    ),
]

setup(
    name="laplacian_pybind",
    version="0.1",
    ext_modules=ext_modules,
    python_requires=">=3.12",
)

