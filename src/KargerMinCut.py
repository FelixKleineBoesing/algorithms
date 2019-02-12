from random import randint
import copy


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

class KargerMinCut:

    def __init__(self, matr: [[]]):
        assert isinstance(matr, list), "data must be of type list"
        assert len(matr) > 2, "data must have at least 2 edges"
        self.matr = matr
        self.num_min_cut = None

    def karger_min_cut(self):
        '''
        :return: minimum number of vertices in this run
        '''
        matr = copy.deepcopy(self.matr)
        while len(matr) > 2:
            # random edge
            edge_f = randint(0, len(matr) - 1)
            #random edge connected with edge_f
            edge_s = randint(1, len(matr[edge_f]) - 1)

            # get headnodes from matrice
            head_nodes = [arr[0] for arr in matr]

            # get index of edge
            ix = head_nodes.index(matr[edge_f][edge_s])
            matr[edge_f] += matr[ix][1:]

            for edge in matr[ix][1:]:
                ix_edge = head_nodes.index(edge)
                for i in range(len(data[ix_edge])):
                    if data[ix_edge][i] == data[ix][0]:
                        matr[ix_edge][i] = data[edge_f][0]

            matr[edge_f][1:] = [x for x in matr[edge_f][1:] if x != matr[edge_f][0]]
            matr.remove(matr[ix])
        num = len(matr[0][1:])
        self.num_min_cut = num
        return num


if __name__=="__main__":
    data = load_file("../data/kargerMinCut.txt")
    results = []
    for i in range(100):
        karger = KargerMinCut(data)
        results += [karger.karger_min_cut()]
    count = {}
    for item in results:
        if item in count.keys():
            count[item] += 1
        else:
            count[item] = 1
    print(count)
    print(results)
