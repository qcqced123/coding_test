import sys


def solution():
    """ 실력 차이
    idea: dynamic programming
        - N**2
    """
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0]*N

    # update the dp cache
    for i in range(1, N):
        for j in range(i):
            cnt = arr[j:i+1]  # optimization point
            dp[i] = max(dp[i], dp[j-1]+(max(cnt) - min(cnt)))

    print(dp[-1])


if __name__ == "__main__":
    solution()
