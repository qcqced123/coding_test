import sys


def dfs(d: int, y: int, x: int) -> None:
    global count, dy, dx, grid, N
    if y == N - 1 and x == N - 1:
        count += 1
        return

    if not d:
        ty, tx = dy[0:2], dx[0:2]
    elif d == 1:
        ty, tx = dy, dx
    else:
        ty, tx = dy[1:], dx[1:]

    for i in range(len(ty)):
        nd = i if not d or d == 1 else i+1
        ny, nx = ty[i] + y, tx[i] + x

        if -1 < ny < N and 0 < nx < N and nd == 1 and not grid[ny][nx] and not grid[ny-1][nx] and not grid[ny][nx-1]:
            dfs(nd, ny, nx)

        elif -1 < ny < N and 0 < nx < N and nd != 1 and not grid[ny][nx]:
            dfs(nd, ny, nx)


N = int(sys.stdin.readline())
grid = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))
dy, dx, count = (1, 1, 0), (0, 1, 1), 0

if grid[N-1][N-1]:
    print(0)
    exit()
dfs(2, 0, 1)
print(count)
