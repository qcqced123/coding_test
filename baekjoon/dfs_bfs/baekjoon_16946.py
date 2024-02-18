import sys
from collections import deque
from typing import List


def bfs(y: int, x: int, graph: List[List]) -> int:
    visit, count = set(), 1
    visit.add((y, x))
    q = deque([(y, x)])
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    while q:
        vy, vx = q.popleft()
        for i in range(4):
            ny, nx = dy[i] + vy, dx[i] + vx
            if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and (ny, nx) not in visit and not graph[ny][nx]:
                count += 1
                visit.add((ny, nx))
                q.append((ny, nx))
    return count


def solution():
    N, M = map(int, sys.stdin.readline().split())
    grid, walls = [], set()
    for i in range(N):
        col = list(map(int,
                       sys.stdin.readline().rstrip()))
        grid.append(col)
        for j in range(M):
            if col[j] == 1:
                walls.add((i, j))

    for coordinate in walls:
        y, x = coordinate
        grid[y][x] = bfs(y, x, grid) % 10

    for i in range(N):
        print(''.join(map(str, grid[i])), end='\n')


if __name__ == "__main__":
    solution()
