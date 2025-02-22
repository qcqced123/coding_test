import sys
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix
        -
    """
    # get input data
    metro = defaultdict(list)
    N, M = map(int, input().split())  # city, day
    arr = list(map(int, input().split()))

    # init metro dictionary
    for i in range(1, N+1):
        cnt = list(map(int, input().split()))
        metro[(i,i+1)].extend(cnt), metro[(i+1, i)].extend(cnt)

    #

if __name__ == "__main__":
    solution()
