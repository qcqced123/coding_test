import sys
from collections import defaultdict, deque
from typing import List


def solution(n: int, m: int):
    grid = defaultdict(list)
    for _ in range(m):
        src, end = map(int, sys.stdin.readline().split())
        grid[src].append(end)

    def tree_depth(x: int, graph: defaultdict) -> int:
        q = deque()
        q.append(x)
        result = 0
        while q:
            for i in range(len(q)):  # binding
                vx = q.popleft()
                for nx in graph[vx]:
                    q.append(nx)
            result += 1
        return result
    print(tree_depth(1, grid))


if __name__ == "__main__":
    solution(4,5)
