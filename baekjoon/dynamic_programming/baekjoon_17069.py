import sys


def solution():
    """
    idea: dynamic programming with adj array
        - 3차원 dp cache array 선언
            - 행 좌표, 열 좌표, 이전 방향
            - 0번 인덱스: 이전 방향이 가로
            - 1번 인덱스: 이전 방향이 세로
            - 2번 인덱스: 이전 방향이 대각선
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [[[0]*3 for _ in range(N)] for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]

    # update the dp cache array
    cache[0][0][0] = 1
    for i in range(1, N):
        if cache[0][i-1][0] and not grid[0][i]:
            cache[0][i][0] = 1

    cache[0][0][0] = 0
    for y in range(1, N):
        for x in range(1, N):
            if not grid[y][x]:
                cache[y][x][0] = cache[y][x-1][0] + cache[y][x-1][2]
                cache[y][x][1] = cache[y-1][x][1] + cache[y-1][x][2]
                if not grid[y-1][x] and not grid[y][x-1]:
                    cache[y][x][2] = cache[y-1][x-1][0] + cache[y-1][x-1][1] + cache[y-1][x-1][2]

    print(sum(cache[-1][-1]))


if __name__ == "__main__":
    solution()
