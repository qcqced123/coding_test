import sys
from typing import List
"""
[요약]
1) N개의 노드로 구성된 트리, M개의 두 노드 쌍을 입력 받아 쌍 사이의 거리를 출력
    - 경로 구하는 문제 + 간선에 가중치가 포함된 문제
    - 시간 제한: 2초
    - 메모리: 넉넉
    - 입력: 1000, 1000
    => 재귀로 풀어야 할 듯
[전략]
1) X -> Y 경로를 구하면서, 가중치의 합까지
    - 근데 가중치를 어떻게 저장할거야..?
    - weight list를 graph랑 똑같이 만들어야지
"""


def dfs(src: int, end: int, arr: List[List[int]], visit: List[bool], result: int = 0) -> None:
    if src == end:
        print(result)

    visit[src] = True
    for i in range(len(arr[src])):
        if not visit[arr[src][i]]:
            dfs(arr[src][i], end, arr, visit, result + weights[src][i])


sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
graph, weights = [[] for _ in range(N+1)], [[] for _ in range(N+1)]

for _ in range(N-1):
    node1, node2, weight = map(int, sys.stdin.readline().split())
    graph[node1].append(node2), graph[node2].append(node1)
    weights[node1].append(weight), weights[node2].append(weight)

path = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  # X -> Y
# inference
for i in range(len(path)):
    visited = [False] * (N+1)
    X, Y = path[i]
    dfs(X, Y, graph, visited)
