import sys

def dfs(x, y):
    if visited[x][y] != 0:
        return visited[x][y]
    visited[x][y] = 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[x][y] < graph[nx][ny]:
                # visited[x][y]: 계속 최대값으로 업데이트
                visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1) # 현재 최대값과 현재 방향의 경로값을 비교
    return visited[x][y]


n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)] # 여기에는 경로를 저장하는게 아니라 시작점에 대한 최대 블록 수를 저장

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

max_num = 0
for i in range(n):
    for j in range(n):
        max_num = max(max_num, dfs(i, j))
print(max_num)
