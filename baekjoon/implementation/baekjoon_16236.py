import sys
from collections import deque
from typing import List


def bfs(y: int, x: int, idx: List) -> bool:
    visit[y][x] = True
    q = deque([(0, y, x)])
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        vs, vy, vx = q.popleft()  # second
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            if r == ny and c == nx:
                idx[3] = vs + 1
                return True
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx] and shark[0] >= grid[ny][nx]:
                visit[ny][nx] = True
                q.append((vs + 1, ny, nx))
    return False


def filtering(sw: int) -> None:
    global fishes
    new_fishes = []
    for fs, fr, fc in fishes:
        if fs < sw:
            dest.append([fs, fr, fc, 0])  # dest[3]: distance
        else:
            new_fishes.append([fs, fr, fc])
    fishes = new_fishes


N = int(sys.stdin.readline())
grid, shark = [], []
fishes, dest, result, checker = [], [], [0], 0

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    grid.append(temp)
    for j in range(N):
        if temp[j] == 9:
            shark.extend([2, i, j])  # shark weight, row, col
            grid[i][j] = 0

        elif temp[j]:
            fishes.append([temp[j], i, j])  # fish weight, row, col

filtering(shark[0])
while dest:
    tmp_dest, tmp_fishes = [], []
    for k in dest:
        w, r, c, _ = k
        visit = [[False] * N for _ in range(N)]
        if bfs(shark[1], shark[2], k):
            tmp_dest.append(k)
        else:
            tmp_fishes.append([w, r, c])  # 먹을 수 있는데 도달 못하는 경우 처리
    dest = tmp_dest
    fishes += tmp_fishes
    if not dest:  # 더 이상 갈 곳 없는 경우
        break

    dest.sort(key=lambda x: (x[3], x[1], x[2]), reverse=True)
    w, r, c, t = dest.pop()
    result[0] += t
    grid[r][c] = 0

    shark[1], shark[2] = r, c
    checker += 1
    if shark[0] == checker:
        shark[0] += 1
        checker = 0
    filtering(shark[0])
print(result[0])
