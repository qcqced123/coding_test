import sys


def solution():

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

    sys.setrecursionlimit(10**5)
    N, M = map(int, sys.stdin.readline().split())
    grid, parent = [], [0]*(N+1)
    for _ in range(M):
        s, e, c = map(int, sys.stdin.readline().split())
        grid.append((c,s,e))

    grid.sort()
    for i in range(1, N+1):
        parent[i] = i

    result, edges = 0, []
    for i in range(M):
        cost, src, end = grid[i]
        if find(parent, src) != find(parent, end):
            union(parent, src, end)
            edges.append(cost)
            result += cost

    edges.sort()
    result -= edges.pop()
    print(result)


if __name__ == "__main__":
    solution()
