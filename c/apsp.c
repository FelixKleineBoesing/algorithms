#include "apsp.h"


double** apsp(double **dist) {
    int n = sizeof(dist) / sizeof(dist[0]);
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