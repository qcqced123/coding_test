import sys


def solution():
    """ 로봇 이동: 오른쪽, 하단, 경유지 반드시 경유 (다행히도 경유지는 한 개)
    idea: dynamic programming
        -
    """
    # init data structure
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    cache = [[0]*M for _ in range(N)]  # grid and dp cache

    # initialize for the first row and col
    for i in range(M):
        cache[0][i] = 1

    for i in range(N):
        cache[i][0] = 1

    # middle point
    if K:
        mid_y, mid_x = divmod(K, M)
        if not mid_x:
            mid_y -= 1
            mid_x = M - 1
        else:
            mid_x -= 1

        for y in range(1, mid_y+1):
            for x in range(1, mid_x+1):
                cache[y][x] = cache[y-1][x] + cache[y][x-1]

        middle = cache[mid_y][mid_x]
        for i in range(mid_x+1, M):
            cache[mid_y][i] = middle
        for i in range(mid_y+1, N):
            cache[i][mid_x] = middle

        for y in range(mid_y+1, N):
            for x in range(mid_x+1, M):
                cache[y][x] = cache[y-1][x] + cache[y][x-1]

    # not middle point
    else:
        for y in range(1, N):
            for x in range(1, M):
                cache[y][x] = cache[y-1][x] + cache[y][x-1]

    print(cache[N-1][M-1])


if __name__ == "__main__":
    solution()
