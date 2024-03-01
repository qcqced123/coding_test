import sys
import bisect


def solution():
    N = int(sys.stdin.readline())
    nums, dp = list(map(int, sys.stdin.readline().split())), [1]*N
    for i in range(N):
        curr = nums[:i+1]
        if i+1 == bisect.bisect_right(curr, nums[i]):
            dp[i] = max(dp[:i+1]) + 1
    print(max(dp))

if __name__ == "__main__":
    solution()
