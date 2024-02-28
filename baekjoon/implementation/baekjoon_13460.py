import sys
import copy
from collections import deque
from typing import List, Set


def solution():
    N, M = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(N):
        col = list(map(str, sys.stdin.readline().rstrip()))
        grid.append(col)
        for j in range(M):
            if col[j] == 'B':
                blue = (i, j)
            elif col[j] == 'R':
                red = (i, j)
    dy, dx, result = (-1, 1, 0, 0), (0, 0, -1, 1), [11]

    def bfs(y: int, x: int, d: int, visited: Set, graph: List[List]):
        q = deque([(y, x)])
        visited.add((graph[y][x], y, x))
        while q:
            vy, vx = q.popleft()
            ny, nx = dy[d] + vy, dx[d] + vx
            if 0 < ny < N - 1 and 0 < nx < M - 1 and graph[ny][nx] == 'B':
                return 2

            if 0 < ny < N-1 and 0 < nx < M-1 and graph[ny][nx] == 'O':
                graph[vy][vx] = '.'
                return 1

            if 0 < ny < N-1 and 0 < nx < M-1 and graph[ny][nx] == '.' and (graph[ny][nx], ny, nx) not in visited:
                graph[ny][nx] = graph[vy][vx]
                graph[vy][vx] = '.'
                visited.add((graph[ny][nx], ny, nx)), q.append((ny, nx))
        return 0

    def backtracking(ry, rx, by, bx, arr: List[List], count: int):
        if count == 11:
            return

        for i in range(4):
            curr = copy.deepcopy(arr)
            visit = set()  # red, blue
            rf = bfs(ry, rx, i, visit, curr)
            bf = bfs(by, bx, i, visit, curr)
            if rf == 2:
                curr[]

            for j in range(N):
                print(curr[j], end='\n')
            if rf == 1:
                print(count+1)

    backtracking(red[0], red[1], blue[0], blue[1], grid, 0)


if __name__ == "__main__":
    solution()
