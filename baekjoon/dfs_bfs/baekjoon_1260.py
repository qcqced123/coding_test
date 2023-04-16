import sys
from collections import deque
"""
[풀이 시간]
1) 23:30 ~ 24:10

[요약]
1) 주어진 그래프 노드 정보를 통해 DFS/BFS 결과를 모두 출력하기

[전략]
1) 두 알고리즘 구현의 공통점, 차이점을 묻는 문제
    - 공통점: 그래프 자료 구조 표현 방식
    - 차이점: 탐색 방식(DFS: Stack, BFS: 테이블)
    - 작은 번호부터 방문: 정렬해서 자료구조에 저장
"""


def dfs(src, visited):
    """ Depth First Search """
    visited[src] = True
    print(src, end=' ')
    for node in graph[src]:
        if not visited[node]:
            dfs(node, visited)


def bfs(src, visited):
    queue = deque([src])
    print(src, end=' ')
    visited[src] = True
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                print(next_node, end=' ')
                visited[next_node] = True
                queue.append(next_node)


N, M, V = list(map(int, sys.stdin.readline().split())) # 노드 개수, 간선 개수, 시작 위치
graph, dfs_visited, bfs_visited = [[] for _ in range(N+1)], [False for _ in range(N+1)], [False for _ in range(N+1)]
for _ in range(M):
    """ make table """
    v, end = map(int, sys.stdin.readline().split())
    graph[v].append(end)
    if v not in graph[end]:
        graph[end].append(v)

for i in range(N+1):
    graph[i].sort()

dfs(V, dfs_visited)
print('')
bfs(V, bfs_visited)
