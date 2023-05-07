import sys
from collections import deque
"""
[풀이 시간]
1) 13:30 ~ 14:00

[요약]
1) 토마토 보관: 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관
    - 인접: 상, 하, 좌, 우
    - 바이러스 문제랑 똑같음, 토마토가 모두 익는데 몇일 걸릴까
[전략]
1) 대부분 이런 문제는 BFS로 해결
    - Table 자료구조 만들어서 BFS 구현
    - BFS 탐색이 총 몇 번 발생 == 모든 토마토가 익는데 필요한 최소 일수
    - visited 따로 구현 필요
    - 일수 계산하는 부분이 좀 많이 까다롭네
=> 일수 계산하는 방법을 모르겠으니 답지를 보자
"""


def bfs(y, x):
    global day
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        v = queue.popleft()
        day += 1
        for idx in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and table[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = True
                table[ny][nx] = 1


M, N = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited, day = [[False] * M for _ in range(N)], 0

dy = [-1, 1, 0, 0]  # M
dx = [0, 0, -1, 1]  # N

for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            bfs(i, j)
            break
print(day)



