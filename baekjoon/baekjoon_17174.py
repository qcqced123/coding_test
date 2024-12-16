import sys
from collections import deque


def solution():
    """
    idea: bfs
        - bfs 쓰는게 훨씬 간단함
    """
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (0, 1), (1, 0)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # do bfs
    q = deque([(0,0)])
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    while q:
        vy, vx = q.popleft()
        vw = grid[vy][vx]
        for i in range(2):
            ny, nx = vy + dy[i]*vw, vx + dx[i]*vw
            if ny == N-1 and nx == N-1:
                print("HaruHaru")
                return

            if -1 < ny < N and -1 < nx < N and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1

    print("Hing")


if __name__ == "__main__":
    solution()
