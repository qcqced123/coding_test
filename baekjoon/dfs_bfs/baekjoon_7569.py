import sys
from collections import deque
"""
[풀이 시간]
1) 14:30 ~ 15:00

[요약]
1) 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관
    - 3차원이네...?
    - 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토
    - 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성
[전략]
1) 7576번과 거의 유사, 3차원 리스트가 되어 좀 더 복잡 및 방향 추가
    - 3차원 리스트를 만들어서 접근해야 하기 때문에 복잡
"""


def bfs():
    global day
    while queue:
        day += 1
        for _ in range(len(queue)):
            z, y, x = queue.popleft()
            for idx in range(6):
                nz = z + dz[idx]
                ny = y + dy[idx]
                nx = x + dx[idx]
                if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and table[nz][ny][nx] == 0:
                    table[nz][ny][nx] = 1
                    queue.append([nz, ny, nx])
    for height in range(H):
        for row in range(N):
            for col in range(M):
                if table[height][row][col] == 0:
                    return -1
    return day - 1


M, N, H = map(int, sys.stdin.readline().split())
table = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
day = 0

dz = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

queue = deque([])
for k in range(H):
    for i in range(N):
        for j in range(M):
            if table[k][i][j] == 1:
                queue.append([k, i, j])
print(bfs())
