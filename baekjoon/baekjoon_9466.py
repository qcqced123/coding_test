import sys
from collections import deque
from collections import defaultdict


def solution():
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, sys.stdin.readline().split()))

        # initialize the graph
        graph = defaultdict(int)
        for i in range(N):
            student, choice = i+1, arr[i]
            graph[student] = choice

        # initialize the cache
        cache = [0]*(N+1)
        visited = [0]*(N+1)

        # bfs with condition
        for i in range(1, N+1):
            if not visited[i]:
                q = deque([i])
                group = []
                while q:
                    vs = q.popleft()
                    group.append(vs)
                    ns = graph[vs]
                    if visited[ns]:
                        if ns in group:
                            cycle_start = group.index(ns)
                            for i in range(cycle_start, len(group)):
                                cache[group[i]] = 1
                        break

                    visited[ns] = 1
                    q.append(ns)

        result = cache.count(0) - 1
        print(result)


if __name__ == "__main__":
    solution()
