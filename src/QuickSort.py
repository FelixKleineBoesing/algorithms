import copy


def load_file(file):
    data = []
    with open(file) as f:
        lines = f.readlines()
    for row in lines:
        data += [int(row.replace("\n", ""))]
    return data


def partition(arr, left, right):
    pivot_element = arr[left]
    index_i = left + 1

    for index_j in range(index_i, right + 1):
        if arr[index_j] < pivot_element:
            arr[index_j], arr[index_i] = arr[index_i], arr[index_j]
            index_i += 1

    arr[index_i - 1], arr[left] = arr[left], arr[index_i - 1]
    return index_i - 1


def create_pivot(arr, left, right, pivot_method):
    pivot_index = left
    middle, median = None, None
    array_length = len(arr[left:right + 1])

    if pivot_method in ("last", "end"):
        pivot_index = right
    elif pivot_method in ("median", "middle"):
        if array_length > 2:
            if array_length % 2 == 0:
                middle = left + (int(round(array_length / 2.0))-1)
            else:
                middle = left + (int(array_length / 2.0))
            list = [arr[left], arr[middle], arr[right]]
            median = sorted(list)[1]
        elif array_length == 2:
            list = [arr[left], arr[left], arr[right]]
            median = sorted(list)[1]
        pivot_index = arr.index(median)

    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    return


def quick_sort(arr, left=0, right=None, pivot = "first"):
    assert pivot in ["first", "last", "median"], "pivot method must be one of first, last or median"
    # init counts
    count_all = 0
    count_lhs = 0
    count_rhs = 0

    if right is None:
        right = len(arr) - 1

    if len(arr[left:(right+1)]) > 1:
        create_pivot(arr, left, right, pivot)
        count_all = len(arr[left:right])
        ix = partition(arr, left, right)
        if ix > left:
            count_lhs = quick_sort(arr, left, ix - 1, pivot)
        if right > ix:
            count_rhs = quick_sort(arr, ix + 1, right, pivot)
    count_all += count_lhs + count_rhs
    return count_all

def main():

    file = "data/QuickSort.txt"
    data = load_file(file)
    # make deepcopy to avoid accidently changing list values
    array_to_count1 = copy.deepcopy(data)
    array_to_count2 = copy.deepcopy(data)
    array_to_count3 = copy.deepcopy(data)

    comparisons_pivot_first = quick_sort(array_to_count1, pivot="first")
    print(comparisons_pivot_first)
    comparisons_pivot_last = quick_sort(array_to_count2, pivot = "last")
    print(comparisons_pivot_last)
    comparisons_pivot_median = quick_sort(array_to_count3 , pivot = "median")
    print(comparisons_pivot_median)

if __name__=="__main__":
    main()
