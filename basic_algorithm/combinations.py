import sys
from typing import List


def combinations(n: int, k: int) -> List[List]:
    """ combination algorithm by using back tracking """
    result, curr = [], []

    def backtracking(src: int, count: int) -> None:
        if not count:
            result.append(curr[:])
            return

        for i in range(src, n+1):
            curr.append(i)
            backtracking(i+1, count-1)
            curr.pop()

    backtracking(1, k)
    return result


sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
nums_list = combinations(N, M)
for nums in nums_list:
    print(*nums)

