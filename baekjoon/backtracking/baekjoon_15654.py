import sys
from typing import List


def solution():
    sys.setrecursionlimit(10**6)
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    def permutations(arr: List) -> List:
        result, curr = [], []

        def backtracking(num: List) -> None:
            if not num:
                result.append(curr[:])
                return

            for i in range(len(num)):
                curr.append(num[i])
                next_permute = num[:i] + num[i+1:]
                backtracking(next_permute)
                curr.pop()

        backtracking(arr)
        return result

    def combinations(n: int, k: int) -> List[List]:
        result, curr = [], []

        def backtracking(src: int, count: int) -> None:
            if not count:
                result.append(curr[:])
                return

            for i in range(src, n):
                curr.append(nums[i])
                backtracking(i+1, count-1)
                curr.pop()

        backtracking(0, k)
        return result

    combs = combinations(N, M)

    total = []
    for i in combs:
        total.extend(permutations(i))

    total.sort()
    for i in range(len(total)):
        print(*total[i], end='\n')


if __name__ == "__main__":
    solution()
