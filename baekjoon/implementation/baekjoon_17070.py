import sys


def solution():
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]  # 방향, 행, 열

    dp[0][0][1] = 1
    for c in range(2, N):
        if dp[0][0][c-1] and not grid[0][c]:
            dp[0][0][c] = 1

    for r in range(1, N):
        for c in range(2, N):
            if not grid[r][c]:
                if not grid[r-1][c-1] and not grid[r-1][c] and not grid[r][c-1]:  # 대각선
                    dp[2][r][c] += dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

                if dp[0][r][c-1]:  # 가로 케이스 1
                    dp[0][r][c] += dp[0][r][c-1]

                if dp[2][r][c-1]:  # 가로 케이스 2
                    dp[0][r][c] += dp[2][r][c-1]

                if dp[1][r-1][c]:  # 세로 케이스 1
                    dp[1][r][c] += dp[1][r-1][c]

                if dp[2][r-1][c]:  # 세로 케이스 2
                    dp[1][r][c] += dp[2][r-1][c]

    print(dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1])


if __name__ == "__main__":
    solution()
