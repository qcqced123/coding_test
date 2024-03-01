import sys
from collections import deque
from typing import List


def solution():
    N, M = map(int, sys.stdin.readline().split())
    robot_y, robot_x, robot_d = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    visit = [[0]*M for _ in range(N)]
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)  # for searching empty space

    def bfs(y: int, x: int, d: int, visited: List[List], graph: List[List]) -> int:
        result = 1
        visited[y][x] = 1
        q = deque([(d, y, x)])
        while q:
            temp = 0
            vd, vy, vx = q.popleft()
            for i in range(4):
                ny, nx = dy[i] + vy, dx[i] + vx
                if -1 < ny < N and -1 < nx < M and not graph[ny][nx] and not visited[ny][nx]:
                    temp += 1
            if temp:
                while True:
                    nd = 3 if not vd else vd-1
                    ny, nx = dy[nd] + vy, dx[nd] + vx
                    if -1 < ny < N and -1 < nx < M and not graph[ny][nx] and not visited[ny][nx]:
                        result += 1
                        visited[ny][nx] = 1
                        q.append((nd, ny, nx))
                        break
                    vd = nd
            else:
                by, bx = vy - dy[vd], vx - dx[vd]
                if -1 < by < N and -1 < bx < M and not graph[by][bx]:
                    q.append((vd, by, bx))
                    continue
                break
        return result
    print(bfs(robot_y, robot_x, robot_d, visit, grid))


if __name__ == "__main__":
    solution()
