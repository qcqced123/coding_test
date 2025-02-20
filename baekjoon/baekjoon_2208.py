import sys


def solution():
    """
    idea: prefix sum + dynamic programming
        -
    limit: NlogN
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + [int(input()) for _ in range(N)]

    # init prefix sum array
    prefix = [0]*(N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + arr[i]

    # update the dp cache
    dp = [0]*(N+1)
    for i in range(M, N+1):
        for j in range(i-M):
            dp[i] = max(dp[i], prefix[i]-prefix[i-M-j])

    print(max(dp))


if __name__ == "__main__":
    solution()
