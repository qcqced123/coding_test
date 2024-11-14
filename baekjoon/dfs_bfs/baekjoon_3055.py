import sys
from collections import deque


def solution():
    """ 경로 찾기, 고슴도치 이동, 물도 이동, 최소 시간
    고슴도치: 상, 하, 좌, 우
    물: 비어있는 곳으로 상, 하, 좌, 우

    D.*
    ...
    .S.

    water_q: [(0,1), (2,1)]
    player_q: [(1,1), (2,0), (2,2)]

    => 큐 길이 측정 필요함

    idea: bfs
        - 특수 블록 위치 찾기 (시작, 종점, 물)
        - outer loop: 시간
        - 고슴 도치 이동 조건:
            - 이동 방향 1~2칸 앞에 물이 존재 X
                - 2칸 앞에 판정할 떄, 2칸 앞이 그리드를 벗어난 곳이면 그냥 큐에 포함이 안되는구나
            - 이동 방향 1칸 앞에 벽 X
        - 물 이동 조건:
            - 도착지 침범 불가
        - 고슴 도치 큐, 물 큐 두개 사용
        - 루프 종료 조건:
            ..?
        - 방문 처리 배열도 필요함
        - 물부터 이동 시키면, 자연스럽게 물이 찰 예정인 칸 판정 가능함
    """
    def is_valid(curr_y: int, curr_x: int) -> bool:
        return -1 < curr_y < R and -1 < curr_x < C

    def is_safe(future_y, future_x) -> int:
        if -1 < future_y < R and -1 < future_x < C:
            if grid[future_y][future_x] != "*":
                return 1
            else:
                return 0
        return 1

    # init data structure
    input = sys.stdin.readline
    R, C = map(int, input().split())
    visited = [[0]*C for _ in range(R)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid, src, goal, waters = [], [], [], []
    for y in range(R):
        col = list(map(str, input().rstrip()))
        for x in range(C):
            if col[x] == "D":
                goal.append((y,x))
            elif col[x] == "S":
                col[x] = "."
                src.append((y,x))
                visited[y][x] = 1
            elif col[x] == "*":
                waters.append((y,x))

        grid.append(col)

    # loop of time
    answer = 0
    player_q, water_q = deque(src), deque(waters)
    while player_q:  # for counting time
        for i in range(len(water_q)):
            wvy, wvx = water_q.popleft()  # water
            for j in range(4):
                wny, wnx = wvy + dy[j], wvx + dx[j]
                if is_valid(wny, wnx) and grid[wny][wnx] == ".":
                    grid[wny][wnx] = "*"
                    water_q.append((wny, wnx))

        for i in range(len(player_q)):
            vy, vx = player_q.popleft()
            for j in range(4):
                ny, nx = vy + dy[j], vx + dx[j]
                fy, fx = vy + dy[j]*2, vx + dx[j]*2
                if is_valid(ny, nx):
                    if grid[ny][nx] == "D":  # end point when we can find the escape point
                        print(answer + 1)
                        return

                    if grid[ny][nx] == "." and not visited[ny][nx] and is_safe(fy, fx):
                        visited[ny][nx] = 1
                        player_q.append((ny, nx))

        answer += 1

    print("KAKTUS")


if __name__ == "__main__":
    solution()
