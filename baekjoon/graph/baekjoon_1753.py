import sys
import heapq
from typing import List
"""
[요약]
1) 방향 그래프가 주어지면 시작점에서 다른 모든 정점으로의 최단 경로 구하는 프로그램 작성
    - 가중치: 10이하 자연수, 음이 아닌 간선
    - 시간 제한: 1초, 메모리 여유, 노드 2만, 간선 30만
    - 힙 정렬 필수
    - 다익스트라
[전략]
1) 다익스트라 with heapq
    - 그래프 초기화: (가중치, 목적지)
    - 현재 노드 기준 가장 짧은 노드 선택
    -
"""


def dijkstra(x: int, distance: List[int]) -> None:
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


V, E = map(int, sys.stdin.readline().split())
src = int(sys.stdin.readline())

# 1) init graph
graph, costs = [[] for _ in range(V+1)], [float('inf')] * (V+1)
costs[src] = 0
for _ in range(E):
    u, v, weight = map(int, sys.stdin.readline().split())
    graph[u].append((weight, v))
print(graph)

dijkstra(src, costs)
for i in range(1, V+1):
    print(costs[i] if costs[i] != float('inf') else 'INF')








