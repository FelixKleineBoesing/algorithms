from typing import Union
import abc
import heapq

class Leaf:

    def __init__(self, val: int, id: Union[int, str]):
        self.val = val
        self.id = id


class Tree:

    def __init__(self, left, right):
        self.val = left.val + right.val
        self.left = left
        self.right = right


class HuffmannEncoding:

    def __init__(self, path: str):
        self.path = path
        self.heap = Heap()
        self.tree = None

    def read_file(self):
        '''
        load file for counting
        :param file: path to file
        :return: list with integers
        '''
        with open(self.path) as f:
            lines = f.readlines()
        number_symbols = int(lines.pop(0))
        id = 1
        for row in lines:
            row = int(row)
            self.heap.insert((row, Leaf(row, id)))
            id += 1

    def build_tree(self):
        while len(self.heap) > 1:
            node_one = self.heap.pop()
            node_two = self.heap.pop()
            new_tree = Tree(node_one, node_two)
            self.heap.insert((new_tree.val, new_tree))
        self.tree = self.heap.pop()

    def get_max_length(self):
        '''
        :return:
        '''
        bits = self.search_binary_tree(self.tree, 1, "max")
        return bits

    def get_min_length(self):
        '''
        :return:
        '''
        bits = self.search_binary_tree(self.tree, 1, "min")
        return bits

    def search_binary_tree(self, tree, current_depth: int, depth: str = "max"):
        '''
        wrapper for tree searching
        :param tree:
        :param current_depth:
        :param depth:
        :return:
        '''
        index = 1 if depth == "max" else 0
        if isinstance(tree.left, Tree):
            depth_left = self.search_binary_tree(tree.left, current_depth + 1, depth)
        else:
            depth_left = current_depth
        if isinstance(tree.right, Tree):
            depth_right = self.search_binary_tree(tree.right, current_depth + 1, depth)
        else:
            depth_right = current_depth
        return sorted((depth_left, depth_right))[index]


class Heap():
    '''
    oop wrapper for heaq
    '''
    def __init__(self):
        self.data = []

    def insert(self, item: tuple):
        heapq.heappush(self.data, item)

    def pop(self):
        return heapq.heappop(self.data)[1]

    def __len__(self):
        return len(self.data)


if __name__=="__main__":
    huffman = HuffmannEncoding("data/huffmann.txt")
    huffman.read_file()
    huffman.build_tree()
    print(huffman.get_max_length())
    print(huffman.get_min_length())