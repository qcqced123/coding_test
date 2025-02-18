import sys
from collections import deque, defaultdict

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """

    # bfs func
    def bfs(limit: int) -> int:
        result = INF
        visited = dict()
        visited[A] = 0
        q = deque([(A, 0)])
        while q:
            vx, vc = q.popleft()
            if vc > visited[vx]:
                continue

            for nw, nx in graph[vx]:
                nc = vc + nw
                if nw <= limit:
                    if nx == B:
                        result = min(result, nc)

                    elif nx not in visited or nc < visited[nx]:
                        visited[nx] = nc
                        q.append((nx, nc))

        return result

    # get input data
    graph = defaultdict(list)
    N, M, A, B, C = map(int, input().split())

    # init graph, pointer
    answer = INF
    l, r = INF, 0
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))
        l = min(l, cost)
        r = max(r, cost)

    # do bfs with parametric search
    while l <= r:
        mid = (l + r) // 2
        if bfs(mid) <= C:
            r = mid - 1
            answer = mid

        else:
            l = mid + 1

    print(answer if answer != INF else -1)


if __name__ == '__main__':
    solution()