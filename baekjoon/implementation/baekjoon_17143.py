import sys
from typing import List, Tuple


def update_state(y: int, x: int, w: int, s: int, d: int, graph: List[List]) -> Tuple:
    UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
    row, col = len(graph), len(graph[0])
    dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
    ny, nx = y + dy[d-1]*s, x + dx[d-1]*s  # s is nums of block
    if ny < 0 or ny > row-1 or nx < 0 or ny > col-1:
        cnt = s  # copy
        while cnt:
            if d == UP:
                ny = y + dy[d-1]*y
                cnt -= y

            elif d == DOWN:
                ny = y + dy[d-1] * y
                cnt -= row - y

            elif d == RIGHT:
                nx = x + dx[d-1] * x
                cnt -= col - x

            elif d == LEFT:
                nx = x + dx[d-1] * x
                cnt -= x

            if cnt:
                if d == UP:
                    d = DOWN

                elif d == DOWN:
                    d = UP

                elif d == RIGHT:
                    d = LEFT

                elif d == LEFT:
                    d = RIGHT

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
