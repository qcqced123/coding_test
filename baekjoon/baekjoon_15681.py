import sys
from collections import defaultdict


def solution():
    """ No weight, direction of tree
    Answering the given question
        1) number of sub tree's nodes

    idea: dfs + dp
        1) update the cache array
        2) answering the question

    """
    def dfs(root: int, group: set) -> None:
        if len(graph[root]) == 1:
            return

        group.add(root)
        for nx in graph[root]:
            if nx not in group:
                dfs(nx, group)
                cache[root] += cache[nx]


    sys.setrecursionlimit(10**4)
    graph = defaultdict(list)
    N, R, Q = map(int, sys.stdin.readline().split())

    # initialize the graph with no direction
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v), graph[v].append(u)

    # initialize the cache array
    cache = [1]*(N+1)
    dfs(R, set())
    print(cache)
    # answering the question
    for _ in range(Q):
        print(cache[int(input())], end='\n')

if __name__ == "__main__":
    solution()
