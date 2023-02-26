import sys
"""
[풀이 시간]
1) 20:10 ~ 21:10

[문제 정리]
1) N x N 사이즈 테이블, 상하좌우로 이동 가능
2) 이동 조건: 현재 위치 대나무 < 옮길 위치 대나무
3) 판다의 최대 이동 가능 블록 수: 시작 위치, 경로 지정

[전략]
1) DFS + Greedy, algorithm 매순간 선택할 때 지역 최대 해가 되도록 조작 필요
- 시작 위치를 굳이 전체 그래프 중 최소값을 선택할 필요가 없다.
- 시간적 여유가 많기 때문에 순차적으로 접근해서 DFS를 시켜도 충분히 시간 제한 안에 풀 수 있음. 
2) 시간 압박이 크게 없는 문제, O(n^2)도 가능
"""
# dfs function
def dfs(x, y, count):
    visited[x][y], num_list, idx_list = True, [], []
    count += 1
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if -1 < nx < n and -1 < ny < n and visited[nx][ny] == -1:
            if graph[nx][ny] > graph[x][y]:
                visited[nx][ny] = True
                num_list.append(graph[nx][ny])
                idx_list.append([nx, ny])
    print(num_list)
    if len(num_list) == 0:
        print(count)
        return False
    else:
        nx, ny = idx_list[num_list.index(min(num_list))]
        print(nx, ny)
        dfs(nx, ny, count)
    return count

# input
n = int(sys.stdin.readline())
visited = [[-1] * n for _ in range(n)]
graph, max_result = [list(map(int, sys.stdin.readline().split())) for _ in range(n)], 0

# direction
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        count = 0
        result = dfs(i, j, count)
        print(result)
        if max_result < result:
            max_result = result
print(max_result)
