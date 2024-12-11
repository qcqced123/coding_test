import sys
from collections import deque, defaultdict


def solution():
    """
    idea: topological sort with dynamic programming
        -
    """
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    dp = [0]*(N+1)
    degree = [0]*(N+1)
    graph = defaultdict(list)
    for _ in range(K):
        src, end, weight = map(int, input().split())
        if src < end:
            degree[end] += 1
            graph[src].append((weight, end))

    # do sort
    q = deque([(1, 1)])
    while q:
        vx, vc = q.popleft()
        vw = dp[vx]
        for nw, nx in graph[vx]:
            nc = vc+1
            degree[nx] -= 1
            if nc <= M:
                dp[nx] = max(dp[nx], vw+nw)
                if not degree[nx]:
                    q.append((nx, nc))
    print(dp)
    print(dp[-1])


def solution2():
    """ idea: bfs with dynamic programming
    """
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    dp = [0]*(N+1)
    graph = defaultdict(list)
    for _ in range(K):
        src, end, weight = map(int, input().split())
        if src < end:
            graph[src].append((weight, end))

    # do sort
    # 메모리가 터짐
    q = deque([(1, 1)])
    while q:
        vx, vc = q.popleft()
        vw = dp[vx]
        for nw, nx in graph[vx]:
            nc = vc+1
            if nc <= M:
                if vw+nw > dp[nx]:
                    dp[nx] = vw+nw
                q.append((nx, nc))
    print(dp[-1])


def solution3():
    """
    idea: dynamic programming
        - structure: 2D Table
            => 안되면 3D로
    """
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    # init data structure
    dp = [[0]*(M+1) for _ in range(N+1)]
    graph = defaultdict(list)
    for _ in range(K):
        src, end, weight = map(int, input().split())
        if src < end:
            graph[src].append((weight, end))

    # init dp cache
    for nw, nx in graph[1]:
        dp[nx][2] = max(dp[nx][2], nw)

    # update dp cache
    for i in range(2, N+1):
        for nw, nx in graph[i]:
            for k in range(1, M):
                if dp[i][k]:
                    dp[nx][k+1] = max(dp[nx][k+1], dp[i][k]+nw)

    print(max(dp[-1]))


if __name__ == "__main__":
    solution3()
