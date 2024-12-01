import sys


def solution():
    """ 귀납적으로 결정
    idea: binary search
        - 탐색 대상/범위: 최대 랜선의 길이, 1 to max(arr)
    """
    input = sys.stdin.readline
    K, N = map(int, input().split())
    arr = [int(input()) for _ in range(K)]

    # do bisect
    answer = 0
    l, r = 1, max(arr)  # for avoiding zero-division error
    while l <= r:
        mid = (l+r) // 2
        cnt = 0
        for lan in arr:
            cnt += lan // mid
            if cnt > N:
                break

        if cnt >= N:
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
