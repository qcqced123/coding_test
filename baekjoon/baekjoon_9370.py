import sys
import heapq
from collections import defaultdict


def solution():
    """
    idea: dijkstra
        - 일반 다익스트라 수행 + 경로 저장

    reference:
        - https://www.acmicpc.net/board/view/119032
    """
    # dijkstra func
    def dijkstra(src: int) -> None:
        h = []
        cost[src] = 0
        path[src] += str(src)
        heapq.heappush(h, (0, src))
        while h:
            vc, vx = heapq.heappop(h)
            vp = path[vx]
            if vc > cost[vx]:
                continue
            if vc == INF:
                continue

            for nc, nx in graph[vx]:
                new_cost = nc+vc
                if new_cost <= cost[nx]:
                    cost[nx] = new_cost
                    path[nx] = vp+str(nx)
                    heapq.heappush(h, (new_cost, nx))

    # get input data
    INF = int(10**9)
    input = sys.stdin.readline
    for _ in range(int(input())):
        graph = defaultdict(list)
        n, m, t = map(int, input().split())  # node, edge, candidates of end point
        s, g, h = map(int, input().split())  # starting point, middle point of total path

        # init graph, cost array
        for _ in range(m):
            a, b, d = map(int, input().split())  # src, end, cost
            graph[a].append((d, b)), graph[b].append((d, a))

        # init candidate array
        candidates = [int(input()) for _ in range(t)]
        candidates.sort()

        # do find the shortest path by using dijkstra
        cost = [INF]*(n+1)
        path = [""]*(n+1)
        dijkstra(s)

        # find the given hint edge in shortest path
        answer = []
        hint1, hint2 = f"{g}{h}", f"{h}{g}"
        for candidate in candidates:
            if (hint1 in path[candidate]) or (hint2 in path[candidate]):
                answer.append(candidate)

        answer.sort()
        print(*answer)

if __name__ == "__main__":
    solution()
