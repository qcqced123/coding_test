import sys


N, M, R = map(int, sys.stdin.readline().split())  # nodes, search, edges
items = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(R):
    src, end, weight = map(int, sys.stdin.readline().split())
    graph[src][end] = weight
    graph[end][src] = weight

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for r in range(1, N+1):
    total = items[r]
    for c in range(1, N+1):
        if graph[r][c] <= M:
            total += items[c]
    result = max(result, total)
print(result)

