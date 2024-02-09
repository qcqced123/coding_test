import sys
from typing import List


def permutations(nums):
    result = []
    current_permutation = []

    def backtrack(remaining):
        if not remaining:
            result.append(current_permutation[:])
            return

        for i in range(len(remaining)):
            current_permutation.append(remaining[i])
            next_remaining = remaining[:i] + remaining[i+1:]
            backtrack(next_remaining)
            current_permutation.pop()

    backtrack(nums)
    return result


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
combination_list = combinations(N, M)

permutation_list = []
for combs in combination_list:
    permutation_list.extend(permutations(combs))

permutation_list.sort()
for nums in permutation_list:
    print(*nums)


