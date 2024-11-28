import sys
import heapq
from collections import defaultdict


def solution():
    """
    idea: dfs with dynamic programming, adj graph
        - 그냥 단순한 dfs 아닌가...?
        - 테스트 케이스 2번째 같은 경우 때문에 dp cache 필요

    feedback:
        - 시간 초과 나니까 다익스트라로 풀어야
    """
    # dfs func
    INF = sys.maxsize
    sys.setrecursionlimit(10**6)
    def dfs(x: int) -> None:
        vt = cache[x]
        for nt, nx in graph[x]:
            if cache[nx] == -1 or vt + nt < cache[nx]:
                cache[nx] = vt + nt
                dfs(nx)

    # init data structure
    input = sys.stdin.readline
    for _ in range(int(input())):
        n, d, c = map(int, input().split())

        # make the adj graph
        graph = defaultdict(list)
        cache = [-1]*(n+1)  # visited array and dp cache
        for _ in range(d):
            child, parent, time = map(int, input().split())
            graph[parent].append((time, child))

        # do dfs
        cache[c] = 0
        dfs(c)

        # answering the question
        nums = 0
        for i in cache:
            if i > -1:
                nums += 1

        print(nums, max(cache))


def solution2():
    """
    idea: dijkstra
        - dfs dynamic programming은 시간 초과 발생

    feedback:
        - 처음엔 인접 그래프라서 O(N+V)가 되니까, 최악의 경우의 11만 수준이라고 판단해 dfs + dp가 괜찮을거라 생각했다
    """
    # shortest path func
    def dijkstra(x: int):
        h = []
        cost[x] = 0
        heapq.heappush(h, (0, x))
        while h:
            vt, vx = heapq.heappop(h)
            if vt > cost[vx]:
                continue

            for nt, nx in graph[vx]:
                new_cost = vt + nt
                if new_cost < cost[nx]:
                    cost[nx] = new_cost
                    heapq.heappush(h, (new_cost, nx))

    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    for _ in range(int(input())):
        n, d, c = map(int, input().split())

        # make the adj graph
        graph = defaultdict(list)
        cost = [INF] * (n+1)  # cost array of dijkstra
        for _ in range(d):
            child, parent, time = map(int, input().split())
            graph[parent].append((time, child))

        # do dijkstra
        dijkstra(c)

        # answering the question
        nums = 0
        last_node = 0
        for i in cost:
            if i < INF:
                nums += 1
                last_node = max(last_node, i)
        print(nums, last_node)


if __name__ == "__main__":
    solution2()
