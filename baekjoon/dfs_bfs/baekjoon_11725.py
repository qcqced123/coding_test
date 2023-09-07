import sys
from typing import List
"""
[시간]
1) 10분

[요약]
1) 루트 없는 트리가 주어지고, 트리의 루트를 1이라고 지정, 이 때 각 노드의 부모를 구해라
    - 시간 제한: 1초
    - 메모리: 넉넉함
    - 입력 길이: 10만
    => 이중 루프 연산 불가
    - 연결 정보가 주어짐
[전략]
1) DFS/BFS
    - 트리용으로 구현 필요
    - stack, queue
    - 파이썬 재귀 호출 최대: 1000
    => 10^6으로 세팅 필요, 항상 이거부터 세팅하고 문제 풀자
"""


def dfs(src: int, graph: List[List[int]], visit: List[bool], result: List[int]) -> None:
    visit[src] = True
    for i in graph[src]:
        if not visit[i]:
            result[i] = src
            dfs(i, graph, visit, result)


sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2), tree[node2].append(node1)

visited = [False] * (N+1)
results = [0] * (N+1)

dfs(1, tree, visited, results)
for i in range(2, N+1):
    print(results[i])
