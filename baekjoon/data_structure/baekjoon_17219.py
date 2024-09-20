import sys
from typing import List


def solution():
    N, M = map(int, sys.stdin.readline().split())
    site_book = {}
    for i in range(N):
        k, v = sys.stdin.readline().rstrip().split(" ")
        site_book[k] = v

    for j in range(M):
        print(site_book[sys.stdin.readline().rstrip()])


if __name__ == "__main__":
    solution()
