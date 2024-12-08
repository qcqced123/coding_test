import sys


def solution():
    """
    idea: dynamic programming
        - overlapping:
        - caching data:
        - data structure:
    """
    input = sys.stdin.readline
    for _ in range(int(input())):
        N = int(input())
        coins = list(map(int, input().split()))
        M = int(input())

        # update dp cache
        dp = [[0]*(M+1) for _ in range(N+1)]
        for i in range(1, N+1):
            cnt = coins[i - 1]
            for j in range(1, M + 1):
                if not j % cnt:
                    dp[i][j] += 1

        for i in range(1, N+1):
            cnt = coins[i-1]
            for j in range(1, M+1):
                dp[i][j] += dp[i-1][j]
                if dp[i-1][j] and j+cnt <= M:
                    dp[i][j+cnt] += dp[i-1][j]*dp[i][cnt]

        # check current state of dp cache
        for i in range(N + 1):
            print(dp[i], end='\n')


if __name__ == "__main__":
    solution()
