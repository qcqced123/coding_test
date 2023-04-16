from collections import deque
import sys
"""

[Situation]
1) 바이러스 확산을 막기 위해 가벽을 세울 예정
2) 연구소 크기 => N * M
3) 간선 가중치 => 1
    => BFS 사용하자!
4) 바이러스는 상하좌우로 이동 가능, 인접한 빈 칸으로 모두 이동 가능함
5) 새로 세울 수 있는 가벽의 수는 3개, 3개 다 세워야 함 적거나 많게 세울 수 없음

[Representation]
0 => 빈칸
1 => 벽
2 => 바이러스가 들어있는 공간
안전 영역 => 바이러스가 더 이상 퍼질 수 없는 공간

[Goal]
연구소 지도가 주어졌을 때, 가벽 3개를 세워서 얻을 수 있는 안전 영역 크기의 최대값

[Strategy]
즉, 현재 0으로 표시된 구역에 가벽을 세울 수 있으며, 0의 개수가 가장 많도록 가벽을 세우면 되겠네 
간선 가중치가 1이라는 것에서 BFS를 활용해야 함을 알 수 있음
이미 값으로 테이블을 초기화 시키기 때문에, 기타 다른 자료형을 선언할 필요가 없고 그대로 사용하면 된다.

"""

# Step 1. Input Init
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for row in range(N)]

print(graph)

dx = [-1, 1, 0, 0] # 좌우
dy = [0, 0, -1, 1] # 상하

# Step 2. BFS
queue = deque()
queue.append((4,1))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 직사각형 밖으로 나가는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 진행 방향에 가벽이 존재하는 경우
        if graph[nx][ny] == 1:
            continue

        # 진행 방항에 가벽이 없는 경우, 진행 방향에 이미 바이러스가 존재하는 경우
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2

        queue.append((nx, ny))


print(graph)
