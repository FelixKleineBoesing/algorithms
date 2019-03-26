import numpy as np


class FloydWarshall:

    def __init__(self, path: str):
        with open(path) as f:
            lines = f.readlines()
        number_vertices, _ = (int(num) for num in lines.pop(0).split())
        distance_matrix = np.full((number_vertices, number_vertices), np.inf)
        for line in lines:
            values = [int(num) for num in line.split()]
            distance_matrix[values[0]-1, values[1]-1] = values[2]
        for i in range(distance_matrix.shape[0]):
            distance_matrix[i, i] = 0
        self.dist = distance_matrix

    def find_shortest_paths(self):
        for k in range(self.dist.shape[0]):
            for i in range(self.dist.shape[0]):
                for j in range(self.dist.shape[0]):
                    if self.dist[i,j] > (self.dist[i,k] + self.dist[k,j]):
                        self.dist[i,j] = (self.dist[i,k] + self.dist[k,j])

        if np.any(np.diagonal(self.dist) < 0):
            print(np.amin(self.dist))
            print("negative cost cycle")
        else:
            print(np.amin(self.dist))


if __name__ == "__main__":
    FloydWarshall("data/g1.txt").find_shortest_paths()
    FloydWarshall("data/g2.txt").find_shortest_paths()
    FloydWarshall("data/g3.txt").find_shortest_paths()