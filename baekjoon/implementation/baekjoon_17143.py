import sys
from typing import List, Tuple


def update_state(y: int, x: int, w: int, s: int, d: int, graph: List[List]) -> Tuple:
    row, col = len(graph), len(graph[0])
    dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
    ny, nx = y + dy[d-1]*s, x + dx[d-1]*s

    if ny < -1 or ny > row - 1 or nx < -1 or nx > col - 1:
        if y == 0 and d == 1:
            d = 2
        elif y == row - 1 and d == 2:
            d = 1
        elif x == 0 and d == 4:
            d = 3
        elif x == col - 1 and d == 3:
            d = 4

        if d == 1:
            d = 1 if int((s - y) // (row - 1)) % 2 else 2
            ny = (row - 1) - int((s - y) % (row - 1)) if d == 1 else int((s - y) % (row - 1))

        elif d == 2:
            d = 2 if int((s - (row - 1 - y)) // (row - 1)) % 2 else 1
            ny = int((s - (row - 1 - y)) % (row - 1)) if d == 2 else (row - 1) - int((s - (row - 1 - y)) % (row - 1))

        elif d == 3:
            d = 3 if int((s - (col - 1 - x)) // (col - 1)) % 2 else 4
            nx = int((s - (col - 1 - x)) % (col - 1)) if d == 3 else (col - 1) - int((s - (col - 1 - x)) % (col - 1))

        elif d == 4:
            d = 4 if int((s - x) // (col - 1)) % 2 else 3
            nx = (col - 1) - int((s - x) % (col - 1)) if d == 4 else int((s - x) % (col - 1))

    new_state = (ny, nx, s, d, w)
    graph[y][x][0], graph[y][x][1], graph[y][x][2] = 0, 0, 0
    return new_state


def moving_shark(graph: List[List]):
    tmp = []
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            speed, direction, size = graph[r][c][0], graph[r][c][1], graph[r][c][2]
            if size:
                tmp.append(update_state(r, c, size, speed, direction, graph))
                continue
    return tmp


def nearest_shark(x: int, graph: List[List]) -> int:
    weight = 0
    for i in range(len(graph)):
        direction, size = graph[i][x][1], graph[i][x][2]
        if size:
            weight += size
            graph[i][x][0], graph[i][x][1], graph[i][x][2] = 0, 0, 0
            return weight
    return 0


def solution():
    R, C, M = map(int, sys.stdin.readline().split())
    grid = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, sys.stdin.readline().split())
        grid[r-1][c-1][0], grid[r-1][c-1][1], grid[r-1][c-1][2] = s, d, z  # speed, direction, size

    timer, result = 0, 0
    while timer != C:
        result += nearest_shark(timer, grid)
        test = moving_shark(grid)
        for state in test:
            ny, nx, ns, nd, nw = state
            if nw > grid[ny][nx][2]:
                grid[ny][nx][0], grid[ny][nx][1], grid[ny][nx][2] = ns, nd, nw
        timer += 1
    print(result)


if __name__ == "__main__":
    solution()
