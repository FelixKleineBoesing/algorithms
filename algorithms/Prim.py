import numpy as np

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


class Prim:
    def __init__(self, graph: dict):
        self.graph = graph
        self.cost = 0

    def calculate_minimum_spanning_tree(self):
        unvisited = set(self.graph.keys())
        # begin with vertex one
        values = {vtx: np.Inf for vtx in unvisited}
        parents = {vtx: 0 for vtx in unvisited}
        values[0] = 0
        while len(unvisited) > 0:
            vtx = self._extract_min(X)
            for edge in self.graph[vtx[0]].keys():
                if edge in unvisited and self.graph[vtx][edge] < values[edge]:
                    parents[edge] = vtx[0]
                    values[edge] =

    def _extract_min(self, edge_cost: set):
        for ix, a in enumerate(edge_cost):
            if ix == 0:
                min = a
            else:
                if a[1] < min[1]:
                    min = a
        return edge_cost.remove(min)


if __name__ == "__main__":
    data = load_file("../data/edges.txt")
    prim = Prim(data)
    prim.calculate_minimum_spanning_tree()
    print("Bla")