import copy
from typing import Tuple, List


def solution(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """ mxn, nxk
    3x4, 4x5
    a의 행 기준으로 첫 루프 잡고


    """
    row, col = len(matrix1), len(matrix2[0])
    result = [[0]*col for _ in range(row)]

    def matmul() -> None:
        for i in range(row):
            for j in range(col):
                cnt = 0
                for k in range(len(matrix1[0])):
                    cnt += matrix1[i][k] * matrix2[k][j]

                result[i][j] = cnt

    def transpose() -> None:
        temp = copy.deepcopy(result)
        for i in range(row):
            for j in range(col):
                if i == j:
                    continue
                result[i][j] = temp[j][i]

    matmul()
    transpose()
    return result


if __name__ == '__main__':
    A, B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    grid = solution(A, B)

    for i in range(len(grid)):
        print(grid[i], end='\n')
