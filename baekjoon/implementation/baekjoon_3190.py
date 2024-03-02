import sys
from collections import deque
from typing import List


def solution():
    N = int(sys.stdin.readline())
    grid = [[0]*N for _ in range(N)]

    curr_y, curr_x = 0, 0  # snake's pos init
    grid[curr_y][curr_x] = 1

    K = int(sys.stdin.readline())
    for _ in range(K):
        src, end = map(int, sys.stdin.readline().split())
        grid[src-1][end-1] = 2

    L = int(sys.stdin.readline())
    moves = deque([tuple(map(str, sys.stdin.readline().split())) for _ in range(L)])  # must string int convert into int
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

    def bfs(y: int, x: int, d: int, graph: List[List]) -> int:
        time = 0
        q = deque([(y, x)])
        g_t, g_d = moves.popleft()  # g_t must change to int
        snake_q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            ny, nx = dy[d] + vy, dx[d] + vx
            if -1 < ny < N and -1 < nx < N and not graph[ny][nx]:  # 사과가 없는 경우
                graph[ny][nx] = 1
                q.append((ny, nx))

                ty, tx = snake_q.popleft()
                graph[ty][tx] = 0
                snake_q.append((ny, nx))

            elif -1 < ny < N and -1 < nx < N and graph[ny][nx] == 2:  # 사과가 있는 경우
                graph[ny][nx] = 1
                q.append((ny, nx))
                snake_q.append((ny, nx))

            elif ny <= -1 or ny >= N or nx <= -1 or nx >= N or graph[ny][nx] == 1:
                break

            time += 1
            if time == int(g_t):
                if g_d == 'L':  # 반시계
                    d = d-1 if d != RIGHT else 3
                else:  # 시계 방향
                    d = d+1 if d != UP else 0
                if len(moves):
                    g_t, g_d = moves.popleft()

        return time+1

    print(bfs(curr_y, curr_x, RIGHT, grid))


if __name__ == "__main__":
    solution()
