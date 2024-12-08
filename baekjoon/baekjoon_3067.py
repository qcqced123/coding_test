import sys


def solution():
    """
    idea: dynamic programming
        - overlapping:
            - dp[i][j] += dp[i-1][j]
            - if not j % cnt, dp[i][j] += 1
            -
        - caching data:
            - dp[i][j]: consider i-th coins, all of case of current sum of j
        - data structure: 2d array
    """
    input = sys.stdin.readline
    for _ in range(int(input())):
        N = int(input())
        coins = list(map(int, input().split()))
        M = int(input())

        # update dp cache
        dp = [[0]*(M+1) for _ in range(N+1)]
        for i in range(1, N+1):
            cnt = coins[i-1]
            for j in range(1, M+1):
                d, r = divmod(j, cnt)
                for k in range(1, d+1):
                    dp[i][j] = max(dp[i][j], dp[i][cnt*k]*dp[i-1][j-cnt*k])

                # dp[i][j] += dp[i-1][j]
                if not r:
                    dp[i][j] += 1

        # check current state of dp cache
        # for i in range(N + 1):
        #     print(dp[i], end='\n')
        print(dp[-1][-1])

if __name__ == "__main__":
    solution()
