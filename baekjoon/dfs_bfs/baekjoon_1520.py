import sys
from typing import List


def solution1():
    """
    problem link:
        https://www.acmicpc.net/problem/1520

    solution:
        1) DFS/BFS + DP
    """
    M, N = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    dp = [[-1]*N for _ in range(M)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    sys.setrecursionlimit(10**6)
    def dfs(y: int, x: int):
        if y == M-1 and x == N-1:
            return 1

        if dp[y][x] != -1:
            return dp[y][x]

        answers = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if -1 < ny < M and -1 < nx < N and grid[y][x] > grid[ny][nx]:
                answers += dfs(ny, nx)

        dp[y][x] = answers
        return dp[y][x]
    print(dfs(0,0))


if __name__ == "__main__":
    solution1()
