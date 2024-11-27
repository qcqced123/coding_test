import sys
from collections import defaultdict


def solution():
    """
    idea: dfs with adj graph, finding cycle
        - dfs by each node
        - if there are cycle, then append the current path to result
    """
    # backtrack func
    sys.setrecursionlimit(10**6)
    def dfs(x, cnt):
        for nx in graph[x]:
            if nx == i:
                result.extend(cnt)

            if nx not in visited:
                cnt.append(nx)
                visited.add(nx)

                dfs(nx, cnt)

                cnt.pop()
                visited.remove(nx)

    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    graph = defaultdict(list)

    for i in range(N):
        graph[i+1].append(arr[i])

    # find the cycle
    result = []
    visited = set()
    for i in range(1, N+1):
        if not i in visited:
            visited.add(i)
            dfs(i, [i])

    result.sort()
    print(len(result))
    for i in result:
        print(i)


if __name__ == "__main__":
    solution()
