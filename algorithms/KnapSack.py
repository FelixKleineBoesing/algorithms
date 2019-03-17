import sys



class Item:

    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight


class Knapsack:

    def __init__(self, path: str):
        self.path = path
        self.value = 0
        self._cache = {}
        self.read_file()

    def read_file(self):
        with open(self.path) as f:
            lines = f.readlines()
        self._weight, item_count = (int(num) for num in lines.pop(0).split())
        self._items = [None] * item_count
        ix = 0
        for row in lines:
            value, weight = (int(num) for num in row.split())
            self._items[ix] = Item(value, weight)
            ix += 1

    def maximize_value(self):
        self.value = self._compute_value(self._weight, len(self._items) - 1)

    def _compute_value(self, weight, index):
        if weight == 0 or index == -1:
            return 0
        item = self._items[index]
        if item.weight > weight:
            if (weight, index - 1) not in self._cache:
                self._cache[(weight, index - 1)] = self._compute_value(weight, index - 1)
            return self._cache[(weight, index - 1)]
        else:
            if (weight - item.weight, index - 1) not in self._cache:
                self._cache[(weight - item.weight, index - 1)] = self._compute_value(weight - item.weight, index - 1)
            sol_with_item = item.value + self._cache[(weight - item.weight, index - 1)]
            if (weight, index - 1) not in self._cache:
                self._cache[(weight, index - 1)] = self._compute_value(weight, index - 1)
            sol_without_item = self._cache[(weight, index - 1)]
            return max(sol_with_item, sol_without_item )

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    knapsack = Knapsack("data/knapsack1.txt")
    knapsack.maximize_value()
    print(knapsack.value)

    knapsack_big = Knapsack("data/knapsack_big.txt")
    knapsack_big.maximize_value()
    print(knapsack_big.value)