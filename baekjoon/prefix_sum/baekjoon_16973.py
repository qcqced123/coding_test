import sys
from collections import deque


def solution():
    """
    idea: bfs with prefix sum
        - 직사각형 왼쪽 모서리 상단을 기준으로 bfs 수행
            - 현재 위치가 유효한지 판정:
                - 부분합 이용해, 내부에 벽이 있는지 없는지 검사
                - 없으면 가능한 위치
                - 있으면 불가능한 위치
    implementation:
        - bfs
    """
    # helper func
    def is_valid(y1, x1, y2, x2) -> int:
        cnt = prefix[y2+1][x2+1] - prefix[y1][x2+1] - prefix[y2+1][x1] + prefix[y1][x1]
        return 1 if not visited[y1][x1] and not grid[ny][nx] and not cnt else 0

    # init data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    prefix = [[0] * (M+1) for _ in range(N+1)]
    grid = [list(map(int, input().split())) for _ in range(N)]
    H, W, src_y, src_x, end_y, end_x = map(int, input().split())

    src_y -= 1
    src_x -= 1
    end_y -= 1
    end_x -= 1

    # init prefix table
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # do bfs with prefix sum
    q = deque([(src_y, src_x, 0)])
    visited = [[0]*M for _ in range(N)]
    visited[src_y][src_x] = 1
    while q:
        vy, vx, vc = q.popleft()
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            ey = ny + H - 1
            ex = nx + W - 1
            if -1 < ny < N and -1 < nx < M and -1 < ey < N and -1 < ex < M and is_valid(ny, nx, ey, ex):
                nc = vc + 1
                if ny == end_y and nx == end_x:
                    print(nc)
                    return

                visited[ny][nx] = 1
                q.append((ny, nx, nc))
    print(-1)


if __name__ == "__main__":
    solution()
