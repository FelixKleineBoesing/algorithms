def load_file(file: str):
    '''
    load file for counting
    :param file: path to file
    :return: list with integers
    '''
    data = {}
    with open(file) as f:
        lines = f.readlines()
    for row in lines:
        row = row.split("\t")
        id = row[0]
        del row[0]
        data[int(id)] = [{"node": int(tuple.split(",")[0]), "length": int(tuple.split(",")[1])} for tuple in
                             row if "," in tuple]
    return data


class Dijkstra:

    def __init__(self, data: {}):
        assert type(data) == dict
        self.graph = data
        self.vertex_source = next(iter(self.graph.keys()))
        self.paths_shortest = None

    def calculate_dijkstra_shortest_path(self):
        # get source node
        src = self.vertex_source
        visited = []
        # init shortest paths, source with distance 0 and every other vertex with 1000000
        # tuple: (Distance, previous nodes)
        paths_shortest = {vtx: (1000000, []) for vtx in self.graph.keys()}
        paths_shortest[src] = (0, [])
        visited += [src]

        # while there are unvisited vertices
        while len(self.graph.keys()-visited) > 0:
            src = -1
            edge_minimum = ()
            for vtx in visited:
                # check every nodes distance that is connected with the vtx-node
                for edge in self.graph[vtx]:
                    if edge["node"] in visited:
                        # continue of node already visited
                        continue
                    if not edge_minimum or paths_shortest[vtx][0] + edge["length"] < edge_minimum[1]:
                        edge_minimum = (edge["node"], paths_shortest[vtx][0] + edge["length"])
                        # set new source for path
                        src = vtx
            paths_shortest[edge_minimum[0]] = (edge_minimum[1], paths_shortest[src][1] + [edge_minimum[0]])
            visited += [edge_minimum[0]]
        self.paths_shortest = paths_shortest
        return paths_shortest


if __name__ == '__main__':
    data = load_file("../data/dijkstraData.txt")
    dijkstra = Dijkstra(data)
    shortest_paths = dijkstra.calculate_dijkstra_shortest_path()
    vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    distances = []
    for vertex in vertices:
        distances += [str(shortest_paths[vertex][0])]

    print(",".join(distances))
