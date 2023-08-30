import sys
from collections import deque
from typing import List
from itertools import combinations
from copy import deepcopy

"""
[시간]
1) 18:10 ~ 18:55
[요약]
1) 바이러스의 확산을 막기 위해서 연구소에 가벽 세워 안전 영역이 최대가 되도록 하는 프로그램 작성
    - 바이러스: 상하좌우, 빈 칸으로 이동 가능
    - 가벽은 꼭 3개 다 써야함
    - 0, 1, 2: 빈 칸, 벽, 바이러스
    - 안전 영역: 가벽을 모두 세운 뒤, 바이러스가 더 이상 퍼질 수 없는 구역
[전략]
1) BFS + BF
    - 입력이 짧고 시간 제한이 길어 여유로움
2) BFS + Greedy
"""


def bfs(y: int, x: int, virus_map: List[List[int]], visit: List[bool]):
    visit[y][x] = True
    queue = deque()
    queue.append([y, x])
    while queue:
        vy, vx = queue.popleft()
        for idx in range(4):
            ny = dy[idx] + vy
            nx = dx[idx] + vx
            if -1 < ny < N and -1 < nx < M and virus_map[ny][nx] == 0 and not visit[ny][nx]:
                visit[ny][nx] = True
                queue.append([ny, nx])
                virus_map[ny][nx] = 2


N, M = map(int, sys.stdin.readline().split())  # row, col
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# Step 1. find wall index
result = []
wall_list = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            wall_list.append([i, j])

# Step 2. make additional wall & move virus
for simulation in list(combinations(wall_list, 3)):
    tmp_lab = deepcopy(lab)
    visited = [[False] * M for _ in range(N)]
    wall1, wall2, wall3 = simulation[0], simulation[1], simulation[2]
    tmp_lab[wall1[0]][wall1[1]], tmp_lab[wall2[0]][wall2[1]], tmp_lab[wall3[0]][wall3[1]] = 1, 1, 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and tmp_lab[i][j] == 2:
                bfs(i, j, tmp_lab, visited)

    # Step 3. calculate score
    tmp_result = 0
    for i in range(N):
        for j in range(M):
            if tmp_lab[i][j] == 0:
                tmp_result += 1
    result.append(tmp_result)
print(max(result))
