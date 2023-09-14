import sys
import heapq
from typing import List
"""
[요약]
1) Dijkstra with heap sorting
     - 입력 길이: 노드 1천개
     => 다만, 시간 제한 0.5초라서 힙으로 구현 필요
"""
try:
    profile
except NameError:
    profile = lambda x: x


@profile
def dijkstra(x: int) -> None:
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
graph, costs = [[] for _ in range(N+1)], [float('inf')] * (N+1)  # 스펠링 똑바로 적자

for _ in range(M):
    A, B, weight = map(int, sys.stdin.readline().split())
    graph[A].append((weight, B))

src, end = map(int, sys.stdin.readline().split()) # init start & end node
costs[src] = 0
dijkstra(src)
print(costs[end])
