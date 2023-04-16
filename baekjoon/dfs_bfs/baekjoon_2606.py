import sys
from collections import deque
"""
[풀이 시간]
1) 21:15 ~ 21:26

[요약]
1) 바이러스는 연결된 네트워크를 통해 전파
    - 1번 (시작 노드) 컴퓨터가 감염되었을 때, 감염되는 컴퓨터의 숫자
[전략]
1) 전형적인 DFS/BFS 문제
    - 메모리 제한, 시간 제한 높음
"""


def bfs(src, visit_list):
    queue = deque([src])
    visit_list[src] = True
    count = 0
    while queue:
        node = queue.popleft()
        for t_node in graph[node]:
            if not visit_list[t_node]:
                queue.append(t_node)
                visit_list[t_node] = True
                count += 1
    return count


N = int(sys.stdin.readline())
graph, visited = [[] for _ in range(N+1)], [False for _ in range(N+1)]

for _ in range(int(sys.stdin.readline())):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2), graph[node2].append(node1)

print(bfs(1, visited))
