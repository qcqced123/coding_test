import sys
from typing import List, Tuple
from collections import deque
"""
[조건]
1) 구간
    - ri, ci, mi, di, si: 행, 열, 질량, 방향, 속도
2) 질량: ⌊(합쳐진 파이어볼 질량의 합)/5⌋
3) 속력: ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
4) 방향
    - 모두 같은 방향: 짝수
    - 다른 경우: 홀수
[풀이]
- 이동 -> 계산 -> 없음
             -> 같은 칸에 두 개 이상 -> 1개로 합치기 -> 4개로 다시 나누기 -> 없음
                                                               -> 질량 0이면 소멸
디버깅 해보니까 양수 부분 변환이 잘 안되는 것 같다.
생각해보니까 매턴마다 그리드를 초기화 해줘야 한다.
grid를 conditional-loop 내부에서 계속 초기화하니까 시간이 개느려질 것 같은데
in 연산도 O(N)이나 잡아 먹는다. 어지간하면 쓰지 말자.
"""


def move(y: int, x: int, di: int, si: int):
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]  # 이동 방향 구현
    ny = dy[di]*si + y
    nx = dx[di]*si + x
    if ny < 1 or ny > N:
        y_rest = ny % N
        if not y_rest:
            ny = N
        else:
            ny = y_rest

    if nx < 1 or nx > N:
        x_rest = nx % N
        if not x_rest:
            nx = N
        else:
            nx = x_rest
    return ny, nx


def calculate(y: int, x: int, grid: List[List[List[int]]]) -> None:
    balls, m, s, d = grid[y][x][0], grid[y][x][1], grid[y][x][2], grid[y][x][3]
    nm, ns = int(m / 5), int(s / balls)
    nd = [0, 2, 4, 6] if not d or d == balls else [1, 3, 5, 7]
    if nm:
        for i in range(4):
            q.append([y, x, nm, ns, nd[i]])


def solution():
    cnt = 1
    while q:
        grid = [[[0, 0, 0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]  # [개수, 질량, 속도, 방향]
        cal_list = []
        for _ in range(len(q)):
            r, c, m, s, d = q.popleft()
            ny, nx = move(r, c, d, s)
            grid[ny][nx][0] += 1  # 개수
            grid[ny][nx][1] += m  # 질량
            grid[ny][nx][2] += s  # 속도
            grid[ny][nx][3] += d % 2  # 방향 판정용
            grid[ny][nx][4] += d  # 1개인 그리드 방향
            if grid[ny][nx][0] == 1:
                cal_list.append([ny, nx])

        for vy, vx in cal_list:
            if grid[vy][vx][0] > 1:
                calculate(vy, vx, grid)
                continue

            elif grid[vy][vx][0] == 1:
                q.append([vy, vx, grid[vy][vx][1], grid[vy][vx][2], grid[vy][vx][4]])
        if cnt == K:
            break
        cnt += 1

    # print result
    result = 0
    for _, _, m, _, _ in q:
        result += m
    print(result)


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    q = deque()
    for _ in range(M):
        q.append(list(map(int, sys.stdin.readline().split())))
    solution()





