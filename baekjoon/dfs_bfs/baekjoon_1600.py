import sys
from collections import deque


def solution():
    """ 말 따라 하기, 말 == 나이트, 시작 to 종점, 최소 횟수
    제약 조건: k번

    저 제약 조건을 어찌할 것인가, 내 생각에 3차원 visited 배열..?
    앞에 K 몇번째로 도달했는지 그런거

    idea: bfs
        - 격자 이동 방식 추가
        - if queue is not empty and the player get to the final point, print answer
        - else print -1
        - 3D visited array
            - R, C, K
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    K = int(input())
    C, R = map(int, input().split())
    visited = [[[INF]*(K+1) for _ in range(C)] for _ in range(R)]
    grid = [list(map(int, input().split())) for _ in range(R)]

    # define the monkey's move direction with knight moving
    # index of 4 ~ 11 is the knight moving, having a constraint
    dy = (-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1)
    dx = (0, 0, -1, 1, -2, -1, 1, 2, 2, 1, -1, -2)

    # do bfs
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 0
    while q:
        vy, vx, vk = q.popleft()  # vk is the how many
        for i in range(12):
            ny, nx, nk = vy + dy[i], vx + dx[i], vk  # 제약 조건 카운팅 부분 수 정
            if i >= 4 and nk + 1 > K:
                continue

            elif i >= 4 and nk + 1 <= K:
                nk = vk + 1

            if ny == R - 1 and nx == C - 1:
                visited[ny][nx][nk] = visited[vy][vx][vk] + 1
                print(visited[ny][nx][nk])
                return

            if -1 < ny < R and -1 < nx < C and not grid[ny][nx]:
                cnt = visited[vy][vx][vk] + 1
                if cnt < visited[ny][nx][nk]:
                    visited[ny][nx][nk] = cnt
                    q.append((ny, nx, nk))

    # cannot move to final or edge case (grid size is 1)
    answer = INF
    for i in range(K+1):
        answer = min(answer, visited[-1][-1][i])

    print(answer if answer != INF else -1)


if __name__ == "__main__":
    solution()
