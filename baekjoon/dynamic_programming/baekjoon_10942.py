import sys


def solution():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))  # for matching number of index
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for j in range(1, N):
        if arr[j-1] == arr[j]:
            dp[j-1][j] = 1

    for k in range(2, N):
        for t in range(k, N):
            if arr[t-k] == arr[t] and dp[t-k+1][t-1]:
                dp[t-k][t] = 1

    M = int(sys.stdin.readline())
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        print(dp[start-1][end-1])


if __name__ == "__main__":
    solution()
