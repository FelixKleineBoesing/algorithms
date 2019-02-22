def load_file(file: str):
    '''
    load file for counting
    :param file: path to file
    :return: list with integers
    '''
    data = []
    with open(file) as f:
        lines = f.readlines()
    for row in lines:
        data += [row.split()]
    return data

class SCC:

    def __init__(self, data: [[]]):
        assert type(data) == list, "type of data must be list!"
        self.data = data
        self.graph = {}
        self.sizes = {}
        self.completed_vertices = None


    def construct_graph(self):
        for con in self.data:
            start, end = int(con[0]), int(con[1])
            if start in self.graph.keys():
                self.graph[start] += [end]
            else:
                self.graph[start] = [end]
            if end in self.graph.keys():
                self.graph[end] += [-start]
            else:
                self.graph[end] = [-start]

    def calculate_scc(self):
        vertices_visited, vertices_completed = [], []

        for vertex in self.graph.keys():
            if vertex in vertices_visited:
                continue
            vertices_con = [vertex]
            while len(vertices_con) > 0:
                a = vertices_con[-1]
                if a not in vertices_visited:
                    vertices_visited += [a]
                    # neighbors
                    neighbs = [-edge for edge in self.graph[a] if edge < 0]
                    for neighb in neighbs:
                        if neighb not in vertices_visited:
                            vertices_con += [neighb]
                else:
                    del vertices_con[-1]
                    if a not in vertices_completed:
                        vertices_completed += [a]
        self.completed_vertices = vertices_completed

        # again, now in reverse
        vertices_visited = []
        for verc in reversed(self.completed_vertices):
            if verc in vertices_visited:
                continue
            vertices_con = [verc]
            n = 0
            while len(vertices_con) > 0:
                a = vertices_con[-1]
                if a not in vertices_visited:
                    n += 1
                    vertices_visited += [a]
                    neighbs = (edge for edge in self.graph[a] if edge > 0)
                    for neighb in neighbs:
                        if neighb not in vertices_visited:
                            vertices_con += [neighb]
            self.sizes[verc] = n

    def get_top_sizes(self, top: int = 5):
        values = self.sizes.values()
        return values.sort()[0:top]

if __name__ == "__main__":
    data = load_file("data/SCC.txt")
    scc = SCC(data)
    scc.construct_graph()
    scc.calculate_scc()
    print(scc.get_top_sizes(5))
    expected_sccs = [434821, 968, 459, 313, 211]