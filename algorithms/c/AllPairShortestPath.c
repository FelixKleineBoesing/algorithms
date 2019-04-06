#include <stdio.h>
#include <Python.h>
#include "calgorithms.h"

PyObject * add(PyObject *self, PyObject *args) {
	int num1, num2;
	char eq[20];

	if(!PyArg_ParseTuple(args, "ii", &num1, &num2))
		return NULL;

	sprintf(eq, "%d + %d", num1, num2);

	return Py_BuildValue("is", num1 + num2, eq);
}
