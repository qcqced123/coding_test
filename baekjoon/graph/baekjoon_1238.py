import sys
import heapq
from collections import defaultdict


def dijkstra(src, arr, graph):
    arr[src] = 0
    h = []
    heapq.heappush(h, (arr[src], src))
    while h:
        vw, vx = heapq.heappop(h)
        if vw > arr[vx]:
            continue
        for i in graph[vx]:  # update cost of curr path
            curr_w, curr_node = i[0], i[1]
            curr_cost = curr_w + vw
            if curr_cost < arr[curr_node]:
                arr[curr_node] = curr_cost
                heapq.heappush(h, (curr_cost, curr_node))


def solution():
    grid = defaultdict(list)
    N, M, X = map(int, sys.stdin.readline().split())  # nodes, edges, destination
    h2p, p2h = [float('inf')]*(N+1), [float('inf')]*(N+1)

    for _ in range(M):
        src, end, cost = map(int, sys.stdin.readline().split())
        grid[src].append((cost, end))  # for dijkstra

    for node in grid.keys():
        tmp = [float('inf')]*(N+1)
        if node == X:
            continue

        dijkstra(node, tmp, grid)
        h2p[node] = tmp[X]

    dijkstra(X, p2h, grid)
    result = 0
    for i, j in zip(h2p, p2h):
        if i == float('inf') or j == float('inf'):
            continue
        result = max(result, i+j)
    print(result)


if __name__ == "__main__":
    solution()
