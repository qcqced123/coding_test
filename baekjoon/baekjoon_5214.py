import sys
from collections import deque, defaultdict


def solution():
    """ 무향 그래프, 최소 방문 경로, NlogN....
    idea: bfs
        - init graph
        - do bfs

    question/result:
        - N == max(100000), 메모리가 터짐....
    """
    # bfs func
    def bfs(x: int) -> int:
        q = deque([(x, 1)])
        visited = set()
        visited.add(x)
        while q:
            vx, vc = q.popleft()
            for nx in graph[vx]:
                if nx == N:
                    return vc+1

                if nx not in visited:
                    visited.add(nx)
                    q.append((nx, vc+1))

        return -1

    # get input data
    input = sys.stdin.readline
    N, K, M = map(int, input().split())
    graph = defaultdict(set)

    # init graph structure
    for _ in range(M):
        cnt = list(map(int, input().split()))
        for i in range(K):
            curr = cnt[:i] + cnt[i+1:]
            for j in curr:
                graph[cnt[i]].add(j)

    # do bfs
    print(bfs(1))


if __name__ == "__main__":
    solution()
