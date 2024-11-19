import sys


def solution():
    """ 거리의 최소값
    최소 거리 = min(일반 경로, 지름길 사용 경로)
    idea: dynamic programming
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 지름길 개수, 고속도로 길이
    shortest = [tuple(map(int, input().split())) for _ in range(N)]
    cache = [INF]*(M+1)

    # update the dp cache
    cache[0] = 0
    for i in range(M+1):
        if i > 0:
            cache[i] = min(cache[i], cache[i-1]+1)

        for j in range(N):
            src, end, cost = shortest[j]
            if src == i and end <= M:
                cache[end] = min(cache[src] + cost, cache[end])

    print(cache[M])


if __name__ == "__main__":
    solution()
