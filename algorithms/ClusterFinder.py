from operator import attrgetter
import itertools

from algorithms.Helper import calculate_number_from_bits
from algorithms.UnionFinder import UnionFinder


class Graph:
    def __init__(self):
        self.graph = None
        self.edges = None
        self.vertices = None

    def read_from_file(self, path: str):
        '''
        load file for counting
        :param file: path to file
        :return: list with integers
        '''
        data = {}
        self.edges = []
        with open(path) as f:
            lines = f.readlines()
        del lines[0]
        for row in lines:
            from_, to_, weight = (int(val) for val in row.split())
            self.edges += [(from_, to_, weight)]
            if from_ not in data.keys():
                data[from_] = {to_: weight}
            else:
                data[from_].update({to_: weight})
            if to_ not in data.keys():
                data[to_] = {from_: weight}
            else:
                data[to_].update({from_: weight})
        self.graph = data
        self.vertices = list(self.graph.keys())

class BitGraph:

    def __init__(self):
        self.size = None
        self.number_bits = None
        self.graph = {}

    def read_from_file(self, path: str):
        assert type(path) == str
        with open(path, "r") as f:
            lines = f.readlines()
        self.size, self.number_bits = lines.pop(0).split()
        id = 1
        for line in lines:
            bits = line.split()
            bits = [int(bit) for bit in bits]
            number = calculate_number_from_bits(bits)
            if number in self.graph:
                self.graph[number] += [(id, bits)]
            else:
                self.graph[number] = [(id, bits)]
            id += 1


class BigKruskalClusterDetector:

    def __init__(self, graph: BitGraph):
        assert type(graph) == BitGraph
        self.graph = graph

    def get_number_clusters(self):
        pass



class KruskalClusterDetector:

    def  __init__(self, graph: Graph):
        assert type(graph) == Graph
        self.graph = graph

    def get_clusters(self, number_cluster: int):
        #sort by costs
        sorted_edges = sorted(self.graph.edges, key=lambda x: x[2])
        union_finder = UnionFinder(self.graph.vertices)
        searching = True
        i = 0
        while searching and i < len(sorted_edges)-1:
            edge = sorted_edges[i]
            i += 1
            # if number of clusters not reached and there are still unconnected  vertices
            if number_cluster != union_finder.number_unions and not union_finder.connected(edge[0], edge[1]):
                union_finder.union(edge[0], edge[1])
            if number_cluster == union_finder.number_unions and not union_finder.connected(edge[0], edge[1]):
                searching = False

        return edge[2]


if __name__=="__main__":
    graph = Graph()
    graph.read_from_file("data/clustering.txt")
    kruskal = KruskalClusterDetector(graph)
    print(kruskal.get_clusters(4))
    graph_big = BitGraph()
    graph_big.read_from_file("data/clustering_big.txt")
    kruskal_big = BigKruskalClusterDetector(graph_big)
    print(kruskal_big.get_number_clusters(4))