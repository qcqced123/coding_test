"""

1) Edge Weight = 1
2) 1 ~ N번 노드, M개의 단방향 도로
3) 특정 도시 X로부터 도달 가능한 모든 도시 중에서, 최단거리 K인 모든 도시들 번호 출력
4) 자기 자신으로 가는 최단 거리는 0

"""
from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for value in range(N + 1)] # 행렬, 테이블 구조는 무조건 이렇게 선언하자
visited = [False for vertex in range(N)]
cost = [0 for edge in range(N)]

for i in range(M):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)

print(graph)

def dfs(graph, visited, X):
    # 지금 노드 2에 의해 sub routine call 된 상황이라고 가정하자
    visited[X-1] = True
    for i in graph[X]:
        if cost[i-1] >
            cost[i-1] += 1
        if not visited[i-1]:

            dfs(graph, visited, i)
