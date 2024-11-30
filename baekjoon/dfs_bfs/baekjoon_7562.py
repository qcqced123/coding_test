import sys
from collections import deque


def solution():
    """ 나이트 이동
    idea: bfs
        - 최소 이동 횟수
    """
    # init the data structure
    input = sys.stdin.readline
    dy, dx = (-1, -2, -2, -1, 1, 2, 2, 1), (-2, -1, 1, 2, 2, 1, -1, -2)
    for _ in range(int(input())):
        N = int(input())
        src_y, src_x = map(int, input().split())
        end_y, end_x = map(int, input().split())

        # do bfs
        q = deque([(src_y, src_x, 0)])
        visited = [[0]*N for _ in range(N)]
        visited[src_y][src_x] = 1
        while q:
            vy, vx, vc = q.popleft()
            if vy == end_y and vx == end_x:
                print(vc)
                break

            for i in range(8):
                ny, nx, nc = vy + dy[i], vx + dx[i], vc + 1
                if -1 < ny < N and -1 < nx < N and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx, nc))


if __name__ == "__main__":
    solution()
