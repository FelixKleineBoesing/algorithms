import copy


def load_file(file):
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


def partition(arr, left, right):
    pivot_element = arr[left]
    index_i = left + 1

    for index_j in range(index_i, right + 1):
        if arr[index_j] < pivot_element:
            arr[index_j], arr[index_i] = arr[index_i], arr[index_j]
            index_i += 1

    arr[index_i - 1], arr[left] = arr[left], arr[index_i - 1]
    return index_i - 1

def create_pivot(arr, left, right, pivot):
    middle, median = None, None
    array_length = len(arr[left:right + 1])
    if pivot == "end":
        pivot_index = right
    elif pivot == "median":
        if array_length > 2:
            if array_length % 2 == 0:
                middle = left + (int(round(array_length / 2))-1)
            else:
                middle = left + (int(array_length / 2))
            choice_list = [arr[left], arr[middle], arr[right]]
            median = sorted(choice_list)[1]
        elif array_length == 2:
            choice_list = [arr[left], arr[left], arr[right]]
            median = sorted(choice_list)[1]
        pivot_index = arr.index(median)
    else:
        pivot_index = left
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    return


def quick_sort(arr: list, left: int = None, right: int = None, pivot: str="first"):
    assert type(arr) == list, "arr must be of type list!"
    assert type(left) == int or left is None, "left must be of type int!"
    assert type(right) == int or right is None, "right must be of type int!"
    assert type(pivot) == str, "pivot must be of type str!"
    assert pivot in ["first", "last", "median"], "pivot method must be one of first, last or median"
    '''
    quick sort given array
    :param arr: unsorted list
    :param left: index of left border
    :param right: index of right border
    :param pivot: choice of pivot element
    :return: list with integers
    '''
    # init counts and borders
    count_all, count_lhs, count_rhs = (0, 0, 0)
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right

    if len(arr[left:(right+1)]) > 1:
        # changes pivot per reference in list
        create_pivot(arr, left, right, pivot)
        count_all = len(arr[left:right])
        ix = partition(arr, left, right)
        if ix > left:
            count_lhs = quick_sort(arr, left, ix - 1, pivot)
        if right > ix:
            count_rhs = quick_sort(arr, ix + 1, right, pivot)
    count_all += count_lhs + count_rhs
    return count_all

if __name__=="__main__":
    data = load_file("data/QuickSort.txt")
    # make deepcopy to avoid changing list values per reference
    comparisons_pivot_first = quick_sort(copy.deepcopy(data), pivot="first")
    print(comparisons_pivot_first)
    comparisons_pivot_last = quick_sort(copy.deepcopy(data), pivot="last")
    print(comparisons_pivot_last)
    comparisons_pivot_median = quick_sort(copy.deepcopy(data), pivot="median")
    print(comparisons_pivot_median)

