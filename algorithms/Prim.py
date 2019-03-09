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
        visited = set()
        queue = set()
        visited.add(1)
        queue.add((1,0))
        while len(unvisited) > 0:
            vtx = extract_min(queue)
            self.cost += vtx[1]
            unvisited.remove(vtx[0])
            visited.add(vtx[0])
            for edge in self.graph[vtx[0]].keys():
                if edge in unvisited:
                    update_set(queue, (edge, self.graph[vtx[0]][edge]))


def extract_min(edge_cost: set):
    for ix, a in enumerate(edge_cost):
        if ix == 0:
            min = a
        else:
            if a[1] < min[1]:
                min = a
    edge_cost.remove(min)
    return min


def update_set(edge_cost: set, edge: tuple):
    found = False
    for tup in edge_cost:
        if tup[0] == edge[0]:
            found = True
            if tup[1] > edge[1]:
                edge_cost.remove(tup)
                edge_cost.add(edge)

    if not found:
        edge_cost.add(edge)


if __name__ == "__main__":
    data = load_file("data/edges.txt")
    prim = Prim(data)
    prim.calculate_minimum_spanning_tree()
    print(prim.cost)
    print("Bla")