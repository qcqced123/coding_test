import sys
from collections import deque
from typing import List

#
# def solution1():
#     """
#     problem link:
#         https://www.acmicpc.net/problem/1520
#
#     summary:
#         1) 등고선 말하는 듯
#           - 테이블 탐색, 상 하 좌 우
#           - 항상 위에서 아래로 이동
#           - 백트래킹스럽게 풀어야 할 듯??
#           => 경로의 개수 구하기
#     args:
#         1) DFS with Backtracking (세제곱까지 가능)
#           - 계단수 이용 (0)
#             - 스택을 쓰자: visit를 스택으로 쓰면서 동시에 값 비교까지 (0)
#             - 앞 뒤를 연쇄적으로 비교하면서, 지속적으로 감소하는지 체크하기
#           - 맨 처음 시작 위치는 visit에 넣고 시작 (ㅌ)
#
#     solution:
#
#     """
#     M, N = map(int, sys.stdin.readline().split())
#     grid = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
#     visit = [[0]*N for _ in range(M)]
#
#     result = [0]
#     dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
#     sys.setrecursionlimit(10**6)
#
#     def dfs(y: int, x: int):
#         if y == M-1 and x == N-1:
#             result[0] += 1
#             return
#
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             if -1 < ny < M and -1 < nx < N and not visit[ny][nx] and grid[ny][nx] < grid[y][x]:  # 이부분 visit로 바꿀수도
#                 visit[ny][nx] = 1
#                 dfs(ny, nx)
#                 visit[ny][nx] = 0
#
#     dfs(0,0)
#     print(result[0])


def solution2():
    """
    problem link:
        https://www.acmicpc.net/problem/1520

    solution:
        1) DFS/BFS + DP
          - Backtracking have time limit
          - So, 3D Table with path
    """
    M, N = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    dp = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(M)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    def bfs(y: int, x: int):
        visit = set()
        visit.add(str(grid[y][x]))
        q = deque([(None, str(grid[y][x]), y, x)])  # dir, path, y, x
        while q:
            vd, vp, vy, vx = q.popleft()
            for i in range(4):
                nd, ny, nx = i, vy + dy[i], vx + dx[i]
                if -1 < ny < M and -1 < nx < N:
                    np = vp + str(grid[ny][nx])
                    print(np)
                    if np not in visit and grid[ny][nx] < grid[y][x]:
                        dp[ny][nx][nd] += 1; visit.add(np)
                        if ny == M-1 and nx == N-1:
                            continue
                        q.append((nd, np, ny, nx))

    bfs(0,0)


if __name__ == "__main__":
    solution2()
