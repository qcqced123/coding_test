import sys
from collections import defaultdict


def solution():
    """
    idea: floyd warshall
        - printing the first node of shortest path
        - need to caching the whole path
    """
    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())

    # init the floyd warshall grid
    cache = defaultdict(list)
    grid = [[INF]*(N+1) for _ in range(N+1)]
    answer = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        src, end, cost = map(int, input().split())
        if cost < grid[src][end]:
            grid[src][end], grid[end][src] = cost, cost
            cache[(src, end)], cache[(end, src)] = [src, end], [end, src]

    # do floyd-warshall
    for k in range(1, N+1):
        for y in range(1, N+1):
            for x in range(1, N+1):
                if y != x:
                    vc = grid[y][x]
                    nc = grid[y][k] + grid[k][x]
                    if nc < vc:
                        grid[y][x] = nc
                        cache[(y,x)] = cache[(y,k)] + cache[(k,x)][1:]

    # update the answer grid
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j: answer[i][j] = cache[(i,j)][1]
            else: answer[i][j] = "_"

    # check the current state of grid
    for i in range(1, N+1):
        print(*answer[i][1:], end="\n")


if __name__ == "__main__":
    solution()
