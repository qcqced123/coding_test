import sys
from typing import List


def solution():
    N = int(sys.stdin.readline())
    array = [0] + list(map(int, sys.stdin.readline().split()))  # for matching number of index
    M = int(sys.stdin.readline())
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())


if __name__ == "__main__":
    solution()
