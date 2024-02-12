import sys
from collections import defaultdict
from typing import List


def bellman(x: int, distance: List[int], graph: defaultdict[int, List]):
    distance[x] = 0
    nums = len(distance) - 1
    for k in range(nums):
        for i in range(1, nums+1):
            for nodes in graph[i]:
                curr_cost, curr_node = nodes
                new_cost = curr_cost + distance[i]
                if new_cost < distance[curr_node]:
                    distance[curr_node] = new_cost
                    if k == nums - 1:
                        return True
    return False


def solution():
    t = int(sys.stdin.readline())

    for _ in range(t):  # for test case
        n, m, w = map(int, sys.stdin.readline().split())  # nodes, edges, hole
        grid = defaultdict(list)
        for _ in range(m):
            src, end, time = map(int, sys.stdin.readline().split())
            grid[src].append((time, end)), grid[end].append((time, src))

        for _ in range(w):
            w_src, w_end, w_time = map(int, sys.stdin.readline().split())  # w_time will be negative int
            grid[w_src].append((-w_time, w_end))

        cost = [1e-9] * (n + 1)
        flag = bellman(1, cost, grid)
        print("YES" if flag else "NO")


if __name__ == "__main__":
    solution()
