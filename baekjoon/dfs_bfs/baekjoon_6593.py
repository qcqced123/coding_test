import sys
from collections import deque


def solution():
    """ 최단 경로 찾기, 3차원 그리드....? 6가지 방향 이동 가능
    idea: bfs with 3D array
        - 6개 방향 정의
        - 시작 위치, 종료 위치 잡기
        - 방문 배열 정의
    point:
        - 엣지 케이스 처리
            - (1,1,1) 케이스는 불가능!
    """
    input = sys.stdin.readline
    dz, dy, dx = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)
    while True:
        L, R, C = map(int, input().split())
        if not L and not R and not C:
            return

        # init the data structure
        grid = []
        sz, sy, sx = 0, 0, 0
        ez, ey, ex = 0, 0, 0
        for i in range(L):
            floor = []
            for j in range(R+1):
                col = list(map(str, input().rstrip()))
                if col:
                    floor.append(col)

                    for k in range(C):
                        if col[k] == "S":
                            sz, sy, sx = i, j, k

                        elif col[k] == "E":
                            ez, ey, ex = i, j, k

            grid.append(floor)

        # do bfs
        flag = 0
        q = deque([(sz, sy, sx)])
        visited = [[[0]*C for _ in range(R)] for _ in range(L)]
        while q:
            vz, vy, vx = q.popleft()
            vt = visited[vz][vy][vx]
            for i in range(6):
                nz, ny, nx = vz + dz[i], vy + dy[i], vx + dx[i]
                if nz == ez and ny == ey and nx == ex:
                    flag += 1
                    print(f"Escaped in {vt+1} minute(s).")
                    break

                if -1 < nz < L and -1 < ny < R and -1 < nx < C and not visited[nz][ny][nx] and grid[nz][ny][nx] == ".":
                    q.append((nz, ny, nx))
                    visited[nz][ny][nx] = vt + 1
            if flag:
                break
        else:
            print("Trapped!")


if __name__ == "__main__":
    solution()
