import sys
"""
[조건]
1) 상하좌우 이동
    - Go K: 현재 이동 방향으로 K만큼 이동
    - Turn dir: 이동 방향 변경, 90도 변경
    => 시작 to 목적까지 최소 명령 횟수 구하기
    => 이동은 상하좌우로만
    => BackTracking 스럽게 풀자 (시간 많고, 메모리 적기 때문)
[풀이]
DFS
1) 이동 가능한 블럭 확인하기
    - 현재 주어진 방향으로 이동 가능한 최대 step size 찾기
        - step == 1 가능하다면, 나머지 사이즈 확인 후, 최대값 도출
            - 명령값 하나 증가, 현재 방향 & 최대 스탭, 스택 호출
        - step == 1 불가능, 다른 방향 탐색
            - 명령값 하나 증가, 다음 방향, 스택 호출
    - 목적지 결과 업데이트
"""


def dfs(sy: int, sx: int, sd: int, visit, result: int) -> None:
    global final
    # 3) 목적지 도착한 경우
    if sy == er-1 and sx == ec-1:
        if sd == ed-1:
            final = min(result, final)
            return
        else:
            for j in [1, -1]:
                tmp = sd - j
                if tmp == -1:
                    tmp = 3
                elif tmp == 4:
                    tmp = 0
                dfs(sy, sx, tmp, visit, result + 1)

    visit[sy][sx] = True
    curr = False
    # 1) 이동 방향, 스탭 사이즈 확정
    for i in range(1, 4):
        ny = dy[sd]*i + sy
        nx = dx[sd]*i + sx
        if -1 < ny < M and -1 < nx < N and graph[ny][nx] == 0 and not visit[ny][nx]:
            tmp_y, tmp_x = ny, nx
            curr = True
            continue
        else:
            break
    # 방향 변경: 왼쪽 오른쪽 중에서 이동 가능한 쪽으로 탐색
    if not curr:
        for j in [1, -1]:
            tmp = sd - j
            if tmp == -1:
                tmp = 3
            elif tmp == 4:
                tmp = 0
            dfs(sy, sx, tmp, visit, result + 1)

    # 2) 방향 및 스탭 사이즈 확정, 탐색 시작
    else:
        dfs(tmp_y, tmp_x, sd, visit, result+1)


sys.setrecursionlimit(10**6)
M, N = map(int, sys.stdin.readline().split())
graph, visited = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)], [[False] * N for _ in range(M)]
nodes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(2)]  # row, col, direction

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

final = float('inf')
r, c, d = nodes[0]  # 시작점
er, ec, ed = nodes[1]  # 목적지

dfs(r-1, c-1, d-1, visited, 0)
print(final)

