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

    def __init__(self, data: [[]]):
        assert type(data) == list
        self.data = data
        self.graph = {}
        self.vertex_source = None

    def construct_graph(self):
        pass

    def calculate_dijkstra_shortets_path(self):
        pass

if __name__ == '__main__':
    data = load_file("data/dijkstraData.txt")
    dijkstra = Dijkstra(data)
    dijkstra.construct_graph()
    shortest_paths = dijkstra.calculate_dijkstra_shortets_path()
