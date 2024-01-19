import sys


def is_safe(r: int, c: int) -> bool:
    for row in range(N):
        if grid[row][c]:
            return False
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if grid[i][j]:
            return False
    for i, j in zip(range(r, -1, -1), range(c, N)):
        if grid[i][j]:
            return False
    return True


def backtracking(y: int, x: int) -> None:
    if y == N:
        result[0] += 1
        return

    for col in range(N):

        if is_safe(y, col):
            grid[y][col] = 1
            backtracking(y+1, col)
            grid[y][col] = 0  # for backtracking


sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
grid, result = [[0]*N for _ in range(N)], [0]

for first_col in range(N):
    grid[0][first_col] = 1
    backtracking(1, first_col)  # input number of next row
    grid[0][first_col] = 0  # for backtracking
print(result[0])
