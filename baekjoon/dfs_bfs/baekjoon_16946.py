import sys
from collections import deque


def bfs(y: int, x: int, z: int, graph, visited, area_dict):
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    visited[y][x], graph[y][x], total = True, z, 1
    q = deque([(y, x)])
    while q:
        vy, vx = q.popleft()
        for i in range(4):
            ny, nx = dy[i] + vy, dx[i] + vx
            if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and not visited[ny][nx] and not graph[ny][nx]:
                total += 1
                q.append((ny, nx))
                visited[ny][nx] = True
                graph[ny][nx] = z
    area_dict[z] = total


def calculate(y: int, x: int, graph, area_dict):
    group_set = set()
    graph[y][x] = 1
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and graph[ny][nx] < -1:
            area = graph[ny][nx]
            group_set.add(area)

    for k in group_set:
        graph[y][x] += area_dict[k]
    graph[y][x] %= 10


def solution():
    N, M = map(int, sys.stdin.readline().split())
    grid, areas, walls, visit = [], set(), set(), [[False] * M for _ in range(N)]
    for i in range(N):
        col = list(map(int, sys.stdin.readline().rstrip()))
        grid.append(col)
        for j in range(M):
            if not col[j]:
                areas.add((i, j))

            elif col[j] == 1:
                grid[i][j] = -1
                walls.add((i, j))
    area = {}
    area_num = -2
    for coordinate in areas:
        r, c = coordinate
        if not grid[r][c]:
            bfs(r, c, area_num, grid, visit, area)
            area_num -= 1

    for coordinate in walls:
        y, x = coordinate
        calculate(y, x, grid, area)

    for r in range(N):  # 여기도 최적화 가능할 것 같고
        for c in range(M):
            if grid[r][c] < 0:
                grid[r][c] = 0

    for i in range(N):
        print(''.join(map(str, grid[i])), end='\n')


if __name__ == "__main__":
    solution()
