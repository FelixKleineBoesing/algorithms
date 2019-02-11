import os, sys


def load_file(file):
    data = []
    with open(file) as f:
        lines = f.readlines()
    for row in lines:
        data += [int(row.replace("\n", ""))]
    return data


def count_inversions(arr: []):
    assert type(arr) == list, "type of arr must be list!"
    '''
    :param arr: list containing integers
    :return: number of inversions in given list
    '''
    k = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                k += 1
    return k


def merge_sort_inversions(arr: []):
    '''
    This function applies merge sort on the given list
    :param arr: unsorted list
    :return: sorted list and number of inversions
    '''
    if len(arr) == 1:
        return arr, 0
    else:
        # split array in halve
        a, b = arr[:int(len(arr)/2)], arr[int(len(arr)/2):]

        a, a_inv = merge_sort_inversions(a)
        b, b_inv = merge_sort_inversions(b)

        c = []
        i = 0
        j = 0
        inv = 0 + a_inv + b_inv
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
            inv += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inv

if __name__=="__main__":
    data = load_file("data/IntegerArray.txt")
    print(count_inversions(data))
    sorted_array, inversions = merge_sort_inversions(data)
    print(inversions)