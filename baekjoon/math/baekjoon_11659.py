import sys


def solution():
    """
    problem link:
        https://www.acmicpc.net/problem/11659

    summary:
        1) 1차원 배열의 누적합

    solution:
        1) 1차원 누적합 배열 생성
        2) 점화식 생성
          - dp[j] - dp[i-1]
    """
    N, M = map(int, sys.stdin.readline().split())
    nums, dp = [0] + list(map(int, sys.stdin.readline().split())), [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + nums[i]

    for _ in range(M):
        src, end = map(int, sys.stdin.readline().split())
        print(dp[end] - dp[src-1])


if __name__ == "__main__":
    solution()
