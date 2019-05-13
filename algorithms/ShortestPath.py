import numpy as np
from algorithms._apsp import apsp


def build_dist_matrix_from_file(path: str):
    with open(path) as f:
        lines = f.readlines()
    number_vertices, _ = (int(num) for num in lines.pop(0).split())
    distance_matrix = np.full((number_vertices, number_vertices), np.inf)
    for line in lines:
        values = [int(num) for num in line.split()]
        distance_matrix[values[0] - 1, values[1] - 1] = values[2]
    for i in range(distance_matrix.shape[0]):
        distance_matrix[i, i] = 0
    return distance_matrix


class FloydWarshall:
    """
    Algorithm for the calculation of all pair shortest paths with dynamic programming
    """

    def __init__(self, dist: np.ndarray):
        assert isinstance(dist, np.ndarray), "distance matrix must be of type ndarray!"
        assert len(dist.shape) == 2, "Must be a 2D array!"
        assert dist.shape[0] == dist.shape[1], "2D array must be cubic!"
        self.dist = dist

    def find_shortest_paths(self):
        for k in range(self.dist.shape[0]):
            for i in range(self.dist.shape[0]):
                for j in range(self.dist.shape[0]):
                    if self.dist[i, j] > (self.dist[i, k] + self.dist[k, j]):
                        self.dist[i, j] = (self.dist[i, k] + self.dist[k, j])

        if np.any(np.diagonal(self.dist) < 0):
            print(np.amin(self.dist))
            print("negative cost cycle")
        else:
            print(np.amin(self.dist))

    def find_shortest_paths_c(self):
        apsp(self.dist, self.dist.shape[0])

        if np.any(np.diagonal(self.dist) < 0):
            print(np.amin(self.dist))
            print("negative cost cycle")
        else:
            print(np.amin(self.dist))

if __name__ == "__main__":
    g1 = build_dist_matrix_from_file("../data/g1.txt")
    g2 = build_dist_matrix_from_file("../data/g2.txt")
    g3 = build_dist_matrix_from_file("../data/g3.txt")
    FloydWarshall(g1).find_shortest_paths_c()
    FloydWarshall(g2).find_shortest_paths_c()
    FloydWarshall(g3).find_shortest_paths_c()