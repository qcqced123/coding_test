import sys


def solution():
    """
    idea: prefix sum + dynamic programming
        - dp[i]: ith 까지 고려한 경우의 최대값

    limit: NlogN
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + [int(input()) for _ in range(N)]

    print(arr)

    # init prefix sum array
    prefix = [0]*(N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + arr[i]

    print(prefix)


if __name__ == "__main__":
    solution()
