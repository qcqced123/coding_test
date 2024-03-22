import sys
from collections import deque


def solution():
    EAST, WEST, NORTH, SOUTH = 0, 1, 2, 3

    N, M, Y, X, K = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    moves = list(map(int, sys.stdin.readline().split()))
    moves.reverse()
    dice_row, dice_col = deque([[2, 0], [1, 0], [5, 0], [6, 0]]), deque([[4, 0], [1, 0], [3, 0], [6, 0]])  # key, value

    def rolling(d: int):
        if d == EAST:
            dice_col.rotate(1)
            dice_row[1], dice_row[3] = dice_col[1], dice_col[3]

        elif d == WEST:
            dice_col.rotate(-1)
            dice_row[1], dice_row[3] = dice_col[1], dice_col[3]

        elif d == NORTH:
            dice_row.rotate(-1)
            dice_col[1], dice_col[3] = dice_row[1], dice_row[3]

        elif d == SOUTH:
            dice_row.rotate(1)
            dice_col[1], dice_col[3] = dice_row[1], dice_row[3]

    def update(y: int, x: int):
        curr = grid[y][x]
        if curr:
            dice_row[3][1], dice_col[3][1] = curr, curr
            grid[y][x] = 0

        else:
            grid[y][x] = dice_row[3][1]

    dy, dx = (0, 0, -1, 1), (1, -1, 0, 0)
    while moves:
        vd = moves.pop() - 1
        ny, nx = dy[vd] + Y, dx[vd] + X
        if -1 < ny < N and -1 < nx < M:
            rolling(vd)
            update(ny, nx)

            Y, X = ny, nx
            print(dice_row[1][1])


if __name__ == "__main__":
    solution()
