import sys


def solution():
    char1 = list('%' + sys.stdin.readline().rstrip())
    char2 = list('%' + sys.stdin.readline().rstrip())

    grid, dp = [[0]*len(char2) for _ in range(len(char1))], [['']*len(char2) for _ in range(len(char1))]
    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            if char1[r] != char2[c]:
                if grid[r-1][c] >= grid[r][c-1]:
                    grid[r][c] = grid[r-1][c]
                    dp[r][c] = dp[r-1][c]
                else:
                    grid[r][c] = grid[r][c-1]
                    dp[r][c] = dp[r][c-1]

            else:
                grid[r][c] = grid[r-1][c-1] + 1
                dp[r][c] = dp[r-1][c-1] + char1[r]

    print(grid[-1][-1], end='\n')
    print(dp[-1][-1])


if __name__ == "__main__":
    solution()
