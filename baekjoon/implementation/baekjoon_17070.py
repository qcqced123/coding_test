import sys
from typing import List


def solution():
    N = int(sys.stdin.readline())
    grid, dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)], [[0]*N for _ in range(N)]

    for c in range(N):
        if not grid[0][c]:
            dp[0][c] = 1
    for c in range(2, N):
        if not grid[1][c] and not grid[1][c-1] and not grid[0][c]:
            dp[1][c] = 1

    for i in range(len(grid)):
        print(grid[i], end='\n')

    for i in range(len(dp)):
        print(dp[i], end='\n')


    for i in range(2, N):
        for j in range(2, N):
            if grid[i][j] == 1:
                continue
            dp[i][j] = dp[i][j-1]  # 가로
            pass





if __name__ == "__main__":
    solution()
