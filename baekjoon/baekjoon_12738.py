import sys
import bisect


def solution():
    """ 가장 긴 증가 부분 수열: 수열 길이 기준, NlogN 이하
    idea: binary search
    """
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    cache = [arr[0]]
    for i in range(1, N):
        if cache[-1] < arr[i]:
            cache.append(arr[i])

        else:
            cnt = bisect.bisect_left(cache, arr[i])
            cache[cnt] = arr[i]

    print(len(cache))
    print(*cache)


if __name__ == "__main__":
    solution()
