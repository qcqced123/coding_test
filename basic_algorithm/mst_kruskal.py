import sys
from typing import List


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


# get input data
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph, parent = [], [0]*(N+1)

# init graph structure
for _ in range(M):
    src, end, cost = map(int, sys.stdin.readline().split())
    graph.append((cost, src, end))

graph.sort()

# init disjoint set array
for i in range(1, N+1):
    parent[i] = i

# make the mst by using kruskal algorithm
# kruskal is the edge-based algorithm for making the mst(minimum spanning tree)
result = 0
for j in range(M):
    weight, start, final = graph[j]
    if find(parent, start) != find(parent, final):
        union(parent, start, final)
        result += weight

print(result)
