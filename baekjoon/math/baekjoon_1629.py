import sys
from typing import List


def solution():
    sys.setrecursionlimit(10**6)
    A, B, C = map(int, sys.stdin.readline().split())

    def multiply(a: int, b: int):
        return a*b % C

    def power(x: int, curr: int):
        if curr == 1:
            return x
        tmp = power(x, curr // 2)
        if not curr % 2:
            return multiply(tmp, tmp)
        else:
            return multiply(multiply(tmp, tmp), x)
    print(power(A, B) % C)


if __name__ == "__main__":
    solution()
