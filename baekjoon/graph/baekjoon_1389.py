import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    grid = [[float('inf')]*(N+1) for _ in range(N+1)]  # for matching input's node nums and index node nums
    for _ in range(M):
        src, end = map(int, sys.stdin.readline().split())
        grid[src][end], grid[end][src] = 1, 1

    for k in range(1, N+1):  # for stop-over
        for y in range(1, N+1):
            for x in range(1, N+1):
                if y == x:
                    continue
                grid[y][x] = min(grid[y][x], grid[y][k] + grid[k][x])

    result = [0, 999999999]
    for r in range(1, N+1):
        cnt = 0
        for c in range(1, N+1):
            if grid[r][c] < float('inf'):
                cnt += grid[r][c]

        if cnt < result[1]:
            result[0], result[1] = r, cnt
    print(result[0])


if __name__ == "__main__":
    solution()
