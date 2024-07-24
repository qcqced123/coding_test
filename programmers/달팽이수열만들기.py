from typing import Tuple, List


def solution(n):
    cnt = 1
    src_row, end_row = 0, n-1
    src_col, end_col = 0, n-1
    result = [[0]*n for _ in range(n)]

    while src_row <= end_row and src_col <= end_col:
        # fill the first row of current square
        for i in range(src_col, end_col+1):
            result[src_row][i] = cnt
            cnt += 1

        src_row += 1

        # fill the last col of current square
        for j in range(src_row, end_row+1):
            result[j][end_col] = cnt
            cnt += 1

        end_col -= 1

        # fill the last row of current square
        for k in range(end_col, src_col-1, -1):
            result[end_row][k] = cnt
            cnt += 1

        end_row -= 1

        # fill the first col of current square
        for l in range(end_row, src_row-1, -1):
            result[l][src_col] = cnt
            cnt += 1

        src_col += 1
    return result


if __name__ == '__main__':
    n = 4
    matrix = solution(n)
    for i in range(n):
        print(matrix[i], end='\n')
