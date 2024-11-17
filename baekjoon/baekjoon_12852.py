import sys


def solution():
    """
    idea: dynamic programming
        - bottom-up
        - 뒤에서 오는게 최소일수도 있어서, 캐시 배열 크기를 N*3까지 늘려야 함
    """
    INF = sys.maxsize
    input = sys.stdin.readline

    N = int(input())
    size = N+1
    cache = [INF]*size
    path = [[] for _ in range(N+1)]

    # update the cache array
    cache[1] = 0
    path[1] = [1]
    for i in range(1, size-1):
        if cache[i+1] > cache[i] + 1:
            cache[i+1] = cache[i] + 1
            path[i+1] = path[i] + [i+1]

        if i*2 <= N and cache[i*2] > cache[i] + 1:
            cache[i*2] = cache[i] + 1
            path[i*2] = path[i] + [i*2]

        if i*3 <= N and cache[i*3] > cache[i] + 1:
            cache[i*3] = cache[i] + 1
            path[i*3] = path[i] + [i*3]

    path[N].reverse()
    print(cache[N])
    print(*path[N])


if __name__ == "__main__":
    solution()
