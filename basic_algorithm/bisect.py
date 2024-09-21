from typing import List


def bisect_left(arr: List, v: int) -> int:
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if v > arr[mid]:
            l = mid + 1

        else:
            r = mid

    return l


def bisect_right(arr: List, v: int) -> int:
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r) // 2
        if v < arr[mid]:
            r = mid

        else:
            l = mid + 1

    return l
