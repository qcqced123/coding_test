import sys
from collections import deque


def bfs(y: int, x: int) -> int:
    count, visit[y][x] = 0, True
    q = deque()
    q.append((y, x))
    while q:
        vy, vx = q.popleft()
        for i in range(4):
            ny, nx = dy[i] + vy, dx[i] + vx
            if -1 < ny < n and -1 < nx < m and not visit[ny][nx] and grid[ny][nx] != 'X':
                visit[ny][nx] = True
                q.append((ny, nx))
                if grid[ny][nx] == 'O':
                    continue
                count += 1
                grid[ny][nx] = 'O'
    return count


n, m = map(int, sys.stdin.readline().split())
grid, visit = [], [[False]*m for _ in range(n)]
for i in range(n):
    col = list(map(str, sys.stdin.readline().rstrip()))
    grid.append(col)
    for j in range(m):
        if col[j] == 'I':
            my_y, my_x = i, j
            grid[my_y][my_x] = 'O'
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
result = bfs(my_y, my_x)
print(result if result else 'TT')
