import sys


def solution():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    dp = sorted(list(set(arr)))
    idx_dict = {dp[i]: i for i in range(len(dp))}

    result = [idx_dict[num] for num in arr]
    print(*result)


if __name__ == "__main__":
    solution()
