import sys
from collections import deque, defaultdict


def solution():
    """
    idea: topological sorting
        - cache[nx] = max(cache[nx], cache[vx] + 1)
    """
    # init the data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    cache = [1]*(N+1)  # for answering the question

    indegree = [0]*(N+1)
    graph = defaultdict(list)
    for _ in range(M):
        src, end = map(int, input().split())
        graph[src].append(end)
        indegree[end] += 1

    # do topological sorting with bfs
    q = deque([i for i in range(1, N+1) if not indegree[i]])
    while q:
        vx = q.popleft()
        for nx in graph[vx]:
            indegree[nx] -= 1
            cache[nx] = max(cache[nx], cache[vx] + 1)
            if not indegree[nx]:
                q.append(nx)

    print(*cache[1:])


if __name__ == "__main__":
    solution()
