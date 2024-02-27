import sys
from collections import deque
from typing import List


def solution():
    N, M = map(int, sys.stdin.readline().split())
    grid, counter = [], 0
    for i in range(N):
        col = list(map(str, sys.stdin.readline().rstrip()))
        grid.append(col)
        for j in range(M):
            if col[j] == 'B':
                blue = (i, j)
            elif col[j] == 'R':
                red = (i, j)
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    def dfs(y: int, x: int, d: int, graph: List[List]):
        ny, nx = dy[d] + y, dx[d] + x
        if -1 < ny < N and -1 < nx < M:
            if graph[ny][nx] == 'O':  # meet hole
                return True

            if graph[ny][nx] == '.':
                dfs(ny, nx, d, graph)
        return False
    def bfs(y: int, x: int, graph: List[List]):
        visit, q = {(y, x)}, deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                print(dfs(vy, vx, i, graph))

    red_y, red_x = red
    bfs(red_y, red_x, grid)


if __name__ == "__main__":
    solution()
