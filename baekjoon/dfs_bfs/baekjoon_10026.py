import sys
"""
[풀이 시간]
1) 05:45 ~ 06:15

[요약]
1)  N×N인 그리드, R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림
    - 그림은 몇 개의 구역, 같은 구역은 같은 색으로 색칠
    - 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역
    - 색상의 차이를 거의 느끼지 못하는 경우도 같은 색상 (빨강색 == 초록색)
    => 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수 출력하기
[전략]
1) 2차원 테이블 자료구조 & 구역 나누기
    - 전형적 DFS 문제
    - visited 필요
"""


def dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and table[ny][nx] == table[y][x]:
            visited[ny][nx] = True
            dfs(ny, nx)


def t_dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not t_visited[ny][nx] and table[ny][nx] == table[y][x]:
            t_visited[ny][nx] = True
            t_dfs(ny, nx)
        elif 0 <= ny < N and 0 <= nx < N and not t_visited[ny][nx] and table[ny][nx] != table[y][x]:
            if (table[y][x] == "R" or table[y][x] == "G") and (table[ny][nx] == "R" or table[ny][nx] == "G"):
                t_visited[ny][nx] = True
                t_dfs(ny, nx)


sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
table, visited = [[i for i in list(sys.stdin.readline().rstrip())] for _ in range(N)], [[False]*N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
tmp1, tmp2, t_visited = 0, 0, [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            tmp1 += 1

for i in range(N):
    for j in range(N):
        if not t_visited[i][j]:
            t_dfs(i, j)
            tmp2 += 1
print(tmp1, end=' ')
print(tmp2)
