import sys
from collections import deque


def solution():
    """
    idea: graph search with adj array
        - 가장 큰 영역 찾기
        - bfs
            - 음식물 조각 위치마다 bfs 수행
    """
    # bfs func
    def bfs(y: int, x: int) -> int:
        nums = 1
        q = deque([(y,x)])
        visited[y][x] = 1
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M and not visited[ny][nx] and grid[ny][nx] == "#":
                    nums += 1
                    q.append((ny,nx))
                    visited[ny][nx] = 1
        return nums

    # init the data
    input = sys.stdin.readline
    N, M, K = map(int, input().split())  # row, col, trash
    grid = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    # make the adj array
    src_point = []
    for _ in range(K):
        i, j = map(int, input().split())  # row, col, trash
        src_point.append((i-1, j-1))
        grid[i-1][j-1] = "#"

    # do bfs
    answer = 0
    for y, x in src_point:
        if not visited[y][x]:
            answer = max(answer, bfs(y, x))

    print(answer)


if __name__ == "__main__":
    solution()
