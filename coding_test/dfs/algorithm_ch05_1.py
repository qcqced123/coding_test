import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dfs(graph, x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리
        dfs(graph, x - 1, y) # 왼쪽
        dfs(graph, x + 1, y)  # 오른쪽
        dfs(graph, x, y - 1)  # 아래
        dfs(graph, x, y + 1)  # 위
        return True

    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(graph, i, j) == True:
            result += 1

print(result)


