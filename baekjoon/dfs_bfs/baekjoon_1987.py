import sys
from typing import List


def backtracking(y: int, x: int, count: int, visit: List, graph: List[List]):
    global result
    visit[ord(graph[y][x]) - 65] = True
    result.add(count)

    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if -1 < ny < r and -1 < nx < c and not visit[ord(graph[ny][nx]) - 65]:
            backtracking(ny, nx, count+1, visit, graph)
            visit[ord(graph[ny][nx]) - 65] = False


r, c = map(int, sys.stdin.readline().split())

result = set()
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
grid, visited = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)], [False] * 26
backtracking(0, 0, 1, visited, grid)
print(max(result))

