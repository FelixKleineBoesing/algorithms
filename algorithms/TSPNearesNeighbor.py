"""
    Solves the Traveling Salesman Problem using dynamic programming
"""

from itertools import combinations
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def read_cities(path: str):
    with open("data/nn.txt", "r") as f:
        lines = f.readlines()
    cities = {}
    number_cities = lines.pop(0)
    for line in lines:
        id, x, y = [float(num) for num in line.split()]
        city = City(int(id), x, y)
        cities[int(id)] = (city)
    return(cities)


class City:

    def __init__(self, id: int, x: float, y: float):
        self.id = id
        self.x = x
        self.y = y


class TSPNearestNeighbor:

    def __init__(self, cities: dict, start_city_id: int = 1):
        """
        TSP Solver with Heuristic nearest neighbour
        :param cities:
        :param start_city:
        """
        self.cities  = cities
        self.start_city_id = start_city_id
        self.coords = np.array([[cities[c].id, cities[c].x, cities[c].y] for c in cities])
        self.mapping = {i: city for i, city in enumerate(cities)}
        self._mapping = {city: i for i, city in enumerate(cities)}

    def calculate_optimal_tour(self):
        start_city = self.cities[self.start_city_id]

        tour_length = 0
        coords = self.coords
        coords = np.delete(coords, (self._mapping[self.start_city_id]), axis=0)

        city = start_city
        while coords.shape[0] > 0:
            distances = np.sqrt(np.add(np.subtract(coords[:, 1], city.x)**2, np.subtract(coords[:, 2], city.y)**2))
            min_dist = np.min(distances)
            index = np.where(min_dist==distances)
            id = coords[index, 0][0][0]
            coords = np.delete(coords, (index), axis = 0)
            city = self.cities[int(id)]
            tour_length += min_dist

        tour_length += sqrt((city.x - start_city.x) **2 + (city.y - start_city.y) **2)
        return tour_length


if __name__== '__main__':
    cities = read_cities("data/nn.txt")
    tsp = TSPNearestNeighbor(cities, 1)
    print(tsp.calculate_optimal_tour())