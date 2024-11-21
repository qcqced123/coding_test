import sys
from bisect import bisect_left


def solution():
    """ NlogN
    idea: binary search
        - 통상적으로 풀면 for-loop(10만) * if x in (10만)
        - 그래서 binary search
        - arr sorting (NlogN)
        - bisect_left(arr, i)
        - arr[bisect_left] == query i ??
    """
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))

    M = int(input())
    queries = list(map(int, input().split()))

    # do bisect
    arr.sort()
    for q in queries:
        i = bisect_left(arr, q)
        if i < N and arr[i] == q:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()
