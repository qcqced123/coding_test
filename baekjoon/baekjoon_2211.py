import sys
import heapq
from collections import defaultdict


def solution():
    """
    idea: dijkstra with caching the path
        - caching the path with hash
            - vx: key
            - nx: value
    limit: N^2*logN
    """
    # dijkstra func
    def dijkstra():
        h = []
        heapq.heappush(h, (0, 1))  # cost, node
        while h:
            vc, vx = heapq.heappop(h)
            if vc > weights[vx]:
                continue

            for nc, nx in graph[vx]:
                new_cost = vc + nc
                if new_cost < weights[nx]:
                    if vx != 1 and (1, nx) in cache:
                        cache.remove((1, nx))

                    cache.add((vx,nx))
                    weights[nx] = new_cost
                    heapq.heappush(h, (new_cost, nx))
        return


    # get input data
    INF = sys.maxsize
    graph = defaultdict(list)
    input = sys.stdin.readline
    N, M = map(int, input().split())

    # init graph
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))

    # do dijkstra
    cache = set()
    weights = [INF]*(N+1)
    weights[1] = 0
    dijkstra()

    # answering the question
    print(len(cache))
    for i in cache:
        print(*i)


if __name__ == "__main__":
    solution()
