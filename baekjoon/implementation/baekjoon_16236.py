import sys
from collections import deque


def bfs(y: int, x: int, size: int) -> bool:
    visit[y][x] = True
    queue = deque([])
    queue.append([0, y, x])

    dy, dx, flag = [-1, 1, 0, 0], [0, 0, -1, 1], True
    while queue:
        vt, vy, vx = queue.popleft()  # time, row, col
        for i in range(4):
            ny = dy[i] + vy
            nx = dx[i] + vx
            nt = vt + 1

            if ny == f_y and nx == f_x and size > grid[ny][nx]:
                print(f"mt: {nt}")
                result[0] += nt
                flag = False
                break

            elif -1 < ny < N and -1 < nx < N and not visit[ny][nx] and size >= grid[ny][nx]:
                visit[ny][nx] = True
                queue.append([nt, ny, nx])

        if not flag:
            return True

    return False


sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
result, count, grid, fishes = [0], 0, [], []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    grid.append(tmp)
    for j, v in enumerate(tmp):
        if v == 9:
            child_idx = [2, i, j]  # [size, row, col]
        elif v:
            fishes.append([v, i, j])  # [size, row, col]

c_size, c_y, c_x = child_idx
fishes.sort(
    key=lambda x: (x[0], abs(x[1] - c_y) + abs(x[2] - c_x)),
    reverse=True
)
while fishes:
    print(f"c_size: {c_size}")
    f_size, f_y, f_x = fishes.pop()
    visit = [[False] * N for _ in range(N)]
    checker = bfs(c_y, c_x, c_size)
    if checker:
        c_y, c_x = f_y, f_x
        count += 1
        if count == c_size:
            c_size += 1
            count = 0
        fishes.sort(
            key=lambda x: (x[0], abs(x[1] - c_y) + abs(x[2] - c_x)),
            reverse=True
        )  # key: size & distance
    else:
        print(result[0])
        exit()
print(result[0])
