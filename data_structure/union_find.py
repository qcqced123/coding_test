import sys


def find(arr: list, x: int) -> int:
    """ method for finding root node """
    if arr[x] != x:
        arr[x] = find(arr, arr[x])
    return arr[x]


def union(arr: list, x: int, y: int):
    """ method for union-find """
    x = find(arr, x)
    y = find(arr, y)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y


if __name__ == '__main__':
    tree = [0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,15,15,15]
    print(union(tree,12, 17))


