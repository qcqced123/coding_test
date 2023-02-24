from collections import deque
import sys

# Step 1. Input Init
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for row in range(N)]
temp_graph = [[0] * M for idx in range(N)] # 바이러스 퍼지는 현황을 표시하는 임시 테이블
result = 0

print(graph)

dx = [-1, 0, 1, 0] # 좌우
dy = [0, 1, 0, -1] # 상하

# dfs로 구현 => 조건에 맞는 모든 블럭에 퍼지게 하는게 목적이라서, 진행 방향에서 가능한 깊게 보내는 것이 맞는 듯
def move_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 직사각형 밖으로 나가는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 진행 방항에 가벽이 없는 경우, 진행 방향에 이미 바이러스가 존재하는 경우
        # 표시는 temp graph에 해야지
        if temp_graph[nx][ny] == 0:
            temp_graph[nx][ny] = 2
            move_virus(nx, ny)

# Count number of "0" in temp_graph
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                score += 1
    return score

# count => 설치한 가벽 개수 (무조건 3개를 세워야 함)
# 가벽을 모두 다 세우고 바이러스를 퍼뜨리자

def dfs(count):
    global result

    # Step 2. 가벽 모두 세우고 바이러스를 퍼뜨리는 상황
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp_graph[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp_graph[i][j] == 2:
                    move_virus(i, j)
        result = max(result, get_score())
        return

    # Step 1. 빈 공간에 울타리 설치
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1 # 가벽 설치
                dfs(count)
                graph[i][j] = 0 # 이건 이해가 안가네
                count -= 1


dfs(0)
print(result)
