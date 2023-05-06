import sys
"""
[풀이 시간]
1) 20:10 ~ 20:40

[요약]
1) 단지를 찾아서 번호를 붙여주기
    - 단지란, 상하좌우로 연결된 집단을 의미함
    - 각 단지에 속하는 집의 수를 오름차순으로 정렬해 출력
[전략]
1) 그룹핑도 해줘야 하고, 그룹 내부에 원소 개수도 구해야하는 문제
2) DFS/BFS, 접근이 필요한데, 네 방향으로 접근하면서 개수를 세는 것은 BFS가 적합
    - Table 자료구조용 BFS 구현하기
"""


def bfs(y, x):
    """ y: row, x: column """
    global count
    visited[y][x] = True
    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and table[ny][nx] == '1':
            count += 1
            visited[ny][nx] = True
            bfs(ny, nx)


N = int(sys.stdin.readline())
table, visited = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)], [[False]*N for _ in range(N)]
result = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(N):
    for j in range(N):
        if table[i][j] == '1' and not visited[i][j]:
            count = 1
            bfs(i, j)
            result.append(count)
result.sort()
print(len(result))
for row in result:
    print(row)
