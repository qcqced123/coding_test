from collections import deque
import sys

"""

[변수 설명]
1) N => Table Size
2) K => Virus 종류
3) S => Time
4) X => Table Row idx
5) Y => Table Col idx

[구조]
1) 입력값 받기
2) 테이블 한 번 BFS 시켜서 , 오름차순으로 큐에 삽입하기 => 실제 바이러스 개수는 정확히 알 수 없으며(K개 이하라는 것만 알 수 있음)
3) 시점마다 바이러스 퍼뜨리기 

*** 문제에 제시된 테이블 인덱스 - 1 = 코드에 정의된 테이블 인덱스
"""

# Input & 오름차순으로 바이러스 종류, 좌표 정보 큐에 넣기
N, K = map(int, sys.stdin.readline().split())
graph, virus_list = [], []

# 오름차순으로 특정 정보만 큐에 넣기
for row in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for col in range(N):
        if graph[row][col] != 0:
            virus_list.append([graph[row][col], 0, row, col])

virus_list.sort()
queue = deque(virus_list)

S, X, Y = map(int, sys.stdin.readline().split())

# BFS Direction
dx = [-1, 0, 1, 0] # 시작 위치에 바이러스가 존재하는 경우 처리하기 위해 맨 앞에 (0,0) 추가
dy = [0, -1, 0, 1]

while queue:
    virus, s, x, y = queue.popleft()
    # 지정된 시간에 도달한 경우
    if s == S:
        break

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny)) # 시점으로 분할해서 bfs 작동시키는 방법!


print(graph[X-1][Y-1])




