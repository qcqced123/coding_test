import sys
from collections import deque
from itertools import combinations


def solution4():
    INF = sys.maxsize
    N, M = map(int, input().split())  # size of grid, number of virus in init active grid
    dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # make the virus position list
    empty = 0
    virus = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                virus.append((i, j))
            elif not grid[i][j]:
                empty += 1
    if not empty:
        print(0)
        return

    # make the case of combinations, do bfs with each case for updating the answer
    answer = INF
    combs = combinations(range(len(virus)), M)
    for comb in combs:
        visited = [[-1] * N for _ in range(N)]
        virus_q = deque([virus[c] for c in comb])
        while virus_q:
            vy, vx = virus_q.popleft()
            # for initializing the starting active virus
            if visited[vy][vx] == -1:
                visited[vy][vx] += 1

            # current active virus value is == 0
            vt = visited[vy][vx]

            # find the next node
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and grid[ny][nx] != 1 and visited[ny][nx] == -1:
                    if not grid[ny][nx]:
                        visited[ny][nx] = vt + 1
                        virus_q.append((ny, nx))

                    # 그냥 큐에 넣질말자
                    elif grid[ny][nx] == 2:
                        visited[ny][nx] = vt

        # update the answer value with current state of grid
        cache, flag = 0, 0
        for y in range(N):
            for x in range(N):
                if (grid[y][x] == 0 or grid[y][x] == 2) and visited[y][x] == -1:
                    flag += 1
                    break

                cache = max(cache, visited[y][x])

            if flag:
                break

        else:
            answer = min(answer, cache)

    print(answer) if answer != INF else print(-1)


if __name__ == "__main__":
    solution4()
