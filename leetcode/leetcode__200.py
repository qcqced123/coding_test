from collections import deque
from typing import List


class Solution:
    def bfs(self, y: int, x: int, grid: List[List[str]], visit: List[bool], row: int, col: int) -> None:
        dy = [0, 0, -1, 1]
        dx = [-1, 1, 0, 0]

        visit[y][x] = True
        queue = deque()
        queue.append([y, x])

        while queue:
            vy, vx = queue.popleft()
            for i in range(4):
                ny = dy[i] + vy
                nx = dx[i] + vx
                if -1 < ny < row and -1 < nx < col and not visit[ny][nx] and grid[ny][nx] == '1':
                    visit[ny][nx] = True
                    queue.append([ny, nx])

    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited, result = [[False] * col for _ in range(row)], 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    self.bfs(i, j, grid, visited, row, col)
                    result += 1
        return result
