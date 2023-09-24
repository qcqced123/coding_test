import sys
from typing import Tuple
from collections import deque


def bfs(x: int, y: int) -> int:
    graph[x] = 0
    q = deque([])
    q.append(x)
    while q:
        vx = q.popleft()
        for i in move:
            nx = 2 * vx if i == 2 else vx + i
            if -1 < nx < 100001 and graph[nx] == -1:
                graph[nx] = graph[vx] if i == 2 else graph[vx] + 1

                if nx != y:
                    q.append(nx)

            elif -1 < nx < 100001 and graph[nx] != -1:
                tmp = graph[vx] if i == 2 else graph[vx] + 1
                graph[nx] = min(graph[nx], tmp)
    return graph[y]


N, K = map(int, sys.stdin.readline().split())
move, graph = [-1, 1, 2], [-1] * 100001
print(bfs(N, K))


