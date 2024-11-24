import sys
import copy
from collections import deque
from itertools import combinations


def solution():
    """
    idea: simulation with adj array, bfs, backtracking (조합)
        - 최소 시간 구해야 해서, bfs 유리
        - outer loop: time

    1) 바이러스 위치 리스트 만들기
    2) 조합 이용해서 경우의 수 만들기
    3) 조합 경우의 수를 outer loop 이용, 값 업데이트
        - bfs
        - update the answer
        - 모든 칸에 바이러스를 놨는지 판정하는 알고리즘이 까다로운데..?
            - 이중 루프 돌려도 되려나..?
    """
    # init the data structure
    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    N, ACTIVE = map(int, input().split())  # size of grid, 활성 바이러스 숫자
    graph = [list(map(int, input().split())) for _ in range(N)]


    # make the initial virus pos list
    virus = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2: virus.append((i, j))

    # make the combinations case
    combs = combinations(range(len(virus)), ACTIVE)
    for comb in combs:
        # init the backtracking
        grid = copy.deepcopy(graph)
        src_point = []
        for idx in comb:
            active_y, active_x = virus[idx]
            grid[active_y][active_x] = 3
            src_point.append((active_y, active_x))

        time = 0
        q = deque(src_point)
        visited = [[0]*N for _ in range(N)]
        while True:
            for i in range(len(q)):
                vy, vx = q.popleft()
                for j in range(4):
                    ny, nx = vy + dy[j], vx + dx[j]
                    if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and (not grid[ny][nx] or grid[ny][nx] == 2):
                        q.append((ny, nx))
                        grid[ny][nx] = 3
                        visited[ny][nx] = 1
            if not q:
                for y in range(N):
                    for x in range(N):
                        if not grid[y][x]:
                            print(-1)
                            return
                else:
                    print(time)
                    break

            time += 1


if __name__ == "__main__":
    solution()
