import sys
import heapq
"""
[풀이]
1) 지름: 가능한 경우의 수 중에서 가장 긴 경로
    - (u, v, cost, -1)
2) DFS
    - set recursion limit
    - find leaf nodes to init start node
        - maybe leaf node has just one connection info in tree
    - iterate leaf nodes list to find most expensive path with dfs
        - maybe most expensive path will be included in leaf to leaf path
=> 수정된 풀이
    - 임의의 점에서 가장 먼 리프 노드 찾기 추가
    - 찾은 점에서 다시 제일 먼 지점 찾기
    => 힙을 사용하면 max()보다 빠름
"""


def dfs(src: int, weight: int):
    heapq.heappush(h, [-weight, src])
    visit[src] = True
    for j in tree[src]:
        next_cost, next_node = j[0], j[1]
        if not visit[next_node]:
            dfs(next_node, weight+next_cost)


sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree, visit, h = [[] for _ in range(N+1)], [False] * (N+1), []

for _ in range(N):
    u, *conn = list(map(int, sys.stdin.readline().split()))[:-1]
    for i in range(0, len(conn), 2):
        v, cost = conn[i], conn[i+1]
        tree[u].append([cost, v])  # [cost, v]

dfs(1, 0)
_, node = heapq.heappop(h)
h.clear()

visit = [False] * (N+1)
dfs(node, 0)
cost, _ = heapq.heappop(h)
print(-1*cost)