import sys
import heapq
from collections import defaultdict


def solution3():
    """
    idea: parametric search + dijkstra
        - cost[i]: i번째 노드로 오는데 mid 값을 넘긴 간선의 개수
            - 전적으로, 파라미터 업데이트는 mid에 몰아주고, 그럼 cost를 K 넘어가는 간선 개수로 정의할 수 있음
            - 그럼 K 넘어가는 간선 개수가 작은게 무조건 유리함
            - 이렇게 짜면, 딱 깔끔하게 parametric search 처럼 되네

        - 최적화 대상/범위:
            대상: 경로상 최대 간선 값의 최소값
            범위: 0 to max(edge), 돈을 안내도 되는 경우가 있어서, lower bound 범위가 0이 되어야 한다
    """
    # dijkstra func
    def dijkstra(src: int, limit: int) -> int:
        h = []
        cost[src] = 0
        heapq.heappush(h, (0, src))
        while h:
            vc, vx = heapq.heappop(h)
            if vc > cost[vx]:
                continue

            for nw, nx in graph[vx]:
                nc = vc
                if nw > limit:
                    nc += 1
                if nc < cost[nx]:
                    cost[nx] = nc
                    heapq.heappush(h, (nc, nx))

        if cost[N] <= K: return 1
        else: return 0


    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, P, K = map(int, input().split())

    # init graph structure
    # 돈을 안내도 되는 경우가 있어서, lower bound 범위가 0이 되어야 한다
    l, r = 0, -INF
    graph = defaultdict(list)
    for _ in range(P):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))
        r = max(r, cost)

    # do parametric search with dijkstra
    answer = INF
    while l <= r:
        mid = (l+r) // 2
        cost = [INF]*(N+1)
        if dijkstra(1, mid):
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer) if answer != INF else print(-1)


if __name__ == "__main__":
    solution3()
