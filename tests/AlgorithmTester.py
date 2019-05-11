from algorithms._apsp import apsp
import numpy as np

def test_c_apsp():
    dist = np.array([[0,np.Inf,3.4], [2.2,0,4.5], [6.6,np.Inf,0]])
    print(dist)
    apsp(dist, 3)
    print(dist)

    with open("../../algorithms/data/g3.txt") as f:
        lines = f.readlines()
    number_vertices, _ = (int(num) for num in lines.pop(0).split())
    distance_matrix = np.full((number_vertices, number_vertices), np.inf)
    for line in lines:
        values = [int(num) for num in line.split()]
        distance_matrix[values[0] - 1, values[1] - 1] = values[2]
    for i in range(distance_matrix.shape[0]):
        distance_matrix[i, i] = 0
    dist = distance_matrix
    print(dist)
    new_dist = apsp(dist, dist.shape[0])
    print(dist)
    print(new_dist)


if __name__=="__main__":
    print(test_c_apsp())