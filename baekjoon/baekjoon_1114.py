import sys


def solution():
    """
    idea: parametric search
        - 최적화 대상/범위: 가장 긴 조각의 최소값, 0 to L
        - 최적화 기준: 탐색 알고리즘 짜는 것부터 험난함...


    """
    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    L, K, C = map(int, input().split())
    arr = list(map(int, input().split())) + [L]

    # do parametric search
    answer = INF
    l, r = 0, L
    while l <= r:
        mid = (l+r) // 2
        prev, cutting = 0, 0


if __name__ == "__main__":
    solution()
