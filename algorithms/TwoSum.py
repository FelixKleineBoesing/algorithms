from algorithms.QuickSort import quick_sort
import bisect

def load_file(file: str):
    '''
    load file for counting
    :param file: path to file
    :return: list with integers
    '''
    # this time use set instead of list to prevent the addition of duplicates
    data = set()
    with open(file) as f:
        lines = f.readlines()
    for row in lines:
        data.add(int(row.replace("\n", "")))
    return data


class TwoSum:

    def __init__(self, data: []):
        assert type(data) == set, "Data must be type set!"

        self.data = sorted(data)

    def return_subset(self):
        # use set here as well to prevent duplicates
        subset = set()
        for item in self.data:
            upper_bound = bisect.bisect_right(self.data, 10000 - item)
            lower_bound = bisect.bisect_left(self.data, -10000 - item)
            for item_subset in self.data[lower_bound:upper_bound]:
                if item_subset != item:
                    subset.add(item + item_subset)
        return subset


if __name__=="__main__":
    data = load_file("data/algo1-programming_prob-2sum.txt")
    two_sum = TwoSum(data)
    subset = two_sum.return_subset()
    print(len(subset))