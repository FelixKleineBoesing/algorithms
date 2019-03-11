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
        self.nodes = []

    def read_from_file(self, path: str):
        assert type(path) == str
        with open(path, "r") as f:
            lines = f.readlines()[:2000]
        self.size, self.number_bits = [int(val) for val in lines.pop(0).split()]
        id = 1
        for line in lines:
            self.nodes += [id]
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
        self.union_finder = UnionFinder(self.graph.nodes)

    def get_number_clusters(self):
        distances_all = [2**bit for bit in range(self.graph.number_bits)]
        distances_all += [-dist for dist in distances_all]
        distances_all += [combi[0] + combi[1] for combi in itertools.combinations(distances_all, 2)]
        distances_all += [0]
        # because exercise says there must be max 2 diff bits per cluster (zero, one, towo)
        unions_zero, unions_one, unions_two = [], [], []
        for distance in distances_all:
            for vtx in self.graph.graph.keys():
                if (vtx + distance) in self.graph.graph.keys():
                    for node_from, bits_from in self.graph.graph[vtx]:
                        for node_to, bits_to in self.graph.graph[vtx + distance]:
                            if self._hamming(bits_from, bits_to) == 0:
                                unions_zero.append((node_from, node_to))
                            elif self._hamming(bits_from, bits_to) == 1:
                                unions_one.append((node_from, node_to))
                            elif self._hamming(bits_from, bits_to) == 2:
                                unions_two.append((node_from, node_to))
        self._make_unions(unions_zero)
        self._make_unions(unions_one)
        self._make_unions(unions_two)
        return self.union_finder.number_unions

    def _hamming(self, bits_from, bits_to):
        hamming = 0
        for bit_from,  bit_to in zip(bits_from, bits_to):
            if bit_from != bit_to:
                hamming += 1
        return hamming

    def _make_unions(self, unions: list):
        for node_from, node_to in unions:
            if not self.union_finder.connected(node_from, node_to):
                self.union_finder.union(node_from, node_to)

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
    print(kruskal_big.get_number_clusters())