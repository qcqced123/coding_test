import sys
from collections import deque
"""
[풀이 시간]
1) 18:30 ~ 18:47

[요약]
1) 방향 없는 그래프, 연결 요소의 개수 출력
    - 연결 요소가 뭘까
"""


def bfs(src, visit_list):
    queue = deque([src])
    visit_list[src] = True
    while queue:
        node = queue.popleft()
        for t_node in graph[node]:
            if not visit_list[t_node]:
                queue.append(t_node)
                visit_list[t_node] = True


N, M = map(int, sys.stdin.readline().split())
graph, visited, count = [[] for _ in range(N+1)], [False] * (N+1), 0

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2), graph[node2].append(node1)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i, visited)
        count += 1
print(count)
