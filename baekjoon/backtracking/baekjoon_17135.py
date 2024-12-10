import sys
from copy import deepcopy
from collections import deque
from itertools import combinations


def solution():
    """
    condition:
        - 사정 거리 내부 가장 가까운 적, 왼쪽부터 공격
        - 한 번에 한 개만 공격
        - 모든 궁수 동시 공격
        - 궁수 공격 이후, 적들은 동시에 아래로 한 칸씩 이동
        - 성에 닿으면 삭제 (격자 밖으로 벗어나면 삭제)

    => 궁수 배치 잘해서 죽일 수 있는 최대 적 구하기
    idea: simulation with backtracking, bfs
        - 조합 이용해서 궁수 배치하는 경우의 수 구하기
        - 경우의 수마다 시물레이션 실행
            - 그리드 복사
            - 삭제 대상 위치 리스트 만들기
                - bfs 사용해서 최단 사정거리, 가장 왼쪽인 친구 찾기
    """
    # helper func
    def is_valid() -> int:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    return 0
        return 1

    def bfs(y, x) -> tuple:
        visited = set()
        visited.add((y, x))
        q = deque([(y, x, 0)])
        result_y, result_x, result_distance = None, None, INF
        while q:
            vy, vx, vd = q.popleft()
            for i in range(4):
                ny, nx, nd = vy + dy[i], vx + dx[i], vd + 1
                if -1 < ny < N and -1 < nx < M and (ny, nx) not in visited and nd <= D:
                    if graph[ny][nx] == 1:
                        if nd < result_distance:
                            result_y, result_x, result_distance = ny, nx, nd
                        elif nd == result_distance and nx < result_x:
                            result_y, result_x = ny, nx

                        continue

                    visited.add((ny, nx))
                    q.append((ny, nx, vd+1))

        return (result_y, result_x)

    INF = sys.maxsize
    input = sys.stdin.readline
    dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)  # 탐색 방향 설정을 제일 먼저 왼쪽으로 두면 될 듯!
    N, M, D = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # get case from combinations
    answer = 0
    for comb in combinations(range(M), 3):
        # deep copy for backtracking
        graph = deepcopy(grid)

        # get del list
        cache = 0
        while True:
            del_list = set()
            for player in comb:
                py, px = N, player
                result = bfs(py, px)
                if result[0] is None:
                    continue
                del_list.add(result)

            # apply result of del_list
            for y, x in del_list:
                cache += 1
                graph[y][x] = 0

            # move the monster
            for i in range(N-1, -1, -1):
                for j in range(M):
                    if graph[i][j] == 1:
                        graph[i][j] = 0
                        if i != N-1:
                            graph[i+1][j] = 1
            # check current state of graph is valid
            if is_valid():
                break

        answer = max(answer, cache)
    print(answer)


if __name__ == "__main__":
    solution()
