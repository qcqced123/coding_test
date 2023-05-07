import sys
from collections import deque


def bfs():
    global day
    while queue:
        day += 1
        for _ in range(len(queue)):  # 여기가 일수 처리 해주는 코드
            y, x = queue.popleft()
            for idx in range(4):
                ny = y + dy[idx]
                nx = x + dx[idx]
                if 0 <= ny < N and 0 <= nx < M and table[ny][nx] == 0:
                    table[ny][nx] = 1
                    queue.append([ny, nx])
    for row in range(N):
        for col in range(M):
            if table[row][col] == 0:
                return -1
    return day - 1


M, N = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
day = 0

dy = [-1, 1, 0, 0]  # M
dx = [0, 0, -1, 1]  # N

queue = deque([])
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            queue.append([i, j])
print(bfs())
