from operator import attrgetter


def load_file(file: str):
    '''
    load file for counting
    :param file: path to file
    :return: list with integers
    '''
    data = {}
    with open(file) as f:
        lines = f.readlines()
    del lines[0]
    for row in lines:
        from_, to_, weight  = (int(val) for val in row.split())
        if from_ not in data.keys():
            data[from_] = {to_: weight}
        else:
            data[from_].update({to_: weight})
        if to_ not in data.keys():
            data[to_] = {from_: weight}
        else:
            data[to_].update({from_: weight})
    return data


class Kruskal:

    def  __init__(self, graph: dict):
        assert type(graph) == dict
        self.graph = graph

    def get_mst(self):
        pass


class ClusterFinder:

    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            self._num_vertices = int(file.readline())
            self._edges = []
            self._unique_vtx = set()
            for line in file:
                edge_from, edge_to, cost = line.split()
                self._edges.append(Edge(int(edge_from), int(edge_to), int(cost)))
                self._unique_vtx.add(int(edge_from))
                self._unique_vtx.add(int(edge_to))

    def find_clusters(self, count):
        sorted_edges = sorted(self._edges, key=attrgetter("cost"))
        uf = UnionFinder(list(self._unique_vtx))
        for index, edge in enumerate(sorted_edges):
            if count != uf.number_items and not uf.connected(edge.from_vertex, edge.to_vertex):
                uf.union(edge.from_vertex, edge.to_vertex)
            if uf.number_items == count and not uf.connected(edge.from_vertex, edge.to_vertex):
                return edge.cost


class Edge:
    def __init__(self, edge_from, edge_to, cost):
        self.from_vertex = edge_from
        self.to_vertex = edge_to
        self.cost = cost


class UnionFinder:

    def __init__(self, ids_vtx: list):
        '''
        IMplements special data sctructure union find
        :param number_items: number of items to hold. MUst be larger than One.
        '''
        assert type(ids_vtx) == list
        assert len(ids_vtx) > 1
        self.ids_vtx = ids_vtx
        self.number_items = len(ids_vtx)
        # original number items
        self._number_items = self.number_items
        self._union_find = {vtx : (vtx, 0) for vtx in self.ids_vtx}

    def find(self, item):
        """
        find parent of item
        :param item:
        :return: the parent
        """
        assert item in self.ids_vtx
        parent = self._get_parent(item)
        prev = item
        while self._union_find[parent][0] != parent:
            self._union_find[prev] = self._union_find[parent][0], self._union_find[prev][1]
            prev = parent
            parent = self._get_parent(parent)
        return parent

    def connected(self, vtx_one: int, vtx_two: int):
        """
        checks if first  and second vertex are connected
        :param vtx_one: first vertex
        :param vtx_two: second vertex
        :return: bool, whether both are connected or  not
        """
        assert vtx_two in self.ids_vtx
        assert vtx_one in self.ids_vtx
        return self.find(vtx_one) == self.find(vtx_two)

    def union(self, first, second):
        """
        Unions <first> with <second> item
        :param first: the first item to be connected
        :param second: the second item to be connected
        :return: None
        """
        if not (1, 1) <= (first, second) <= (self._number_items, self._number_items):
            raise ValueError("Items {}, {} should be in the range [1..{}]".format(first, second, self._number_items))
        first_parent = self.find(first)
        second_parent = self.find(second)
        if first_parent == second_parent:
            return
        self.number_items -= 1
        first_rank = self._union_find[first_parent][1]
        second_rank = self._union_find[second_parent][1]

        if first_rank > second_rank:
            self._union_find[second_parent] = self._union_find[first_parent][0], self._union_find[second_parent][1]
        elif second_rank > first_rank:
            self._union_find[first_parent] = self._union_find[second_parent][0], self._union_find[first_parent][1]
        else:
            self._union_find[second_parent] = self._union_find[first_parent]
            self._union_find[first_parent] = (first_parent, self._union_find[first_parent][1] + 1)

    def _get_parent(self, item):
        node, node_range = self._union_find[item]
        return node




if __name__=="__main__":
    cluster_finder = ClusterFinder("data/clustering.txt")
    print(cluster_finder.find_clusters(4))
    graph = load_file("../data/clustering.txt")
    kruskal = Kruskal(graph)
    kruskal.get_mst()