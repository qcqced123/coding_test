import sys
import copy
from collections import deque
from typing import List
"""
[구현]
1) 격자 나누기 (0)
2) 격자 회전: 시계 방향 90도 (0)
3) 인접 얼음 칸 개수에 따라서 얼음 값 갱신 (0)
    - 계산도 일괄 적용하는 방법으로 가야함 (0)
4) 전체 합 구하기, 5) 덩어리 크기 계산하기
"""


def solution():
    N, Q = map(int, sys.stdin.readline().split())
    size = 2**N
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
    visit = [[0]*size for _ in range(size)]
    levels = [int(sys.stdin.readline())] if Q == 1 else list(map(int, sys.stdin.readline().split()))
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    def divide(y: int, x: int, n: int, l: int, graph: List[List]):
        if n > l:
            divide(y, x, n // 2, l, graph)
            divide(y, x + (n // 2), n // 2, l, graph)
            divide(y + (n // 2), x, n // 2, l, graph)
            divide(y + (n // 2), x + (n // 2), n // 2, l, graph)
            return

        elif n == l:
            rotation(y, x, n, graph)
            return

    def rotation(y: int, x: int, n: int, graph: List[List]):
        curr_col = x + n - 1
        for r in range(y, y+n):
            tmp = []
            for c in range(x, x+n):
                tmp.append(graph[r][c])
            for k in range(len(tmp)):
                grid[y+k][curr_col] = tmp[k]

            curr_col -= 1

    def calculate() -> List:
        result = []
        for r in range(size):
            for c in range(size):
                count = 0
                if grid[r][c]:
                    for i in range(4):
                        nr, nc = dy[i] + r, dx[i] + c
                        if -1 < nr < size and -1 < nc < size and grid[nr][nc]:
                            count += 1

                    if count <= 2:
                        result.append((r, c))

        return result

    def bfs(y: int, x: int):
        count = 1
        visit[y][x] = 1
        q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < size and -1 < nx < size and not visit[ny][nx] and grid[ny][nx]:
                    count += 1
                    visit[ny][nx] = 1
                    q.append((ny, nx))

        return count

    while Q:
        arr = copy.deepcopy(grid)
        level = 2**levels[len(levels)-Q]
        divide(0, 0, size, level, arr)

        cnt = calculate()
        for vy, vx in cnt:
            grid[vy][vx] -= 1

        Q -= 1

    print(sum(map(sum, grid)))
    result = 0
    for r in range(size):
        for c in range(size):
            if grid[r][c] and not visit[r][c]:
                result = max(result, bfs(r, c))
    print(result)


if __name__ == "__main__":
    solution()
