import sys
from copy import deepcopy
from collections import deque
from itertools import combinations


def solution():
    """
    idea: simulation with bfs, backtracking (combinations)
        - 바이러스 위치 리스트
        - 활성 바이러스 조합 뽑기
        - 조합 경우의 수마다 탐색, 기록
        - visited 배열에 '시간'을 기록하자
    """
    # init the data structure
    INF = sys.maxsize
    N, M = map(int, input().split())  # size of grid, number of virus in init active grid
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # make the virus position list
    virus = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                virus.append((i,j))

    # make the case of combinations, do bfs with each case for updating the answer
    answer = INF
    combs = combinations(range(len(virus)), M)
    for comb in combs:
        time = 0
        visited = deepcopy(grid)  # for recording
        virus_q = deque([virus[c] for c in comb])
        while True:
            for i in range(len(virus_q)):
                vy, vx = virus_q.popleft()
                if visited[vy][vx] != 3:
                    visited[vy][vx] = 3

                for j in range(4):
                    ny, nx = vy + dy[j], vx + dx[j]
                    if -1 < ny < N and -1 < nx < N and (not visited[ny][nx] or visited[ny][nx] == 2):
                        visited[ny][nx] = 3
                        virus_q.append((ny,nx))

            if not virus_q:
                for y in range(N):
                    for x in range(N):
                        if not visited[y][x]:
                            print(-1)
                            return
                else:
                    print(time)
                    break

            time += 1


def solution2():
    # init the data structure
    INF = sys.maxsize
    N, M = map(int, input().split())  # size of grid, number of virus in init active grid
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # make the virus position list
    virus = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                virus.append((i,j))
    # make the case of combinations, do bfs with each case for updating the answer
    answer = INF
    combs = combinations(range(len(virus)), M)
    for comb in combs:
        graph = deepcopy(grid)  # for recording
        visited = [[0]*N for _ in range(N)]
        virus_q = deque([virus[c] for c in comb])
        while virus_q:
            vy, vx = virus_q.popleft()
            vt = graph[vy][vx]
            if not visited[vy][vx]:
                visited[vy][vx] = 1

            for j in range(4):
                ny, nx = vy + dy[j], vx + dx[j]
                if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and graph[ny][nx] != 1:
                    if not graph[ny][nx]:
                        graph[ny][nx] = vt+1
                        visited[ny][nx] = 1
                        virus_q.append((ny, nx))

                    elif graph[ny][nx] == 2:
                        graph[ny][nx] = vt
                        visited[ny][nx] = 1
                        virus_q.append((ny, nx))


def solution3():
    """
    grid not deepcopy, record the value to visited array
    initialize the visited array with -1

    방문 조건:
        1) 빈

    """
    INF = sys.maxsize
    N, M = map(int, input().split())  # size of grid, number of virus in init active grid
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # make the virus position list
    virus = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                virus.append((i, j))
    # make the case of combinations, do bfs with each case for updating the answer
    answer = INF
    combs = combinations(range(len(virus)), M)
    for comb in combs:
        visited = [[-1] * N for _ in range(N)]
        virus_q = deque([virus[c] for c in comb])
        while virus_q:
            vy, vx = virus_q.popleft()
            if visited[vy][vx] == -1:
                visited[vy][vx] += 1

            vt = visited[vy][vx]
            for j in range(4):
                ny, nx = vy + dy[j], vx + dx[j]
                if -1 < ny < N and -1 < nx < N and visited[ny][nx] == -1:
                    if not grid[ny][nx]:
                        visited[ny][nx] = vt + 1
                        virus_q.append((ny,nx))

                    elif grid[ny][nx] == 2:
                        visited[ny][nx] = vt
                        virus_q.append((ny, nx))

        # check the current grid state
        cache = 0
        flag = True
        for i in range(N):
            for j in range(N):
                cache = max(cache, visited[i][j])

            if not flag:
                break
        else:
            answer = min(answer, cache)

    print(answer)


if __name__ == "__main__":
    solution3()
