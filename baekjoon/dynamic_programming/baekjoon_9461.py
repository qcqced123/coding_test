import sys


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n <= 3:
            print(1)
            continue
        elif n <= 5:
            print(2)
            continue

        dp = [0] * (n+1)
        dp[1:6] = [1, 1, 1, 2, 2]
        for i in range(6, n+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[n])


if __name__ == '__main__':
    solution()