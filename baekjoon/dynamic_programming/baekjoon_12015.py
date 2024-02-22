import sys


def solution():
    N = int(sys.stdin.readline())
    nums, dp = [0] + list(map(int, sys.stdin.readline().split())), [0]*(N+1)
    tmp = 0
    for i in range(1, len(nums)):
        if nums[i] > tmp:
            tmp = nums[i]
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    print(max())


if __name__ == "__main__":
    solution()
