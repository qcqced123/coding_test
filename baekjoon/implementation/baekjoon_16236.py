import sys
from collections import deque
from typing import List
"""
1) 시간
21:15 ~ 21:45
"""


def bfs(y: int, x: int) -> bool:
    visit[y][x] = True
    q = deque([])
    q.append([0, y, x])

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    flag = False
    while q:
        print(q)
        vs, vy, vx = q.popleft()  # second
        for i in range(4):
            ny = dy[i] + vy
            nx = dx[i] + vx
            if r == ny and c == nx:
                result[0] += vs + 1
                grid[ny][nx] = 0
                flag = True
                break

            elif -1 < ny < N and -1 < nx < N and not visit[ny][nx] and shark[0] >= grid[ny][nx]:
                visit[ny][nx] = True
                q.append([vs+1, ny, nx])  # fish weight, r, c
        if flag:
            break
    if flag:
        return True
    else:
        return False


def filtering(w: int) -> None:
    length = len(fishes)
    while length:
        s, r, c = fishes.popleft()
        if s < w:
            length -= 1
            dest.append([s, r, c])

        else:
            length -= 1
            fishes.append([s, r, c])


def sorting(w: int, r: int, c: int) -> None:
    filtering(w)
    dest.sort(key=lambda x: (abs(x[1] - r)) + abs(x[2] - c))


N = int(sys.stdin.readline())
grid, shark = [], []
fishes, dest, result, checker = deque([]), [], [0], 0

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    grid.append(temp)
    for j in range(N):
        if temp[j] == 9:
            shark.extend([2, i, j])  # shark weight, row, col
            grid[i][j] = 0

        elif temp[j]:
            fishes.append([temp[j], i, j])  # fish weight, row, col

sorting(shark[0], shark[1], shark[2])
while dest:
    w, r, c = dest.pop()
    visit = [[False]*N for _ in range(N)]
    if bfs(shark[1], shark[2]):
        shark[1], shark[2] = r, c
        checker += 1
        if shark[0] == checker:
            shark[0] += 1
            checker = 0
        sorting(shark[0], shark[1], shark[2])
    else:
        print(result[0])
        exit()
print(result[0])
