import sys


def solution():
    """
    idea: prefix sum + dynamic programming
        - dp[i] = max(dp[i-1] + arr[i], arr[i])
            - if dp[i-1]'s window size is larger than M
    limit: NlogN
    result:
        - 22% 틀림

    feedback:
        - 카운터 변수 쓰면서, 초기화할 때, 원소 1개의 합으로 초기화 하지 말고, 그냥 고정된 윈도우 크기의 합으로 초기화!

    """
    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + [int(input()) for _ in range(N)]

    # init prefix sum
    prefix = [0]*(N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + arr[i]

    # update the dp cache
    dp = [0]*(N+1)
    dp[M] = prefix[M]
    for i in range(M+1, N+1):
        dp[i] = max(dp[i-1] + arr[i], prefix[i] - prefix[i-M])

    print(max(dp))


if __name__ == "__main__":
    solution()
