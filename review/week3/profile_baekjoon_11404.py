import sys
from typing import List

try:
    profile
except NameError:
    profile = lambda x: x


@profile
def floyd():
    # 1) init values
    N = int(sys.stdin.readline())  # num of nodes
    M = int(sys.stdin.readline())  # num of edges
    graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    for i in range(0, N+1):
        graph[i][i] = 0

    for _ in range(M):
        src, end, cost = map(int, sys.stdin.readline().split())
        if graph[src][end] > cost:
            graph[src][end] = cost

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, N+1):
        for j in range(1, N+1):
            print(graph[i][j] if graph[i][j] != float('inf') else 0, end=' ')
        print()


if __name__ == "__main__":
    floyd()