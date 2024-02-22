import sys
from typing import List


def solution():
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[[[0] for _ in range(N)] for _ in range(N)] for _ in range(3)]  # 방향, 행, 열

    dp[0][0][0], dp[0][0][1] = 1, 1
    for r in range(2, N):
        if dp[0][0][r-1]:
            dp[0][0][r] = 1

    for k in range(3):
        for r in range(1, N):
            for c in range(2, N):
                if not k:
                    

                elif k == 1:
                    pass
                else:
                    pass



if __name__ == "__main__":
    solution()
