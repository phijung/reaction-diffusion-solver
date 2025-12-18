#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

py::array_t<double> laplacian_pybind(py::array_t<double, py::array::c_style | py::array::forcecast> input) {
    auto conc = input.unchecked<2>();

    const size_t num_rows = conc.shape(0);
    const size_t num_col = conc.shape(1);

    auto out = py::array_t<double>({num_rows, num_col});
    auto result = out.mutable_unchecked<2>();

    for (size_t i = 0; i < num_rows; ++i) {

        const size_t j_row_above = (i == 0) ? 0 : i - 1;
        const size_t j_row_below = (i + 1 < num_rows) ? i + 1 : num_rows - 1;

        for (size_t j = 0; j < num_col; ++j) {

            const size_t i_colum_left = (j == 0) ? 0 : j - 1;
            const size_t i_colum_right = (j + 1 < num_col) ? j + 1 : num_col - 1;

            result(i, j) = conc(j_row_above, j) + conc(j_row_below, j) + conc(i, i_colum_left) + conc(i, i_colum_right) - 4.0 * conc(i, j);
        }
    }

    return out;
}

PYBIND11_MODULE(laplacian_pybind, m) {
    m.doc() = "pybind11 backend";
    m.def("laplacian_pybind", &laplacian_pybind, "Compute the laplacian");
}
