import numpy as np


class MWIST:

    def __init__(self, path: str):
        self.path = path
        self.data = None
        self.read_file()

    def read_file(self):
        '''
        load file for counting
        :param file: path to file
        :return: Nothing
        '''
        with open(self.path) as f:
            lines = f.readlines()
        number_vertices = int(lines.pop(0))
        # np array because aggregation stats like max are easier to calculate
        self.data = np.array([int(num) for num in lines])

    def find_maximum_weight_graph(self):
        vertices = {-1: 0, 0: 0, 1: self.data[0]}
        for i in range(1, len(self.data)):
            vertices[i] = np.long(max(vertices[i - 1], vertices[i - 2] + self.data[i - 1]))
        maximum_weight_graph = set()
        position = len(self.data)
        while position >= 1:
            if vertices[position - 1] >= (vertices[position - 2] + self.data[position - 1]):
                position = position - 1
            else:
                maximum_weight_graph.add(position)
                position = position - 2
        self.maximum_weight_graph = maximum_weight_graph
        return maximum_weight_graph

if __name__=="__main__":
    assigment_vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    mwis = MWIST("data/mwis.txt")
    mwis_graph = mwis.find_maximum_weight_graph()
    vertix_check = [str(int(vtx in mwis_graph)) for vtx in assigment_vertices]
    print("".join(vertix_check))