import sys
from bisect import bisect_left


def solution():
    """
    idea: binary search
        - 가장 긴 증가하는 부분 수열 길이
        - 4만**2 => 16억이라서 N**2 불가
            - binary search 사용한 알고리즘으로 풀이
    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    cache = []  # for saving the longest sub sequence

    # do the bisect
    frame = -1
    for i in range(N):
        cnt = arr[i]
        if cnt > frame:
            cache.append(cnt)
            frame = cnt
        else:
            idx = bisect_left(cache, cnt)
            cache[idx] = cnt
            frame = cache[-1]

    print(len(cache))


if __name__ == "__main__":
    solution()
