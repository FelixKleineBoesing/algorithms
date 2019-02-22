import heapq
import abc

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
        data += [int(row.replace("\n", ""))]
    return data


class Heap(abc.ABC):
    '''
    oop abc wrapper for heapq
    '''
    def __init__(self):
        self.data = []

    @abc.abstractmethod
    def insert(self, value: int):
        pass

    def pop(self):
        return heapq.heappop(self.data)[1]

    def get_first_value(self):
        return self.data[0][1]


class MaxHeap(Heap):

    def insert(self, value: int):
        heapq.heappush(self.data, (value, value))


class MinHeap(Heap):

    def insert(self, value: int):
        heapq.heappush(self.data, (-value, value))


class MedianMaintenance:

    def __init__(self, data: []):
        self.data = data
        self.median_sum = 0
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def sum_medians(self):
        for number in self.data:
            if len(self.min_heap.data) == 0:
                self.min_heap.insert(number)
                self.median_sum += number
                continue
            if number <= self.min_heap.get_first_value():
                self.min_heap.insert(number)
            else:
                self.max_heap.insert(number)
            if (len(self.min_heap.data) - len(self.max_heap.data)) >= 2:
                self.max_heap.insert(self.min_heap.pop())
            elif (len(self.max_heap.data) - len(self.min_heap.data)) >= 2:
                self.min_heap.insert(self.max_heap.pop())
            if len(self.min_heap.data) >= len(self.max_heap.data):
                self.median_sum += self.min_heap.get_first_value()
            else:
                self.median_sum += self.max_heap.get_first_value()

        return self.median_sum % len(self.data)



if __name__=="__main__":
    data = load_file("data/Median.txt")
    median = MedianMaintenance(data)
    print(median.sum_medians())