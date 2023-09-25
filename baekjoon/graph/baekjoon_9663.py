import sys
from typing import List
"""
[요약]
1) N-Queen
    - 10초, 128mb, N ≤ 15
    => Back-Tracking 이라서 넉넉함
[풀이]
1) Back Tracking
    - 방문 처리 (대각선, 가로, 세로)
    -
"""


def dfs(x: int, y: int, tmp: int, graph: List[List[int]]):
    if tmp == len(graph):
        result.append(1)
        return
    # 1) init cannot visited
    for i in range(len(graph)):
        graph[x][i] = -1
        graph[i][i] = -1,
        graph[i][y] = -1
    graph[x][y] = 1
    print(graph)
    # 2) Back Track
    for col in range(1, len(graph)):
        for row in range(1, len(graph)):
            if not graph[row][col]:
                dfs(row, col, tmp + 1, graph)


N = int(sys.stdin.readline())
grid, result = [[0] * N for _ in range(N)], []
for i in range(N):
    dfs(i, 0, 1, grid)
print(len(result))
