import sys


def bfs(y: int, x: int) -> None:
    count = 0
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if not grid[ny][nx]:
            count += 1
    if count > 1:
        melt.add((y, x))


def dfs(y: int, x: int) -> None:
    global flag
    grid[y][x] = 2
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if -1 < ny < n and -1 < nx < m and not grid[ny][nx]:
            dfs(ny, nx)

        elif -1 < ny < n and -1 < nx < m and grid[ny][nx]:
            continue

        else:
            flag = False

        if not flag:
            grid[y][x] = 0
            return


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
    for i in range(2, n):
        for j in range(2, m):
            if (not grid[i][j] or grid[i][j] == 2) and grid[i-1][j] == 1 and grid[i][j-1] == 1:
                dfs(i, j)
                flag = True
    melt = set()
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
