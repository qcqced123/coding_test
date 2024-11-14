import sys
from collections import deque


def solution():
    """
    condit 1: 공기랑 닿으면 사라짐
        - 치즈 안쪽 공간은 공기 x

    idea: graph search
        - outer loop: 시간
            - 빈공간 vs 공기 판정
                 - 공기 쪽에서 탐색해서 이어지면, 그냥 빈공간이 공간이 되겠지??

            - 사라질 치즈 찾기
                - 동시에 사라져야 해서, 리스트에 위치만 담기

            - 리스트에 담긴 치즈 모두 삭제
    """
    # helper function
    def find_air() -> None:
        visited = set()
        visited.add((0,0))
        q = deque([(0,0)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M and (ny, nx) not in visited and grid[ny][nx] != 1:  # optimize
                    grid[ny][nx] = 2
                    visited.add((ny,nx))
                    q.append((ny,nx))

    def find_removable_cheese(y: int, x: int) -> None:
        q = deque([(y,x)])
        record.add((y,x))
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M and (ny,nx) not in record and grid[ny][nx] == 1: # optimize
                    # is there any adj air?
                    for j in range(4):
                        ay, ax = ny + dy[j], nx + dx[j]
                        if -1 < ay < N and -1 < ax < M and grid[ay][ax] == 2:
                            del_list.append((ny, nx))
                            break
                    record.add((ny, nx))
                    q.append((ny, nx))

    input = sys.stdin.readline
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # do the bfs
    time, last = 0, 0
    while True:
        find_air()
        del_list, record = [], set()
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 1 and (y, x) not in record:
                    del_list.append((y, x))
                    find_removable_cheese(y, x)

        if not del_list:
            break

        for r, c in del_list:
            grid[r][c] = 2
        time += 1
        last = len(del_list)

    print(time)
    print(last)


if __name__ == "__main__":
    solution()
