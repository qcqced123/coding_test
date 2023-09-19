import sys
import heapq
from typing import List
try:
    profile
except NameError:
    profile = lambda x: x


@profile
def dijkstra(x: int, graph: List[List[int]], costs: List[float]) -> None:
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

@profile
def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph, costs = [[] for _ in range(N+1)], [float('inf')] * (N+1)  # 스펠링 똑바로 적자

    for _ in range(M):
        A, B, weight = map(int, sys.stdin.readline().split())
        graph[A].append((weight, B))

    src, end = map(int, sys.stdin.readline().split()) # init start & end node
    costs[src] = 0
    dijkstra(src, graph, costs)
    print(costs[end])


if __name__ == "__main__":
    main()
