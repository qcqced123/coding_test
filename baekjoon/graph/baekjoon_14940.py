import sys
from collections import deque
from typing import List


def bfs(y: int, x: int, graph: List[List], visited: List[List]) -> None:
    graph[y][x] = 0
    visited[y][x] = True
    q = deque([(0, y, x)])  # distance, y, x

    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    while q:
        vd, vy, vx = q.popleft()
        for i in range(4):
            ny, nx = dy[i] + vy, dx[i] + vx
            if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and not visited[ny][nx] and graph[ny][nx]:
                nd = vd + 1
                graph[ny][nx], visited[ny][nx] = nd, True
                q.append((nd, ny, nx))
    return


def solution():
    n, m = map(int, sys.stdin.readline().split())
    grid, dest, visit = [], None, [[False]*m for _ in range(n)]

    for i in range(n):
        col = list(map(int, sys.stdin.readline().split()))
        grid.append(col)
        for j in range(m):
            if grid[i][j] == 2:
                dest = (i, j)
                break
    bfs(dest[0], dest[1], grid, visit)
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and grid[i][j] == 1:
                grid[i][j] = -1

    for i in grid:
        print(*i, end='\n')


if __name__ == "__main__":
    solution()
