import sys
from collections import deque


def solution():
    """
    idea 1: bfs
        - 일단 벽이고 뭐고 도착지로 이동
        - 이동 끝나고 벽 몇 개 없앴는지 확인하고 K개 이하만 정답 갱신에 반영
        - 최적화 하게, 현재 경로가 현재 최단 경로 값보다 커지면, pruning
        - 큐에 경로 길이랑, 벽 부순거 다 넣으면 터지지 않을까

    idea 2: bfs with 3d cache
        - visited[n][n][k]
    """
    # get input
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    # do bfs
    answer = INF
    q = deque([(0, 0, 0)])
    visited = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        vy, vx, vk = q.popleft()
        vl = visited[vy][vx][vk]
        if vy == N-1 and vx == M-1 and vk <= K:
            answer = min(answer, vl)
            continue

        for i in range(4):
            ny, nx, nk = vy + dy[i], vx + dx[i], vk
            if -1 < ny < N and -1 < nx < M:
                if grid[ny][nx] == 1 and nk+1 <= K and vl + 1 < visited[ny][nx][nk+1]:
                    q.append((ny, nx, nk + 1))
                    visited[ny][nx][nk+1] = vl + 1

                elif not grid[ny][nx] and vl + 1 < visited[ny][nx][nk]:
                    q.append((ny, nx, nk))
                    visited[ny][nx][nk] = vl + 1

    print(answer) if answer != INF else print(-1)


if __name__ == "__main__":
    solution()
