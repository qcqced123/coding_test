from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
src = (1,1)
end_point = (N, M)

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0] # 좌우
dy = [0, 0, -1, 1] # 상하

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 방향이 4개니까 4로 설정하는 것이 맞음
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(graph, 0, 0))

