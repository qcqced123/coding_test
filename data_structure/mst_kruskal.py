import sys
from typing import List
"""
[조건]
1) 모든 컴퓨터가 연결 상태
    - 연결 상태 == 간선 혹은 경로 존재
    - 모든 컴퓨터를 최소 비용으로 연결
[풀이]
1) 개별 노드를 시작 노드로 iteration
    - 모든 노드에 도달 가능한 경로가 존재하는가
    - 가능한 경로 중에서 최소 비용 경로 찾기
    => 얘는 최소 스패닝 트리를 찾아보고 풀자 의미없다 이렇게 푸는게
"""


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


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph, parent = [], [0]*(N+1)

# 0-0) 간선 연결 정보 초기화, 정렬
for _ in range(M):
    src, end, cost = map(int, sys.stdin.readline().split())
    graph.append((cost, src, end))
graph.sort()

# 0-1) 연결 정보 초기화
for i in range(1, N+1):
    parent[i] = i

# 1) Kruskal Algorithm
result = 0
for j in range(M):
    weight, start, final = graph[j]
    if find(parent, start) != find(parent, final):
        union(parent, start, final)
        result += weight

print(result)
