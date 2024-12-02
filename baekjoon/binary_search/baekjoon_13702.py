import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 최대 막걸리 용량 배열, 1 to max(arr)
        - 탐색 기준: 기준값을 이용해서 막걸리마다 나눠서, 최대 몇 명에게 줄 수 있는지 세어보기
    """
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    answer = 0
    l, r = 1, max(arr)
    while l <= r:
        cnt = 0
        mid = (l+r) // 2
        for water in arr:
            cnt += water // mid
            if cnt >= K:
                break

        if cnt >= K:
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


if __name__ == '__main__':
    solution()