#include "apsp.h"


double* apsp(double* arr) {
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (arr[i][j] > (arr[i][k] + arr[k][j])) {
                    arr[i][j] = (arr[i][k] + arr[k][j]);
                }
            }
        }
    }
    return arr;
}