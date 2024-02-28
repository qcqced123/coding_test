import sys
import copy
from collections import deque
from typing import List, Set


def solution():
    sys.setrecursionlimit(10**6)
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dy, dx, result = (-1, 1, 0, 0), (0, 0, -1, 1), [0]

    def calculate(arr: List[List]):
        total = 0
        for i in range(N):
            for j in range(N):
                total = max(total, arr[i][j])
        return total

    def bfs(y: int, x: int, d: int, visited: Set, graph: List[List]):
        q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            ny, nx = dy[d] + vy, dx[d] + vx
            if -1 < ny < N and -1 < nx < N and graph[ny][nx] == graph[vy][vx] and (ny, nx) not in visited:
                graph[ny][nx] += graph[vy][vx]
                graph[vy][vx] = 0
                visited.add((ny, nx))
                return

            if -1 < ny < N and -1 < nx < N and not graph[ny][nx]:
                graph[ny][nx] = graph[vy][vx]
                graph[vy][vx] = 0
                q.append((ny, nx))

    def move(d, arr: List[List]):
        curr = copy.deepcopy(arr)  # copy current state of graph
        visit = set()
        if d == UP or d == DOWN:
            if d == UP:
                for r in range(N):
                    for c in range(N):
                        if curr[r][c]:
                            bfs(r, c, d, visit, curr)
            elif d == DOWN:
                for r in range(N-1, -1, -1):
                    for c in range(N):
                        if curr[r][c]:
                            bfs(r, c, d, visit, curr)
        else:
            if d == LEFT:
                for c in range(N):
                    for r in range(N):
                        if curr[r][c]:
                            bfs(r, c, d, visit, curr)
            elif d == RIGHT:
                for c in range(N-1, -1, -1):
                    for r in range(N):
                        if curr[r][c]:
                            bfs(r, c, d, visit, curr)
        return curr

    def backtracking(arr: List[List], count: int):
        if count == 5:
            result[0] = max(result[0], calculate(arr))
            return

        for i in range(4):
            curr = move(i, arr)
            backtracking(curr, count+1)

    backtracking(grid, 0)
    print(result[0])


if __name__ == "__main__":
    solution()
