import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 최대 파 길이, 1 to 10억
    """
    input = sys.stdin.readline
    S, C = map(int, input().split())
    arr = [int(input()) for _ in range(S)]

    # do bisect
    answer = 0
    l, r = 1, max(arr)
    while l <= r:
        mid = (l+r) // 2
        cnt = 0
        for i in arr:
            cnt += i // mid
            if cnt >= C:
                break

        if cnt >= C:
            answer = mid
            l = mid + 1
        else:
            r = mid - 1

    curr = 0
    result = 0
    for i in arr:
        divisor, remain = divmod(i, answer)
        if curr + divisor > C:
            remain += (C - curr+divisor)*answer
            result += remain
            curr = C
            continue

        curr += divisor
        result += remain

    print(result)


if __name__ == "__main__":
    solution()
