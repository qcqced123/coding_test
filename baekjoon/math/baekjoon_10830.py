import sys
from typing import List


def solution():
    sys.setrecursionlimit(10**6)
    N, B = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    def matrix_square(a: List[List], b: List[List]) -> List[List]:
        cache = [[0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                for k in range(N):
                    cache[r][c] += a[r][k] * b[k][c]
                cache[r][c] %= 1000
        return cache

    def power(x: List[List], curr: int):
        if curr == 1:
            return x
        tmp = power(x, curr // 2)
        if not curr % 2:
            return matrix_square(tmp, tmp)
        else:
            return matrix_square(matrix_square(tmp, tmp), x)

    result = power(matrix, B)

    for i in range(N):
        for j in range(N):
            result[i][j] = result[i][j] % 1000
        print(*result[i], end='\n')


if __name__ == "__main__":
    solution()
