import sys
from typing import List, Set


def solution():
    sys.setrecursionlimit(10**6)
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    def permutations(arr: List) -> Set:
        result, curr = set(), []

        def backtracking(remaining: List) -> None:
            if not remaining:
                result.add(tuple(curr[:]))
                return

            for i in range(len(remaining)):
                curr.append(remaining[i])
                next_permute = remaining[:i] + remaining[i+1:]
                backtracking(next_permute)
                curr.pop()

        backtracking(arr)
        return result

    def combinations(n: int, k: int) -> Set:
        result, curr = set(), []

        def backtracking(src: int, count: int) -> None:
            if not count:
                result.add(tuple(curr[:]))  # copy curr state to result
                return

            for i in range(src, n):
                curr.append(nums[i])
                backtracking(i+1, count-1)
                curr.pop()

        backtracking(0, k)
        return result

    total = []
    combs = combinations(N, M)
    for comb in combs:
        total.extend(permutations(comb))

    total = sorted(set(total))
    for i in total:
        print(*i, end='\n')


if __name__ == "__main__":
    solution()
