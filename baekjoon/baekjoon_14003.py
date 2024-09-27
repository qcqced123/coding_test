import sys
import bisect


def solution():
    """ 가장 긴 증가 부분 수열: 수열 길이 기준, NlogN 이하

    idea: binary search with recording index of array

    Good Input Example:
        10
        100 50 70 90 75 87 105 78 110 60

    """
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))

    count = 0
    cache, cache_list = [arr[0]], [(arr[0], count)]
    for i in range(1, N):
        if cache[-1] < arr[i]:
            count += 1
            cache.append(arr[i])
            cache_list.append((arr[i], count))

        else:
            cnt = bisect.bisect_left(cache, arr[i])
            cache[cnt] = arr[i]
            cache_list.append((arr[i], cnt))

    result = []
    for i in range(len(cache_list)-1, -1, -1):
        vx, vc = cache_list[i]
        if vc == count:
            result.append(vx)
            count -= 1
    result.reverse()

    print(len(cache))
    print(*result)


if __name__ == "__main__":
    solution()
