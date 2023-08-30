import sys
from collections import deque
from typing import List

"""
[시간]
1) 00:35 ~ 00:55
[요약]
1) 정사각형으로 이루어져 있는 섬과 바다 지도가 주어지면 섬의 개수를 세는 프로그램 작성
    - 섬: 걸어갈 수 있는 정사각형으로 구성된 집합체
    - 걷기 가능: 상하좌우 + 대각선 연결
[전략]
1) 테이블 형태의 자료구조 & 상하좌우: BFS가 가장 유리
    - 영역 구분: BFS 메서드 호출 횟수 == 섬의 개수
"""


def bfs(y: int, x: int, visit: List[bool]) -> None:
    visit[y][x] = True
    queue = deque()
    queue.append([y, x])
    while queue:
        vy, vx = queue.popleft()
        for i in range(8):
            ny = dy[i] + vy
            nx = dx[i] + vx
            if -1 < ny < H and -1 < nx < W and not visit[ny][nx] and global_map[ny][nx] == 1:
                visit[ny][nx] = True
                queue.append([ny, nx])


iter_checker = True
dy = [0, 0, -1, 1, -1, 1, -1, 1]
dx = [-1, 1, 0, 0, 1, -1, -1, 1]

while iter_checker:
    W, H = map(int, sys.stdin.readline().split())  # col, row
    if W == 0 and H == 0:  # exit()
        break

    global_map = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    visited, result = [[False] * W for _ in range(H)], 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and global_map[i][j] == 1:
                bfs(i, j, visited)
                result += 1
    print(result)
