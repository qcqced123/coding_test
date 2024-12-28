import sys
import heapq
from collections import defaultdict


def solution():
    """
    idea: parametric search + dijkstra
        - 그래프 탐색 방식:
    """
    # shortest path func
    def dijkstra(x: int, limit: int):
        h = []
        cost[x] = 0
        heapq.heappush(h, (0, x))
        while h:
            vc, vx = heapq.heappop(h)
            vp = path[vx]
            if vc > cost[vx]:
                continue

            for nc, nx in graph[vx]:
                new_cost = vc + nc
                if new_cost < cost[nx]:
                    path[nx] = vp
                    if nc > limit: path[nx] += 1
                    cost[nx] = new_cost
                    heapq.heappush(h, (new_cost, nx))

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, P, K = map(int, input().split())

    # init graph structure
    l, r = INF, -INF
    graph = defaultdict(list)
    for _ in range(P):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))
        l = min(l, cost)
        r = max(r, cost)

    # do parametric search with dijkstra
    answer = 0
    while l <= r:
        mid = (l+r) // 2
        path = [0]*(N+1)
        cost = [INF]*(N+1)
        dijkstra(1, mid)
        print(mid, path)
        if cost[N] != INF and path[N] <= K:
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
