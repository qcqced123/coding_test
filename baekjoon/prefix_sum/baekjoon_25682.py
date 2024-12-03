import sys
import copy
from collections import deque


def solution():
    """
    idea: prefix sum
        - 부분 중에서 최소를 고르는 문제 ~ 부분합
        - 2차원 테이블의 부분합 응용
        - bfs: 전체 그리드 대상, 규칙에 맞게 바꿔야 하는 위치 개수, 부분합으로 표현
            - 처음꺼 바꾸는 경우도 고려 (예제 3번)
        - 2d table prefix sum
    """
    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(input().rstrip()) for _ in range(N)]

    # do bfs for recording
    answer = INF
    for i in range(2):
        graph = copy.deepcopy(grid)
        q = deque([(0, 0)])
        cache = [[0] * M for _ in range(N)]
        if i == 1:
            cache[0][0] = 1
            graph[0][0] = "W" if graph[0][0] == "B" else "B"

        visited = [[0]*M for _ in range(N)]
        visited[0][0] = 1
        while q:
            vy, vx = q.popleft()
            vc = graph[vy][vx]
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
                    if vc == graph[ny][nx]:
                        graph[ny][nx] = "W" if vc == "B" else "B"
                        cache[ny][nx] = 1

                    q.append((ny, nx))
                    visited[ny][nx] = 1

        # init prefix sum array
        prefix = [[0]*(M+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, M+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + cache[i-1][j-1]

        # find the optimal solution
        for y in range(1, N-K+2):
            for x in range(1, M-K+2):
                ey = y+K-1
                ex = x+K-1
                cnt = prefix[ey][ex] - prefix[y-1][ex] - prefix[ey][x-1] + prefix[y-1][x-1]
                answer = min(answer, cnt)

    print(answer)


if __name__ == "__main__":
    solution()
