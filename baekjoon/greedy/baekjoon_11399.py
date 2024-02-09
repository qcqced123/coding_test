import sys


def solution():
    n = int(sys.stdin.readline())
    table = sorted(tuple(map(int, sys.stdin.readline().split())))
    dp = [table[0]] + [0]*(n-1)
    for i in range(1, n):
        dp[i] = dp[i-1] + table[i]
    print(sum(dp))


if __name__ == "__main__":
    solution()

