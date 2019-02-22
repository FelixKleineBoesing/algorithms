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
        data += [int(row.replace("\n", ""))]
    return data


def sort(arr, left, right):
    '''

    :param arr: unsorted array
    :param left: left border
    :param right: right border
    :return:
    '''
    pivot_element = arr[left]
    ix_i = left + 1
    # iterate over given array and switch places if element of
    for ix_j in range(ix_i, right + 1):
        if arr[ix_j] < pivot_element:
            arr[ix_j], arr[ix_i] = arr[ix_i], arr[ix_j]
            ix_i += 1

    arr[ix_i - 1], arr[left] = arr[left], arr[ix_i - 1]
    return ix_i - 1


def switch_pivot(arr, left, right, pivot):
    '''
    switch position of pivot element with left element
    :param arr: unsorted array
    :param left: left border
    :param right: rigth border
    :param pivot: pivot element
    :return:
    '''
    middle, median = None, None
    arr_len = len(arr[left:right + 1])
    if pivot == "median":
        if arr_len > 2:
            if arr_len % 2 == 0:
                middle = left + (int(round(arr_len / 2))-1)
            else:
                middle = left + (int(arr_len / 2))
            choice_list = (arr[left], arr[middle], arr[right])
            median = sorted(choice_list)[1]
        elif arr_len == 2:
            choice_list = (arr[left], arr[left], arr[right])
            median = sorted(choice_list)[1]
        ix = arr.index(median)
    elif pivot == "first":
        ix = right
    else:
        ix = left
    arr[left], arr[ix] = arr[ix], arr[left]


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
        switch_pivot(arr, left, right, pivot)
        count_all = len(arr[left:right])
        ix = sort(arr, left, right)
        if right > ix:
            count_rhs = quick_sort(arr, ix + 1, right, pivot)
        if left < ix:
            count_lhs = quick_sort(arr, left, ix - 1, pivot)

    count_all += count_lhs + count_rhs
    return count_all


if __name__=="__main__":
    data = load_file("../data/QuickSort.txt")
    # make deepcopy to avoid changing list values per reference
    comparisons_pivot_first = quick_sort(copy.deepcopy(data), pivot="first")
    print(comparisons_pivot_first)
    comparisons_pivot_last = quick_sort(copy.deepcopy(data), pivot="last")
    print(comparisons_pivot_last)
    comparisons_pivot_median = quick_sort(copy.deepcopy(data), pivot="median")
    print(comparisons_pivot_median)

