import sys
from typing import List
"""
[풀이]
1) 지름: 가능한 경우의 수 중에서 가장 긴 경로
    - (u, v, cost, -1)
    - DP or DFS
=> 트리도 결국 그래프,
"""


def solution():
    # 1) make input
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]

    for _ in range(N):
        u, *conn = list(map(int, sys.stdin.readline().split()))[:-1]
        for i in range(0, len(conn), 2):
            v, cost = conn[i], conn[i+1]
            tree[u].append([cost, v])  # [cost, v]
    # 2)

if __name__ == "__main__":
    solution()
