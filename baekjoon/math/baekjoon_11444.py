import sys
from typing import List


def solution():
    sys.setrecursionlimit(10**6)
    n = int(sys.stdin.readline())

    def fibo(curr: int):
        if curr <= 1:
            return 1
        left = fibo(curr-1)
        right = fibo(curr-2)
        return


if __name__ == "__main__":
    solution()
