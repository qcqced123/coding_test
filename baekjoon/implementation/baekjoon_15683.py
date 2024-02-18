import sys
import copy
from collections import deque
from typing import List


def solution():
    sys.setrecursionlimit(10**5)
    grid, cams, result = [], [], [999999999]
    N, M = map(int, sys.stdin.readline().split())
    for i in range(N):
        col = list(map(int, sys.stdin.readline().split()))
        grid.append(col)
        for j in range(M):
            if 0 < col[j] < 6:
                cams.append((col[j], i, j))
    # 상, 하, 좌, 우
    cam_type = {
        0: 0,
        1: deque([0, 0, 0, 1]),  # rotate 3
        2: deque([0, 0, 1, 1]),  # rotate 1
        3: deque([0, 1, 0, 1]),  # rotate 3
        4: deque([0, 1, 1, 1]),  # rotate 3
        5: deque([1, 1, 1, 1]),  # 회전 의미 없음
    }
    nums_rotate = (0, 4, 2, 4, 4, 1)
    size_rotate = (0, 1, 2, 1, 1, 0)

    def calculate(arr) -> int:
        total = 0
        for i in range(N):
            for j in range(M):
                if not arr[i][j]:
                    total += 1
        return total

    def marking(arr, y: int, x: int, d: int):
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        y += dy[d]
        x += dx[d]
        if -1 < y < N and -1 < x < M and (not arr[y][x] or arr[y][x] == -1):
            arr[y][x] = -1
            marking(arr, y, x, d)

        elif -1 < y < N and -1 < x < M and 0 < arr[y][x] < 6:
            marking(arr, y, x, d)

    def dfs(arr, curr):
        if not len(curr):
            result[0] = min(result[0], calculate(arr))
            return

        cam, y, x = curr[0]
        for _ in range(nums_rotate[cam]):
            array = copy.deepcopy(arr)
            for idx, d in enumerate(cam_type[cam]):
                if d == 1:
                    marking(array, y, x, idx)
            for i in range(0, len(curr)):
                new_curr = curr[i+1:]
                dfs(array, new_curr)

            cam_type[cam].rotate(size_rotate[cam])

    dfs(grid, cams)
    print(result[0])


if __name__ == "__main__":
    solution()
