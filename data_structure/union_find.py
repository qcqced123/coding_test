import sys


def find(arr: list, x: int) -> int:
    """ method for finding root node """
    if arr[x] != x:
        arr[x] = find(arr, arr[x])
    return arr[x]


def union(arr: list, x: int, y: int):
    """ method for union-find """
    root_x = find(arr, x)
    root_y = find(arr, y)

    if root_x < root_y:
        arr[y] = root_x
    else:
        arr[x] = root_y
    return arr


if __name__ == '__main__':
    tree = [0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,15,15,15]
    print(union(tree,12, 17))


