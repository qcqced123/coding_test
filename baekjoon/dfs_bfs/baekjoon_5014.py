import sys
from collections import deque
from typing import List
"""
[풀이]
1) 눌러야 하는 버튼 최소값: 가장 작은걸 타겟 인덱스 위치에 저장
"""


def solution():
    grid = [-1]*(F+1)
    grid[S] = 0
    q = deque([S])
    while q:
        vx = q.popleft()
        for i in range(2):
            nx = dx[i] + vx
            if 0 < nx < F+1 and grid[nx] == -1:
                q.append(nx)
                grid[nx] = grid[vx] + 1
            if 0 < nx < F+1 and grid[nx]:
                grid[nx] = min(grid[nx], grid[vx] + 1)
    print(grid[G]) if grid[G] != -1 else print("use the stairs")


if __name__ == "__main__":
    F, S, G, U, D = map(int, sys.stdin.readline().split())
    dx = [U, -D]
    solution()
