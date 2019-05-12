#include "apsp.h"
#include <stdio.h>

double* apsp(double *dist, int n) {

    char str[12];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (dist[i*n + j] > (dist[i*n + k] + dist[k*n + j])) {
                    dist[i*n + j] = (dist[i*n + k] + dist[k*n + j]);
                }
            }
        }
    }

    return dist;
}
