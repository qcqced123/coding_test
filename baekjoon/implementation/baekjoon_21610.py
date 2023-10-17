import sys
from collections import deque
from typing import List, Tuple
"""
[풀이]
- 구름 초기 생성 -> 구름 이동 -> 물 뿌리기 -> 사라짐 -> 복사 버그 -> 구름 다시 생성
- 문제 인덱스 != 풀이 인덱스
- 복사 버그는 한 번에 업데이트!
"""


def bug(y: int, x: int):
    dy = [-1, 1, 1, -1]
    dx = [1, 1, -1, -1]
    result = 0
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if -1 < ny < N and -1 < nx < N and grid[ny][nx]:
            result += 1
    return result


def move(di: int, si: int, y: int, x: int) -> Tuple[int, int]:
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # 입력 방향 숫자와 코드상 방향 숫자 맞추기 위해 열 추가
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    ny = dy[di]*si + y
    nx = dx[di]*si + x
    if ny < 0:
        ny = (ny % N) + N
    if nx < 0:
        nx = (nx % N) + N
    if ny > N-1:
        ny = ny % N
    if nx > N-1:
        nx = nx % N
    return ny, nx


def solution():
    # 1) 구름 초기 생성
    for i in range(2):
        for j in range(N-2, N):
            cloud_q.append([j, i])
    while dir_q:
        d, s = dir_q.popleft()
        cloud = [[1]*N for _ in range(N)]  # for next cloud
        bug_pos, bug_result = [], []
        for _ in range(len(cloud_q)):
            vy, vx = cloud_q.popleft()
            ny, nx = move(d, s, vy, vx)
            grid[ny][nx] += 1
            cloud[ny][nx] = 0
            bug_pos.append([ny, nx])

        for ny, nx in bug_pos:
            bug_result.append(bug(ny, nx))

        for i, pos in enumerate(bug_pos):
            ny, nx = pos
            grid[ny][nx] += bug_result[i]

        for i in range(N):
            for j in range(N):
                if grid[i][j] >= 2 and cloud[i][j]:
                    cloud_q.append([i, j])
                    grid[i][j] -= 2
    print(sum(map(sum, grid)))


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dir_q, cloud_q = deque([list(map(int, sys.stdin.readline().split())) for _ in range(M)]), deque()
    solution()

