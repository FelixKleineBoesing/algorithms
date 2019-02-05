import os, sys

def count_inversions(list: []):
    k = 0
    n = len(list)
    for i in range(n):
        for j in range(i + 1,n):
            if list[i] > list[j]:
                k += 1
    return k


def merge_sort_inversions(list: []):
    if len(list) == 1:
        return list, 0
    else:
        a, b = list[:int(len(list)/2)], list[int(len(list)/2):]

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
    data = []
    with open("data/IntegerArray.txt") as f:
        lines = f.readlines()
    for row in lines:
        data += [int(row.replace("\n", ""))]
    print(data[0:6])
    a = [1, 3, 4, 5, 2, 1, 4, 8]
    print(count_inversions(a))
    #print(count_inversions(data))
    sorted_array, inversions = merge_sort_inversions(data)
    print(inversions)