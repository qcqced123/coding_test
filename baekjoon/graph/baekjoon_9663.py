import sys, copy
from typing import List
"""
[풀이]
1) Backtracking + DFS
    - 1D array vs 2D array
    - 0행 어디에 퀸을 두는가에 따라 경우의 수가 달라짐
    - 가로, 세로, 대각선 모두 방문 처리
        - 대각선: 로우 차이 == 컬럼 차이
    - DFS 탐색
    visited가 지금 mutable이구나
"""


def dfs(y: int, x: int, visit: List[List[bool]], tmp: int):
    global result
    # 2) check possible case
    if tmp == N:
        result += 1
        return

    # 1) apply chess rule
    for i in range(y, N):  # 대각 방향 모두 처리
        for j in range(N):
            if x == j:  # 세로 방향 처리
                visit[i][j] = True
                continue

            if not visit[y][j]:  # 가로 방향 처리
                visit[y][j] = True
                continue

            if abs(y-i) == abs(x-j):  # 대각 방향 처리
                visit[i][j] = True
                continue
    # 2) DFS
    next_row = y+1
    c_visit = copy.deepcopy(visit)
    for col in range(N):
        if not visit[next_row][col]:
            dfs(next_row, col, c_visit, tmp+1)
        visit[next_row][col] = True


def solution():
    for i in range(N):
        visited = [[False]*N for _ in range(N)]
        dfs(0, i, visited, 1)
    print(result)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    N = int(sys.stdin.readline())
    result = 0
    solution()
