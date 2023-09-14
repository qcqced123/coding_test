import sys
import heapq
from typing import List
"""
[요약]
1) Dijkstra with heap sorting
"""


def dijkstra(x: int, y: int) -> None:
    h = []
    heapq.heappush(h, (costs[x], x))  # init start node to heap sort
    while h:
        min_cost, nodes = heapq.heappop(h)
        if min_cost > costs[nodes]:
            continue
        for i in graph[nodes]:
            new_cost = min_cost + i[0]
            if new_cost < costs[i[1]]:
                costs[i[1]] = new_cost
                heapq.heappush(h, (new_cost, i[1]))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph, costs = [[] for _ in range(M+1)], [float('inf')] * (N+1)

for _ in range(M):
    A, B, weight = map(int, sys.stdin.readline().split())
    graph[A].append((weight, B))

src, end = map(int, sys.stdin.readline().split()) # init start & end node
costs[src] = 0
dijkstra(src, end)
for i in range(1, N+1):
    if i == end:
        print(costs[i])

