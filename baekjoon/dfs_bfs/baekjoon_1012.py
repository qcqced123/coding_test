import sys
from collections import deque
"""
[풀이 시간]
1) 17:20 ~ 17:50

[요약]
1) 농사 짓는데 필요한 최소 지렁이 숫자 구하기
    - 인접(상하좌우)한 곳이면 지렁이가 이동 가능함
[전략]
1) DFS/BFS 문제
    - 값 저장 테이블, 방문 정보 저장 테이블 두 개 구성
"""
T = int(sys.stdin.readline())  # Test Case
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
for _ in range(T):
    counter = 0
    M, N, K = map(int, sys.stdin.readline().split())
    graph, visited = [[0] * M for _ in range(N)], [[False] * M for _ in range(N)]
    for _ in range(K):
        """ Make Table """
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    # Table Loop
    for row in range(N):
        for col in range(M):
            if not visited[row][col] and graph[row][col] == 1:
                queue = deque([(row, col)])
                visited[row][col] = True
                while queue:
                    node_y, node_x = queue.popleft()
                    for i in range(4):
                        nx = dx[i] + node_x
                        ny = dy[i] + node_y
                        if 0 <= nx < M and 0 <= ny < N:
                            if not visited[ny][nx] and graph[ny][nx] == 1:
                                visited[ny][nx] = True
                                queue.append((ny, nx))
                counter += 1
    result.append(counter)

for i in range(T):
    print(result[i])

