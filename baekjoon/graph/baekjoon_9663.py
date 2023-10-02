import sys
from typing import List, Tuple

"""
[풀이]
1) Back Tracking
    - grid, visited 따로 저장
"""


def dfs(x: int) -> None:
    global count, grid, N
    if x == N:
        count += 1
        return
    for col in range(N):
        grid[x] = col
        for element in range(x):
            if grid[x] == grid[element] and (abs(x-element) == abs(grid[x] - grid[element])):
                continue
            else:
                dfs(x + 1)  # dive into next row


def solution():
    dfs(0)
    print(count)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    N = int(sys.stdin.readline())
    grid = [] * N
    count = 0
    solution()
