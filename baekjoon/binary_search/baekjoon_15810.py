import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 시간 배열
        - 탐색 기준: 현재 시간값으로 만들 수 있는 풍선 개수
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    # do bisect with time
    # lower, upper bound 범위 잡는게 진짜 중요해!
    answer = 0
    l, r = 1, arr[-1]*M
    while l <= r:
        mid = (l+r) // 2  # value of current time
        cnt = 0
        for player in arr:
            cnt += mid // player
            if cnt >= M:
                break

        if cnt >= M:
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
