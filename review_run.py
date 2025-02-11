import sys
from collections import deque

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """
    # bfs func
    def bfs(y: int, x: int, path: str):
        visited.add(path)
        q = deque([(path, y, x, 0)])
        while q:
            vp, vy, vx, vc = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < 3 and -1 < nx < 3:
                    cnt = list(vp)
                    cnt[vy * 3 + vx], cnt[ny * 3 + nx] = cnt[ny * 3 + nx], "0"
                    np = "".join(cnt)
                    if np == result:
                        return vc + 1

                    if np not in visited:
                        visited.add(np)
                        q.append((np, ny, nx, vc + 1))
        return -1

    # init data structure
    result = "123456780"
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(3)]

    # find the starting point
    sy, sx = None, None
    for i in range(3):
        for j in range(3):
            if not grid[i][j]:
                sy, sx = i, j
                break

    # do bfs
    visited = set()
    sp = ""
    for i in range(3):
        sp += "".join(map(str, grid[i]))

    print(bfs(sy, sx, sp) if result != sp else 0)


if __name__ == '__main__':
    solution()