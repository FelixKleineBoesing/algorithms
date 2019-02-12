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


def count_inversions(arr: []):
    assert isinstance(arr, list), "type of arr must be list!"
    '''
    :param arr: list containing integers
    :return: number of inversions in given list
    '''
    inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv


def merge_sort(arr: []):
    assert isinstance(arr, list), "type of arr must be list!"
    '''
    This function applies merge sort on the given list
    :param arr: unsorted list
    :return: sorted list and number of inversions
    '''
    if len(arr) > 1:
        # split array in halve
        arr_f, arr_s = arr[:int(len(arr)/2)], arr[int(len(arr)/2):]

        arr_f, inv_f = merge_sort(arr_f)
        arr_s, inv_s = merge_sort(arr_s)

        arr_merged = []
        i, j = (0, 0)
        inv = 0 + inv_f + inv_s
        while i < len(arr_f) and j < len(arr_s):
            if arr_f[i] <= arr_s[j]:
                arr_merged += [arr_f[i]]
                i += 1
            else:
                arr_merged += [arr_s[j]]
                j += 1
                inv += (len(arr_s)-i)
        arr_merged += arr_f[i:]
        arr_merged += arr_s[j:]
        return arr_merged, inv
    else:
        return arr, 0

if __name__=="__main__":
    data = load_file("data/IntegerArray.txt")
    print(count_inversions(data))
    sorted_array, inversions = merge_sort(data)
    print(inversions)