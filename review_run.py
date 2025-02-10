import sys
INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """
    # get input data
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    # init dp cache, pointer position
    dp = [0] * (N + 1)
    left, right, cnt = 0, 1, 0
    while right <= N:
        cnt += arr[right]
        dp[right] = dp[right - 1]
        while cnt >= M:
            dp[right] = max(dp[right], dp[left - 1] + cnt - M)
            cnt -= arr[left]
            left += 1

        right += 1

    print(dp[N])

if __name__ == '__main__':
    solution()