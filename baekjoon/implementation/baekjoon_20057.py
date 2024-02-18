import sys


def calculate(send, y, x, d, graph) -> int:
    total, remove = 0, 0
    move = (
        ((-1, 1), (-1, 0), (-1, -1), (-2, 0), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)),  # left
        ((-1, -1), (0, -1), (1, -1), (0, -2), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)),   # down
        ((-1, 1), (-1, 0), (-1, -1), (-2, 0), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0)),   # right
        ((1, 1), (0, 1), (-1, 1), (0, 2), (-2, 0), (-1, -1), (0, -1), (1, -1), (0, -2)),  # up
    )
    rdy, rdx = (0, 1, 0, -1), (-1, 0, 1, 0)
    ratio = (0.01, 0.07, 0.1, 0.02, 0.05, 0.1, 0.07, 0.01, 0.02)
    for i in range(9):
        tmp = int(send*ratio[i])
        remove += tmp
        ny, nx = y + move[d][i][0], x + move[d][i][1]
        if -1 < ny < len(graph) and -1 < nx < len(graph[0]):
            graph[ny][nx] += tmp
        else:
            total += tmp
    ry, rx = y + rdy[d], x + rdx[d]
    if -1 < ry < len(graph) and -1 < rx < len(graph[0]):
        graph[ry][rx] += send - remove
    else:
        total += send - remove
    graph[y][x] = 0
    return total


def solution():
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    y, x, d, count, span = int((N-1) / 2), int((N-1) / 2), 0, 2, 1
    dy, dx = (0, 1, 0, -1), (-1, 0, 1, 0)
    result = 0
    while True:
        for _ in range(span):
            nd = d % 4
            ny, nx = y + dy[nd], x + dx[nd]
            rest = grid[ny][nx]
            result += calculate(rest, ny, nx, nd, grid)

            y, x = ny, nx
            if not y and not x:
                print(result)
                exit()

        d += 1
        count -= 1
        if not count:
            span += 1
            count = 2


if __name__ == "__main__":
    solution()
