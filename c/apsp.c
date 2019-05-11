#include "apsp.h"
#include <stdio.h>

double* apsp(double *dist, int n) {
    printf("kjhdglhn");
    float test;
    char str[12];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                test = (*((dist+i*n) + k) + *((dist+k*n) + j));
                sprintf(str, "test6%f", test);
                printf("test5");
                if (*((dist+i*n) + j) > (*((dist+i*n) + k) + *((dist+k*n) + j))) {
                    printf("test4\n");
                    *((dist+i*n) + j) = (*((dist+i*n) + k) + *((dist+k*n) + j));
                }
            }
        }
    }

    return dist;
}
