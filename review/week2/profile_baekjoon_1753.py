import sys
import heapq
from typing import List


try:
    profile
except NameError:
    profile = lambda x: x


@profile
def dijkstra(x: int, distance: List[int], graph: List[List[int]]) -> None:
    h = []
    heapq.heappush(h, (distance[x], x))
    while h:
        min_cost, node = heapq.heappop(h)
        # 방문한 노드 처리: cost를 기준으로 다음 노드를 선정, 따라서 cost가 distance[node]보다 크다면 이미 방문 했던 노드로 볼 수 있음
        if min_cost > distance[node]:
            continue
        for i in graph[node]:
            cost = min_cost + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(h, (cost, i[1]))


@profile
def main(V, src, graph, costs):
    dijkstra(src, costs, graph)
    for i in range(1, V+1):
        print(costs[i] if costs[i] != float('inf') else 'INF')


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    src = int(sys.stdin.readline())

    # 1) init graph
    graph, costs = [[] for _ in range(V + 1)], [float('inf')] * (V + 1)
    costs[src] = 0
    for _ in range(E):
        u, v, weight = map(int, sys.stdin.readline().split())
        graph[u].append((weight, v))

    main(V, src, graph, costs)







