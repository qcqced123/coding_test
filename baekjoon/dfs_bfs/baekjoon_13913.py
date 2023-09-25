import sys
from collections import deque
from typing import Tuple, List


def bfs(x: int, y: int):
    graph[x] = 0
    q = deque([])
    q.append(x)
    while q:
        vx = q.popleft()
        for i in move:
            nx = vx * i if i == 2 else vx + i
            if -1 < nx < 100001 and graph[nx] == -1:
                graph[nx] = graph[vx] + 1
                q.append(nx)
                path[nx] = vx
            if nx == y:
                return graph[y]


N, K = map(int, sys.stdin.readline().split())
move, path, graph, result = [-1, 1, 2], {}, [-1] * 100001, [K]
min_value = bfs(N, K)
while K != N:
    K = path[K]
    result.append(K)
print(min_value)
print(*reversed(result))

