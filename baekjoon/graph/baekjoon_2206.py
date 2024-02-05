import sys
from collections import deque


def bfs(y: int, x: int) -> int:
    global hammer, wall
    visit.add((y, x))
    q , dest = deque([(1, y, x)]), (n-1, m-1)
    while q:
        vw, vy, vx = q.popleft()
        for i in range(4):
            ny, nx = dy[i] + vy, dx[i] + vx
            if ny == n - 1 and nx == m - 1:
                return vw+1
            if -1 < ny < n and -1 < nx < m and (ny, nx) not in visit and not grid[ny][nx]:
                visit.add((ny, nx))
                q.append((vw+1, ny, nx))

        if not q and dest not in visit and hammer:  # 벽을 부수지 않은 퓨어한 상태
            hammer -= 1
            return -3

        elif not q and dest not in visit and not hammer and not wall:
            return -1

        elif not q and dest not in visit and not hammer:  # 도달 불가
            return -2


n, m = map(int, sys.stdin.readline().split())
grid, wall, hammer = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)], set(), 1
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

for i in range(n):
    for j in range(m):
        if grid[i][j]:
            check = 0
            for k in range(4):
                ni, nj = dy[k] + i, dx[k] + j
                if -1 < ni < n and -1 < nj < m and not grid[ni][nj]:
                    check += 1
            if check > 0:
                wall.add((i, j))

flag, result, w_r, w_c = True, 0, -1, -1
while flag:
    visit = set()
    result = bfs(0, 0)
    if result >= -1:
        break
    else:
        if w_r != -1 and w_c != -1:
            grid[w_r][w_c] = 1
        w_r, w_c = wall.pop()
        grid[w_r][w_c] = 0
print(result)

