#include "apsp.h"
#include <stdio.h>

double* apsp(double *dist, int n) {
    printf("kjhdglhn\n");
    float test;
    char str[12];

      // 2d array
  int num[3][4] = {
    {1, 2,  3,  4},
    {5, 6,  7,  8},
    {9, 10, 11, 12}
  };

  int
    ROWS = 3,
    COLS = 4,
    i, j;

  // pointer
  int *ptr = &num[0][0];

  // print the element of the array via pointer ptr
  for (i = 0; i < ROWS; i++) {
    for (j = 0; j < COLS; j++) {
      printf("%d ", *(ptr + i * COLS + j));
    }
    printf("\n");
  }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                test = *((dist + i*n) + j);
                printf("%d\n", test);
                printf("test5\n");
                if (*((dist+i*n) + j) > (*((dist+i*n) + k) + *((dist+k*n) + j))) {
                    printf("test4\n");
                    *((dist+i*n) + j) = (*((dist+i*n) + k) + *((dist+k*n) + j));
                }
            }
        }
    }

    return dist;
}
