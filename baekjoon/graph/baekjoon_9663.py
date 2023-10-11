import sys
from typing import List

"""
[풀이]
1) Back Tracking
    1-1) 말을 놓는다 (graph)
        - 갈 수 없는 곳을 죄다 체크 (visited)
        - 말을 놓을 수 있다면 놓고 다음 행으로 넘어가서 위 과정 반복
"""


def dfs(r: int, c: int, graph: List[List[int]], visit: List[List[bool]], count: int):
    global result
    if count == N:
        result += 1
        return

    for row in range(N):
        for col in range(N):
            if row == r or col == c or abs(col-c) == row:
                visit[row][col] = True

    for x in range(N):
        if not visit[r+1][x]:
            graph[r+1][x] = 0
            dfs(r+1, x, graph, visit, count+1)  # 돌아오면 여기 뒤쪽 부터 실행
            graph[r+1][x] = -1
    if 1 not in graph[r+1]:
        return


def solution():
    for i in range(N):
        grid, visited = [[-1] * N for _ in range(N)], [[False] * N for _ in range(N)]
        grid[0][i] = 0
        dfs(0, i, grid, visited, 1)
    print(result)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    N = int(sys.stdin.readline())
    result = 0
    solution()
