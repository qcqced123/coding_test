import sys
from collections import defaultdict
from typing import List


def dfs(x: int, d: int, cost: int, total: List, graph: defaultdict[int, List], visited: list):
    visited.append(x)
    for node in graph[x]:
        nt, nx = node
        if nx == d and nx in visited:
            total.append(cost+nt)
            return

        if nx not in visited:
            dfs(nx, d, cost+nt, total, graph, visited)
            visited.pop()


def solution():
    sys.setrecursionlimit(10**6)
    t = int(sys.stdin.readline())
    n, m, w = map(int, sys.stdin.readline().split())  # nodes, edges, hole

    for _ in range(t):  # for test case
        grid = defaultdict(list)

        for _ in range(m):
            src, end, time = map(int, sys.stdin.readline().split())
            grid[src].append((time, end)), grid[end].append((time, src))

        for _ in range(w):
            w_src, w_end, w_time = map(int, sys.stdin.readline().split())  # w_time will be negative int
            grid[w_src].append((-w_time, w_end))

        for h in grid.keys():
            visit, flag, result = [], False, []
            dfs(h, h, 0, result, grid, visit)
            for i in result:
                if i < 0:
                    print("YES")
                    flag = True
                    break
            if flag:
                break

        if not flag:
            print("NO")


if __name__ == "__main__":
    solution()
