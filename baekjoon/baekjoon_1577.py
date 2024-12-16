import sys


def solution():
    """
    idea: dynamic programming
    question:
        - 공사중인 곳 초기화 하는 방법을 모르겠음
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dp = [[1]*(N+1) for _ in range(M+1)]

    # 여기가 관건인데 모르겠음
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2: x2 = x1
        if y1 > y2: y2 = y1
        dp[y2][x2] = 0

    # init dp cache
    for i in range(1, M+1):
        if not dp[i-1][0]:
            dp[i][0] = 0

    for i in range(1, N+1):
        if not dp[0][i-1]:
            dp[0][i] = 0

    # update dp cache
    for i in range(1, M+1):
        for j in range(1, N+1):
            if dp[i][j]:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # for i in range(M+1):
    #     print(dp[i], end="\n")
    print(dp[-1][-1])

if __name__ == "__main__":
    solution()
