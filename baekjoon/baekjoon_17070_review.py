import sys
from typing import List


def solution():
    """ 유니크한 파이프 시퀀스 개수, 방향 3개, 16*16
    확장 논리로 접근, optimal sub-structure & overlapping sub-problem 특징이 모두 드러남
    현재 시퀀스의 값은 이전 시퀀스의 방향에 의해 결정

    idea: dynamic programming
    """

    N = int(input())
    dp = [[[0]*3 for _ in range(N)] for _ in range(N)]  # 가로, 세로, 대각선
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # initialize first row
    dp[0][1][0] = 1
    for i in range(1, N):
        if not grid[0][i] and dp[0][i-1][0]:
            dp[0][i][0] = 1

    # calculate the others
    for d in range(3):
        for y in range(1, N):
            for x in range(2, N):
                # 가로 & 세로 방향 처리
                if not grid[y][x]:
                    dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]  # 왼쪽 원소의 가로 방향 개수 + 대각선 방향 개수
                    dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]

                    # 대각 방향 처리
                    if not grid[y-1][x] and not grid[y][x-1]:
                        dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]
    print(sum(dp[-1][-1]))


if __name__ == "__main__":
    solution()
