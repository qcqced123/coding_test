import sys


def is_safe(row: int, col: int, left_diagonal: int, right_diagonal: int, column_set: int) -> bool:
    return not (column_set & (1 << col)) and not (left_diagonal & (1 << (row + col))) and not (right_diagonal & (1 << (row - col + N - 1)))


def backtracking(row: int, left_diagonal: int, right_diagonal: int, column_set: int) -> None:
    if row == N:
        result[0] += 1
        return

    for col in range(N):
        if is_safe(row, col, left_diagonal, right_diagonal, column_set):
            backtracking(row + 1, left_diagonal | (1 << (row + col)), right_diagonal | (1 << (row - col + N - 1)), column_set | (1 << col))


N = int(sys.stdin.readline())
result = [0]
backtracking(0, 0, 0, 0)
print(result[0])
