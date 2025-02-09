import sys


def solution():
    """ <= NlogN
    idea: parametric search with sliding window
        - 최적화 대상/범위: 윈도우 사이즈, M to N
        - 최적화 기준:
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]



if __name__ == "__main__":
    solution()
