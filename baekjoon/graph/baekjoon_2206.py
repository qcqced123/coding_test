import sys
from collections import deque
from typing import List


def bfs(y: int, x: int, visited: List[List[List]], graph: List[List]) -> int:
    visited[y][x][0] = 1
    q = deque([(0, y, x)])  # broken wall, distance, y, x
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    while q:
        vw, vy, vx = q.popleft()
        if vy == len(graph) - 1 and vx == len(graph[0]) - 1:
            return visited[vy][vx][vw]

        for i in range(4):
            ny, nx = dy[i] + vy, dx[i] + vx
            if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and not visited[ny][nx][vw] and not graph[ny][nx]:
                visited[ny][nx][vw] = visited[vy][vx][vw] + 1
                q.append((vw, ny, nx))
            elif -1 < ny < len(graph) and -1 < nx < len(graph[0]) and not vw and graph[ny][nx]:
                visited[ny][nx][vw+1] = visited[vy][vx][vw] + 1
                q.append((vw+1, ny, nx))
    return -1


def solution():
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    print(bfs(0,0, visit, grid))


if __name__ == '__main__':
    solution()
