import sys
from typing import Set


def bfs(y: int, x: int) -> None:
    count = 0
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if grid[ny][nx] == 2:
            count += 1
    if count > 1:
        melt.add((y, x))


def dfs(y: int, x: int, visited: Set) -> None:
    visited.add((y, x))
    grid[y][x] = 2
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if -1 < ny < n and -1 < nx < m and (ny, nx) not in visited and grid[ny][nx] == 0:
            dfs(ny, nx, visited)


sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
grid, cheese_set, flag, result = [], set(), True, 0
for i in range(n):
    tmp_col = list(map(int, sys.stdin.readline().split()))
    grid.append(tmp_col)
    for j in range(m):
        if tmp_col[j]:
            cheese_set.add((i, j))

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
while cheese_set:
    melt, visit = set(), set()
    dfs(0,0, visit)

    for cheese in cheese_set:
        r, c = cheese
        bfs(r, c)

    for cheese in melt:
        m_r, m_c = cheese
        grid[m_r][m_c] = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 0
    cheese_set -= melt
    result += 1
print(result)
