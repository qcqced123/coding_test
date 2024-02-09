import sys
import heapq
from collections import defaultdict
from typing import List


def dijkstra(x: int, distance: List, graph: defaultdict[int, List]) -> None:
    distance[x] = 0
    h = []
    heapq.heappush(h, (distance[x], x))
    while h:
        min_cost, min_node = heapq.heappop(h)
        if min_cost > distance[min_node]:
            continue

        for i in graph[min_node]:
            curr_cost, curr_node = i
            new_cost = min_cost + curr_cost
            if new_cost < distance[curr_node]:
                distance[curr_node] = new_cost
                heapq.heappush(h, (new_cost, curr_node))


def solution():
    grid = defaultdict(list)
    N, M = map(int, sys.stdin.readline().split())

    for _ in range(M):
        src, end, weight = map(int, sys.stdin.readline().split())
        grid[src].append((weight, end)), grid[end].append((weight, src))

    v1, v2 = map(int, sys.stdin.readline().split())
    dest_list = [1, v1, v2]
    cost_list = ([float('inf')] * (N + 1), [float('inf')] * (N + 1), [float('inf')] * (N + 1))
    for i in range(len(dest_list)):
        dijkstra(dest_list[i], cost_list[i], grid)

    result = min(cost_list[0][v1] + cost_list[1][v2] + cost_list[2][N], cost_list[0][v2] + cost_list[1][N] + cost_list[2][v1])
    print(result if result != float('inf') else -1)


if __name__ == "__main__":
    solution()
