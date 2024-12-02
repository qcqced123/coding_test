import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 예산의 최대값 배열, N to max(arr)
    """
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    limit = int(input())

    # do bisect
    answer = 0
    l, r = 0, arr[-1]
    while l <= r:
        mid = (l+r) // 2
        cnt = 0
        for money in arr:
            cnt += money if money <= mid else mid
            if cnt > limit:
                break

        if cnt > limit:
            r = mid - 1

        else:
            l = mid + 1
            answer = mid

    print(answer)


if __name__ == "__main__":
    solution()
