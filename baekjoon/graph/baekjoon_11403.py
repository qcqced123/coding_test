import sys


def solution():
    N = int(sys.stdin.readline())
    grid = []
    for _ in range(N):
        col = list(map(int, sys.stdin.readline().split()))
        for i in range(N):
            if not col[i]:
                col[i] = float('inf')
        grid.append(col)

    for k in range(N):
        for r in range(N):
            for c in range(N):
                grid[r][c] = min(grid[r][c], grid[r][k] + grid[k][c])

    for r in range(N):
        for c in range(N):
            if grid[r][c] == float('inf'):
                grid[r][c] = 0
            elif grid[r][c] > 1:
                grid[r][c] = 1
        print(*grid[r], end='\n')


if __name__ == "__main__":
    solution()
