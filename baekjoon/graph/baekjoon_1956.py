import sys


def solution():
    """ 유향 그래프, 사이클 찾기, 최소 경로(사이클) 찾기, N**3
    사이클: 출발지 to 출발지

    idea: graph, floyd warshall
        - 플루이드 워셜 수행
        - k to j, j to k가 최소인 경로 찾기

    feedback:
        - 플루이드 워셜로 풀면 python3에서 시간초과
        - 찾아 보니까 풀루이드 워셜은 pypy3만 가능하다고 함
        - 다익스트라 두 번 써도 되겠네 근데
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    V, E = map(int, input().split())
    cache = [[INF]*(V+1) for _ in range(V+1)]

    # init the cache
    for _ in range(E):
        src, end, cost = map(int, input().split())
        cache[src][end] = cost

    # do the floyd-warshall (dynamic programming)
    for k in range(1, V+1):
        for y in range(1, V+1):
            for x in range(1, V+1):
                if y != x:
                    cache[y][x] = min(cache[y][x], cache[y][k] + cache[k][x])  # 경유 하는게 빠른가, 직접 가는게 빠른가

    # find the minimum cost of cycle
    answer = INF
    for y in range(1, V+1):
        for x in range(1, V+1):
            if cache[y][x] != INF:
                answer = min(answer, cache[y][x]+cache[x][y])

    print(answer if answer != INF else -1)


if __name__ == "__main__":
    solution()
