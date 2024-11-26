import sys
from collections import defaultdict

def solution():
    """
    idea: dynamic programming
        - 노드가 최대 100만개: backtrack 일 수가 없음
        - 제약 조건: 얼리 어답터 몇 명
        - 개 어려워....ㅜㅠㅜ
    feedback:
        - tree dynamic programming...?
            - 난이도가 어메이징 하네 진짜
            - 진짜 더럽게 어렵고 좋은 문제구나
    """
    # dfs func
    sys.setrecursionlimit(10**9)
    def dfs(x: int) -> None:
        visited[x] = 1
        for nx in graph[x]:
            if not visited[nx]:
                dfs(nx)
                cache[x][1] += min(cache[nx][0], cache[nx][1])
                cache[x][0] += cache[nx][1]

        cache[x][1] += 1

    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [[0, 0] for _ in range(N+1)]  # index 0: current node is not early-adapter, 1: current node is early-adpater
    visited = [0]*(N+1)

    # get the no-directional tree
    graph = defaultdict(list)
    for _ in range(N-1):
        parent, child = map(int, input().split())
        graph[parent].append(child)
        graph[child].append(parent)

    dfs(1)
    print(min(cache[1][0], cache[1][1]))


if __name__ == "__main__":
    solution()
