import sys


def solution():
    """ 2차원 테이블 누적합
    idea: prefix sum
    """
    # init data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    prefix = [[0]*(M+1) for _ in range(N+1)]
    queries = [tuple(map(int, input().split())) for _ in range(int(input()))]

    # init prefix
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # answering the questions
    for query in queries:
        ly, lx, ry, rx = query
        print(prefix[ry][rx] - prefix[ly-1][rx] - prefix[ry][lx-1] + prefix[ly-1][lx-1])


if __name__ == "__main__":
    solution()
