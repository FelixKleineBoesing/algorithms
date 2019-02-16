from ast import literal_eval

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

    def construct_graph(self):
        pass

    def calculate_dijkstra_shortest_path(self):

        src = self.vertex_source
        visited = []

        paths_shortest = {vtx: (9999999999, []) for vtx in self.graph.keys()}
        paths_shortest[src] = (0, [])
        visited += [src]

        while len(self.graph.keys()-visited) > 0:
            src = -1
            edge_minimum = ()
            for vtx in visited:
                for edge in self.graph[vtx]:
                    if edge["node"] in visited:
                        continue
                    if not edge_minimum or paths_shortest[vtx][0] + edge["length"] < edge_minimum[1]:
                        edge_minimum = (edge["node"], paths_shortest[vtx][0] + edge["length"])
                        src = vtx
            paths_shortest[edge_minimum[0]] = (edge_minimum[1], paths_shortest[src][1] + [edge_minimum[0]])
            visited += [edge_minimum[0]]
        return paths_shortest


if __name__ == '__main__':
    data = load_file("data/dijkstraData.txt")
    dijkstra = Dijkstra(data)
    dijkstra.construct_graph()
    shortest_paths = dijkstra.calculate_dijkstra_shortest_path()
    actual = {vertex: distance[0] for (vertex, distance) in shortest_paths.items()}
    print(actual[7])
    print(actual[37])
    print(actual[59])
    print(actual[82])
    print(actual[99])
    print(actual[115])
    print(actual[133])
    print(actual[165])
    print(actual[188])
    print(actual[197])
