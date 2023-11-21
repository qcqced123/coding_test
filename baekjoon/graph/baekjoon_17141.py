import sys, copy
from collections import deque
from itertools import combinations
"""
[조건]
1) 상하좌우 이동
    - 빈 칸에 바이러스 복제: 1초 걸림
    => 모든 객체 동시 이동 구현 필요
    - 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수
    => 바이러스 개수랑 M이 똑같은게 아님, 2는 그냥 바이러스를 놓을 수 있는 칸의 개수
    => 바이러스 위치를 조합해서 최소 시간을 구하는게 목적
[풀이]
1) 자료구조 정의
    - 그래프, 방문 여부, 이동 방향, 바이러스 위치
2) 바이러스 놓기
    - 그래프에서 2 위치 미리 찾기
    - 바이러스 놓은 위치는 3으로 바꾸기
3) BFS
    - 반드시 빈칸만 복제 가능
4) 빈 칸 있는지 판정
"""


def solution():
    N, M = map(int, sys.stdin.readline().split())  # size, num of virus
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # list for mutable

    # 2) 바이러스 놓는 경우의 수
    pos = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                pos.append((i, j))
    case = combinations(pos, M)
    # 3) BFS by time
    result = []
    for idx in case:
        graph = copy.deepcopy(grid)
        visited = [[False] * N for _ in range(N)]  # list for mutable
        virus = deque([])
        for y, x in idx:
            graph[y][x] = 3  # 바이러스 놓자마자 끝나는 경우의 수 때문에, 2와는 다른 값으로 설정해줘야 한다.
            virus.append((y, x))
        tmp = 0
        while virus:
            for _ in range(len(virus)):
                vy, vx = virus.popleft()
                for i in range(4):
                    ny = dy[i] + vy
                    nx = dx[i] + vx
                    # graph[i][j] == 2도 포함해야 한다
                    if -1 < ny < N and -1 < nx < N and (graph[ny][nx] == 0 or graph[ny][nx] == 2) and not visited[ny][nx]:
                        visited[ny][nx] = True
                        graph[ny][nx] = 3
                        virus.append((ny, nx))
            if not virus:
                break
            tmp += 1

        # 4) 빈 칸 있는지 판정
        curr = False
        for i in range(N):
            for j in range(N):
                if not graph[i][j] or graph[i][j] == 2:
                    curr = True
                    break
            if curr:
                break
        result.append(tmp if not curr else float('inf'))
    final = min(result)
    print(final if final != float('inf') else -1)


if __name__ == "__main__":
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)  # tuple for immutable
    solution()

