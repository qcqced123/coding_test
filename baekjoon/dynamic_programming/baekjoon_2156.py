import sys


def solution():
    """ 100,000,000, N^2
    conditions:
        1) 선택하면 다 먹고 원위치
        2) 연속 3잔 불가
        => 최대한 양 먹기
    idea: dynamic programming
        1) max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

    => 제발 잘 좀 풀자
    => 구현을 그지 같이 하냐...,,,........ㅠ
    """
    N = int(input())
    glass = [int(input()) for _ in range(N)]

    dp = [0]*N
    dp[0] = glass[0]
    if N > 1:
        dp[1] = glass[0] + glass[1]
    if N > 2:
        dp[2] = max(glass[0] + glass[2], glass[1] + glass[2], dp[1])

    for i in range(3, N):
        dp[i] = max(
            dp[i-3] + glass[i-1] + glass[i],
            dp[i-2] + glass[i],
            dp[i-1]
        )
    print(max(dp))


if __name__ == "__main__":
    solution()
