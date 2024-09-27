import sys
from typing import List


def solution():
    """ 왼쪽 to 가장 아래
    방향: 오른쪽, 아래
    원소: 이동 칸
    이동 중, 방향 변경 불가

    idea: dynamic programming
        1)
    """
    def is_valid(y: int, x: int) -> bool:
        return -1 < y < N and -1 < x < N

    N = int(input())
    dp = [[0]*N for _ in range(N)]
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # initialize the setting
    # for-loop
    dp[0][0] = 1
    for y in range(N):
        for x in range(N):
            # add right direction and down direction
            if grid[y][x] and dp[y][x]:
                # for right direction, 격자 넘어갈 수도 ?
                rny, rnx = y, x + grid[y][x]
                if is_valid(rny, rnx):
                    dp[rny][rnx] += dp[y][x]

                dny, dnx = y + grid[y][x], x
                if is_valid(dny, dnx):
                    dp[dny][dnx] += dp[y][x]

    print(dp[-1][-1])


if __name__ == "__main__":
    solution()
