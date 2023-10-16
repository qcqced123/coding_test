import sys
from typing import List
from collections import deque
"""
[풀이]
1) 격자 한복판 탐색 시작
    - 시작 위치 지정 필요
    - 어차피 시작 위치를 미리 알아서 모래 위치를 받을 필요 없음
2) 위치 이동 구현
    - 특정 방향에 대한 최대 탐색 깊이가 점점 커짐 (1 to N)
        - 탐색 깊이마다 두번씩 탐색, 2번 이후 깊이 사이즈+1
    - 반시계 방향 구현
    => 따로 메서드를 만들 필요까지 없을듯
3) 모래 양 계산 메서드
    - 격자에 남아 있는 모래양, 기존 격자의 모래와 합치기
    - 격자 밖으로 나가는 모래양 죄다 합치기
    - 상어가 어디서 왔는가 정보 필요함
    - 격자는 큐를 통해 구현 rotate
"""


def calculate(y: int, x: int, direction: int):
    global result
    sand, s_grid = grid[y][x], deque([[0,0], [1,0], [7,2], [10,0], [0,5], [10, 0], [7,2], [1,0]])
    s_grid.rotate(2*direction)
    sy = [0, -1, -1, -1, 0, 1, 1, 1]
    sx = [1, 1, 0, -1, -1, -1, 0, 1]
    total_sand = 0
    for i in range(8):
        for j in range(1, 3):
            ny = sy[i]*j + y
            nx = sx[i]*j + x
            tmp_sand = int((s_grid[i][j-1]/100) * sand)
            if -1 < ny < N and -1 < nx < N:
                grid[ny][nx] += tmp_sand
            else:
                result += tmp_sand
            total_sand += tmp_sand
    grid[y][x] = 0
    return sand - total_sand


def solution():
    y, x = N // 2, N // 2  # init starting point
    dy = [0, 1, 0, -1]  # 반시계 방향
    dx = [-1, 0, 1, 0]
    moving, depth, d = True, 1, 0  # for moving depth
    while moving:
        for _ in range(2):
            for j in range(depth):
                direction = d % 4
                ny = dy[direction] + y
                nx = dx[direction] + x
                if grid[ny][nx]:
                    alpha = calculate(ny, nx, direction)  # need to calculate sand vol
                    alpha_y, alpha_x = dy[direction]+ny, dx[direction]+nx
                    if -1 < alpha_y < N and -1 < alpha_x < N:
                        grid[alpha_y][alpha_x] = alpha

                if not ny and not nx:
                    moving = False
                    break

                y, x = ny, nx
            if not moving:
                break
            d += 1  # change direction
        depth += 1  # update depth size
    print(result)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    result = 0
    solution()
