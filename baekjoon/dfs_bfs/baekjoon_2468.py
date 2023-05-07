import sys
"""
[풀이 시간]
1) 15:05 ~ 15:35

[요약]
1) 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사
    - 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
2) 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
    - 물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다
    - 다만, 한 칸짜리도 안전 영역이 될 수 있음
[전략]
1) Table DFS 사용
    - 주어진 높이 이하의 구역에 마스킹 적용
    - DFS 탐색, 호출 횟수 == 안전 구역 개수
    - 내가 구하라고 기준 높이를???
=> list.copy: deepcopy가 맞음
"""


def dfs(y, x):
    visited[y][x] = True
    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and tmp_table[ny][nx] != -1:
            visited[ny][nx] = True
            dfs(ny, nx)


sys.setrecursionlimit(10**9)  # recursive call 문제는 무조건 이거부터 세팅하고 풀자
N = int(sys.stdin.readline())
table, result = [list(map(int, sys.stdin.readline().split())) for _ in range(N)], 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(0, 100):
    tmp_table, tmp_result = table.copy(), 0  # list class deepcopy
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if tmp_table[row][col] <= i:
                tmp_table[row][col] = -1
    for row in range(N):
        for col in range(N):
            if not visited[row][col] and tmp_table[row][col] != -1:
                dfs(row, col)
                tmp_result += 1
    result = max(result, tmp_result)
print(result)
