import sys
import bisect


def solution():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    dp = [nums[0]]

    for num in nums:
        if dp[-1] < num:
            dp.append(num)
        else:
            idx = bisect.bisect_left(dp, num)
            dp[idx] = num
        print(dp)
    print(len(dp))


if __name__ == "__main__":
    solution()
