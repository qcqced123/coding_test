import sys
from collections import defaultdict


def solution():
    """ No weight, direction of tree
    Answering the given question
        1) number of sub tree's nodes

    idea: dfs + dp
        1) update the cache array
        2) answering the question

    => 시간 초과가 어디서 날까...?
    => 쿼리 입력이 너무 많은데 sys 모듈 안쓰고, input()쓰다가 초과 났음
    reference:
        https://www.acmicpc.net/board/view/141985
    """
    def dfs(root: int, group: set) -> None:
        group.add(root)
        for nx in graph[root]:
            if nx not in group:
                dfs(nx, group)
                cache[root] += cache[nx]

    sys.setrecursionlimit(10**6)
    graph = defaultdict(list)
    N, R, Q = map(int, sys.stdin.readline().split())

    # initialize the graph with no direction
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v), graph[v].append(u)

    # initialize the cache array
    cache = [1]*(N+1)
    dfs(R, set())

    # answering the question
    for _ in range(Q):
        print(cache[int(sys.stdin.readline().rstrip())], end='\n')


if __name__ == "__main__":
    solution()
