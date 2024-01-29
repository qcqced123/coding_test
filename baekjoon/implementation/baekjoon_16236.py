import sys
from collections import deque
from typing import List


def bfs(y: int, x: int) -> bool:
    visit[y][x] = True
    q = deque([(0, y, x)])  # 시작 시간, 현재 위치의 행, 현재 위치의 열을 튜플로 묶어 큐에 저장
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        vs, vy, vx = q.popleft()  # second
        print(f"vs, vy, vx: {vs, vy, vx}")
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            if r == ny and c == nx:
                result[0] += vs + 1
                grid[ny][nx] = 0
                return True
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx] and shark[0] >= grid[ny][nx]:
                visit[ny][nx] = True
                q.append((vs + 1, ny, nx))
    return False


def filtering(fw: int) -> None:
    new_fishes = deque()
    for fs, fr, fc in fishes:
        if fs < fw:
            dest.append([fs, fr, fc, 0])  # dest[3]: distance
        else:
            new_fishes.append([fs, fr, fc])


def sorting(sw: int, sr: int, sc: int) -> None:
    filtering(sw)  # already calculate destination
    dest.sort(key=lambda x: (x[3], x[1], x[2]), reverse=True)
    print(f"dest: {dest}")


sys.setrecursionlimit(10**6)
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
    w, r, c, _ = dest.pop()
    print(f"w, r, c: {w, r, c}")
    print(f"result: {result}")
    visit = [[False]*N for _ in range(N)]
    if bfs(shark[1], shark[2]):
        shark[1], shark[2] = r, c
        print(f"new shark pos: {shark[1], shark[2]}")
        checker += 1
        if shark[0] == checker:
            shark[0] += 1
            checker = 0
        sorting(shark[0], shark[1], shark[2])
    else:
        print(result[0])
        exit()
print(result[0])
