#include "apsp.h"
#include <stdio.h>

double* apsp(double *dist, int n) {
    /*printf("kjhdglhn");


    sprintf(str, "%f",  *((dist+0*n) + 1));
    */
    char str[12];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (*((dist+i*n) + j) > (*((dist+i*n) + k) + *((dist+k*n) + j))) {
                    system(sprintf(str, "%f",  *((dist+i*n) + j)));
                    *((dist+i*n) + j) = (*((dist+i*n) + k) + *((dist+k*n) + j));
                }
            }
        }
    }

    return dist;
}

/*
double** apsp(double **dist) {
    printf("kjhdglhn");
    int sizeAll = sizeof(**dist);
    char str[12];
    sprintf(str, "%d", sizeAll);
    int sizeAlone = sizeof(dist[0][0]);
    sprintf(str, "%d", sizeAlone);


    int n = sizeof(dist) / sizeof(dist[0]);
    sprintf(str, "%d", n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (dist[i][j] > (dist[i][k] + dist[k][j])) {
                    dist[i][j] = (dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    return dist;
}

*/