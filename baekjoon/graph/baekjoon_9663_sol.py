import sys


def check(x: int):
    for i in range(x):
        if grid[x] == grid[i] or abs(grid[x] - grid[i]) == abs(x - i):  # 같은 열에 있는지 & 대각선에 퀸이 있는지 검사
            return False
    return True


def dfs(x: int):
    global result
    if x == N:
        result += 1
        return
    for i in range(N):
        grid[x] = i
        if check(x):
            dfs(x+1)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    N = int(sys.stdin.readline())
    grid, result = [0 for _ in range(N)], 0
    dfs(0)
    print(result)
