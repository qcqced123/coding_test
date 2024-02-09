import sys
import heapq
from typing import List


def dijkstra(src: int, distance: List[int]) -> None:
    """ dijkstra algorithm: src node to rest of nodes
    1) select start node (o)
    2) init shortest-table (o)
        - start node are zero-init
    3) select shortest-cost which is visit FLAG == False
        - selecting algorithm must be implemented with heapq
        - heapq sort guarantee max or min element sorting
        - linear search will be restricted b time limit
    4) update additional path, created by current shortest path (o)
        - compare updated path's cost & past updated path
    5) iter above steps until complete
    """
    h = []
    heapq.heappush(h, (distance[src], src))
    while h:
        min_cost, node = heapq.heappop(h)
        if min_cost > distance[node]:
            continue

        for i in graph[node]:
            curr_cost, curr_node = i[0], i[1]
            cost = min_cost + curr_cost
            if cost < distance[curr_node]:
                distance[curr_node] = cost
                heapq.heappush(h, (cost, curr_node))


V, E = map(int, sys.stdin.readline().split())
src = int(sys.stdin.readline())

# 1) init graph
graph, costs = [[] for _ in range(V+1)], [float('inf')] * (V+1)
costs[src] = 0
for _ in range(E):
    u, v, weight = map(int, sys.stdin.readline().split())
    graph[u].append((weight, v))

dijkstra(src, costs)
for i in range(1, V+1):
    print(costs[i] if costs[i] != float('inf') else 'INF')








