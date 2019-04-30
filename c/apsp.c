#include "apsp.h"

double apsp(double m, double b, double *x, double *y, double *yerr, int N) {
    int n;
    double result = 0.0, diff;

    for (n = 0; n < N; n++) {
        diff = (y[n] - (m * x[n] + b)) / yerr[n];
        result += diff * diff;
    }

    return result;
};

double apsp(float *arr, int number_vtx) {

    for (i = 0; i < number_vtx; i++) {
        for (j = 0; j < number_vtx; j++) {
            for (k = 0; k < number_vtx; k++) {
                if (arr[i, j] > (arr[i, k] + arr[k, j])) {
                    arr[i, j] =arr[i, k] + arr[k, j];
                }
            }
        }
    }
    return arr_out
}