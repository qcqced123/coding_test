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

def postprocess(arr: list):
    """ func for post-processing for union-find
    when the input connection data isn't in order, union-find algorithm do not guarantee the
    right result of group segmentation

    so, guaranteeing the right result of group segmentation, you must call this func
    """
    for i in range(1, len(arr)):
        if i != arr[i]:
            arr[i] = find(arr, i)
    return arr

if __name__ == '__main__':
    tree = [0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,15,15,15]
    union(tree,12, 17)
    print(tree)
    postprocess(tree)


