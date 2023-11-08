import sys
from typing import List
from collections import deque

"""
[조건]
1) 공기 청정기: 항상 1열 배치
    - 크기는 두 행 차지

[풀이]
1) 미세 먼지 확산(모두 동시)
    - 상하좌우 확산
        - 상하좌우에 공기 청정기 존재 여부 판단
            - 있거나, 격자 끝이라면 이동 중지
    - 확산 질량: 기존 양 // 5
    - 새로운 위치 잔존 미세 먼지 양 계산
        - 동시 이동으로 구현해야 함
    - 현재 위치 잔존 미세 먼지 양 계산
2) 공기 청정기 작동
    - 반시계/시계 방향 회전 => 위쪽/아래쪽
        - 풍향에 따라 미세 먼지도 한 칸씩 이동
        - 풍향에 따라서 공기 청정기에 들어온 미세 먼지는 모두 사라짐
=> 공기 청정기 작동 구현을 찾아보자...
"""


def move(r: int, c: int):
    check = True
    for i in range(4):
        while check:
            if not i:
                grid[r+1][c] = 0
                for j in range(r+1, R-1):
                    grid[j][c] = grid[j+1][c]
                break
            elif i == 1:
                for j in range(C-1):
                    grid[R-1][j] = grid[R-1][j+1]
                break
            elif i == 2:
                for j in range(R-1, r, -1):
                    grid[j][-1] = grid[j-1][-1]
                break
            else:
                for j in range(C-1, 1, -1):
                    grid[r][j] = grid[r][j-1]
                grid[r][1] = 0
                break


def r_move(r: int, c: int):
    check = True
    for i in range(4):
        while check:
            if not i:
                grid[r-1][c] = 0
                for j in range(r-1, 0, -1):
                    grid[j][c] = grid[j-1][c]
                break
            elif i == 1:
                for j in range(C-1):
                    grid[0][j] = grid[0][j+1]
                break
            elif i == 2:
                for j in range(0, r):
                    grid[j][-1] = grid[j+1][-1]
                break
            else:
                for j in range(C-1, 1, -1):
                    grid[r][j] = grid[r][j-1]
                grid[r][1] = 0
                break


def solution():
    # 1) init queue for moving dust, list for air purifier
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                q.append([i, j])
            elif grid[i][j] == -1:
                air_purifier.append([i, j])

    # 2) conditional dust move
    curr = 1
    while q:
        add_list = []
        for _ in range(len(q)):  # cutting search depth by each time
            vy, vx = q.popleft()
            count, n_dust = 0, grid[vy][vx] // 5
            for i in range(4):
                ny = dy[i] + vy
                nx = dx[i] + vx
                if -1 < ny < R and -1 < nx < C and grid[ny][nx] != -1:
                    q.append([ny, nx])
                    add_list.append([ny, nx, n_dust])
                    count += 1
            grid[vy][vx] -= count * n_dust
        # 2-2) 잔존 먼지양 동시에 업데이트
        for r, c, d in add_list:
            grid[r][c] += d

        # 3) 공기 청정기 가동
        for i, l in enumerate(air_purifier):
            ra, ca = l
            r_move(ra, ca) if not i else move(ra, ca)

        # 4) 루프 종료 조건: 다음 턴 진행
        if curr == T:
            break
        curr += 1
    print(sum(map(sum, grid)) + 2)


if __name__ == "__main__":
    R, C, T = map(int, sys.stdin.readline().split())  # row, col, iter
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    q, air_purifier = deque([]), []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    solution()
