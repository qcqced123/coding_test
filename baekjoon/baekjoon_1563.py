import sys


def solution():
    """ 개근상: 지각 두번 이상 X, 결석 3연속 X
    idea: dynamic programming
        - 3차원 dp cache
    """
    input = sys.stdin.readline
    N = int(input())
    dp = [[[0, 0, 0] for _ in range(2)] for _ in range(N+1)]

    # update dynamic programming
    # dp[i][j][0]: 직전에 출석, dp[i][j][1]: 지각, dp[i][j][2]: 직전에 결석
    dp[1][0] = [1,0,1]
    dp[1][1] = [1,1,1]


if __name__ == "__main__":
    solution()
