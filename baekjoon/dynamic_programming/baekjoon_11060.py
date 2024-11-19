import sys


def solution():
    """ N**3
    idea: bfs, dynamic programming
        -
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    cache = [INF]*N

    # do update the dp cache
    cache[0] = 0
    for i in range(N):
        cnt = arr[i]
        for j in range(1, cnt+1):
            if i + j < N:
                cache[i+j] = min(cache[i+j], cache[i]+1)

    print(cache[-1]) if cache[-1] != INF else print(-1)


if __name__ == "__main__":
    solution()
