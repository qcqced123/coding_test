import sys
from typing import List
"""
[요약]
1) 연결 엣지 개수만큼?? 지나치는 노드 개수 == 촌수
    - 시간 제한 : 1초
    - 메모리: 넉넉함
    - 입력 길이: 사람 100명
[전략]
1) 트리 구조 + DFS
    - 특정 노드 to 노드 경로 계산이랑 비슷한 듯
"""


def dfs(src: int, end: int, graph: List[List[int]], visit: List[bool], result: int = 0):
    if src == end:
        print(result)
        exit()

    visit[src] = True
    for j in graph[src]:
        if not visit[j]:
            dfs(j, end, graph, visit, result+1)  # 이렇게 넣어 주는게 훨씬 보기 편하다


sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
target1, target2 = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
tree, visited = [[] for _ in range(N+1)], [False] * (N+1),
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2), tree[node2].append(node1)
dfs(target1, target2, tree, visited)
print(-1)
