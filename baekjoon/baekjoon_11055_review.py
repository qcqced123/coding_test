import sys


def solution():
    """ 가장 큰 증가 하는 부분 수열, 합의 최대값, N^2logN

    idea: dynamic programming (연속된 부분 수열이 아니라서, two-pointer 사용할 필요 없음)
        1) 1D DP Array
    """
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = arr[:]  # 이게 문제구나

    dp[0] = arr[0]
    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+arr[i], dp[i])

    print(max(dp))


if __name__ == "__main__":
    solution()
