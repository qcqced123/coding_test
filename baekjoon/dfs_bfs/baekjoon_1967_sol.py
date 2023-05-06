import sys
"""
[Sol]
기존 내 풀이는 시간 초과로 제출이 안되는 상황, 정답은 맞추는 듯 하다.
1) 루트에서 가장 멀리 있는 노드 찾기
2) 1번에서 찾은 노드에서 가장 멀리 떨어진 노드 찾기
"""


def dfs(start, total):
    for node, weight in node_list[start]:
        if distance[node] == -1:
            distance[node] = total + weight
            dfs(node, total + weight)


sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
node_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    src, end, cost = map(int, sys.stdin.readline().split())
    node_list[src].append([end, cost])
    node_list[end].append([src, cost]) # for stage 2

distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)
first_idx = distance.index(max(distance))

distance = [-1] * (N + 1)
distance[first_idx] = 0
dfs(first_idx, 0)
print(max(distance))
