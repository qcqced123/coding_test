import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens_util(board, row, n, count):
    if row == n:
        # 모든 퀸을 놓았을 때, 해의 개수를 증가시킴
        count[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, count)
            board[row][col] = 0  # Backtrack


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    count = [0]  # 해의 개수를 저장하기 위한 리스트
    solve_n_queens_util(board, 0, n, count)
    return count[0]


result = solve_n_queens(int(sys.stdin.readline()))
print(result)
