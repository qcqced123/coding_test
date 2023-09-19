import sys
from typing import List
try:
    profile
except NameError:
    profile = lambda x: x


@profile
def main():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    dp_left, dp_right = [1] * N, [0] * N
    # 1) init dp left
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j] and dp_left[i] < dp_left[j] + 1:
                dp_left[i] = dp_left[j] + 1

    # 2) init dp right
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if nums[i] > nums[j] and dp_right[i] < dp_right[j] + 1:
                dp_right[i] = dp_right[j] + 1
    dp = [i+j for i, j in zip(dp_left, dp_right)]
    print(max(dp))


if __name__ == '__main__':
    main()