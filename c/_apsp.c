#include <Python.h>
#include <numpy/arrayobject.h>
#include "apsp.h"

static char module_docstring[] =
    "This module provides an interface for calculating all pair shortest path using C.";
static char apsp_docstring[] =
    "Calculate the all pair shortest path of a given distance matrix";

static PyObject *apsp_apsp(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
    {"apsp", apsp_apsp, METH_VARARGS, apsp_docstring},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC PyInit__apsp(void)
{

    PyObject *module;
    static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "_apsp",
        module_docstring,
        -1,
        module_methods,
        NULL,
        NULL,
        NULL,
        NULL
    };
    module = PyModule_Create(&moduledef);
    if (!module) return NULL;

    /* Load `numpy` functionality. */
    import_array();

    return module;
}

static PyObject *apsp_apsp(PyObject *self, PyObject *args)
{
    PyObject *dist_obj;
    int n;
    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "Oi", &dist_obj, &n))
        return NULL;

    /* Interpret the input objects as numpy arrays. */
    PyObject *dist_array = PyArray_FROM_OTF(dist_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work,s throw an exception. */
    if (dist_array == NULL) {
        Py_XDECREF(dist_array);
        return NULL;
    }

    /* Get pointers to the data as C-types. */
    double *dist    = (double*)PyArray_DATA(dist_array);

    /* Call the external C function to compute the chi-squared. */
    double *value = apsp(dist, n);

    /* Clean up. */
    Py_DECREF(dist_array);

    /* Build the output tuple */
    PyObject *ret = Py_BuildValue("d", value);
    return ret;
}