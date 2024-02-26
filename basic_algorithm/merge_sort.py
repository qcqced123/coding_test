import sys
from typing import List


def combine(l, r) -> List:
    result = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result += l[i:]
    result += r[j:]
    return result


def merge_sort(arr: List):
    """ Merge sort by divide & conquer with recursive call
    1) divide into optimal sub-structure
    2) conquer optimal sub-structure
    3) combine optimal sub-structure solution
    """
    if len(arr) <= 1:  # conquer
        return arr

    half = len(arr) // 2
    left = merge_sort(arr[:half])  # divide
    right = merge_sort(arr[half:])  # divide
    return combine(left, right)


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    array = [23, 4, 19, 8, 7, 20, 100, 1, 2, 3, 1011]
    print(merge_sort(array))
