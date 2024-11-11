import sys


def solution():
    """ N**3
    idea: dynamic programming
        - dp[i][j] = arr[i][j] + max(세방향)
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cache = [[0]*M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            left = cache[y][x-1] if x-1 > -1 else 0
            diagonal = cache[y-1][x-1] if y - 1 > -1 and x-1 > -1 else 0
            down = cache[y-1][x] if y - 1 > -1 else 0
            cache[y][x] = arr[y][x] + max(left, diagonal, down)

    print(cache[N-1][M-1])


if __name__ == "__main__":
    solution()
