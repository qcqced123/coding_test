import sys
from collections import deque


def solution():
    """ 사이클 탐지

    idea: bfs, disjoint, union find
        1) visited 배열로 새로운 사이클, 기존 사이클 여부 판정

    reference:
        https://www.acmicpc.net/board/view/73547
    """
    def move(y: int, x: int) -> int:
        group = set()
        while True:
            if not visited[y][x]:
                group.add((y, x))
                visited[y][x] = 1
                cnt_dir = dir[grid[y][x]]
                y += dy[cnt_dir]
                x += dx[cnt_dir]

            else:
                if (y, x) in group:
                    return 1
                else:
                    return 0

    dir = {
        "U": 0,
        "D": 1,
        "L": 2,
        "R": 3
    }
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    N, M = map(int, sys.stdin.readline().split())

    grid = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    result = 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c]:
                result += move(r, c)
    print(result)


if __name__ == "__main__":
    solution()
