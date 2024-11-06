import sys


def solution():
    """ NlogN, 석순: 바닥 to 천장, 종유석: 천장 to 바닥
    idea: binary search, two-pointer
        - 탐색 대상/범위: 장애물 개수, 0 to max
        - 탐색 기준:

    """
    input = sys.stdin.readline
    N, H = map(int, input().split())  # 장애물 숫자, 길이
    height = [int(input()) for _ in range(N)]

    l, r = 0, H
    while l <= r:
        mid = (l+r) // 2


if __name__ == "__main__":
    solution()
