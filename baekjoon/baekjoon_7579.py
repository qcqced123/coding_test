import sys


def solution():
    """ In-memory, In-Active Algorithm
    idea: Dynamic Programming
        1) 비용 기준, 용량 계산
            - 행: 용량
            - 열: 비용
    """
    N, M = map(int, sys.stdin.readline().split())  # number of apps, need
    memory = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))

    # initialize the cache array
    # zip the memory and cost array, sorting by ascending
    col_size = sum(cost)+1
    cache = [[0]*col_size for _ in range(N+1)]
    arr = [(m, c) for m, c in zip(memory, cost)]
    arr.sort()

    # do dynamic programming search
    result = sys.maxsize
    for y in range(1, N+1):
        for x in range(col_size):
            cnt_memory, cnt_cost = arr[y-1]
            if x < cnt_cost:
                cache[y][x] = max(cache[y-1][x], cache[y][x])

            else:
                cache[y][x] = max(cache[y-1][x-cnt_cost]+cnt_memory, cache[y-1][x], cache[y][x])
                if cache[y][x] >= M:  # update the minimum cost
                    result = min(result, x)
    print(result)


if __name__ == "__main__":
    solution()
