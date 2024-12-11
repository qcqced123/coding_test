import sys


def solution():
    """
    idea: dynamic programming
        - dp[i][j] = grid[i][j] + max(dp[i][j-1], dp[i-1][j])
    """
    # init structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dp = [[0]*M for _ in range(N)]
    grid = [tuple(map(int, input().split())) for _ in range(N)]

    # init dynamic programming
    dp[0][0] = grid[0][0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, M):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    # update dynamic programming
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = grid[i][j] + max(dp[i][j-1], dp[i-1][j])

    print(dp[-1][-1])


if __name__ == "__main__":
    solution()
