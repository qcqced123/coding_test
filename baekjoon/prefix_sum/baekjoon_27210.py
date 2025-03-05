import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum + hash
    """
    N = int(input())
    arr = list(map(int, input().split()))

    # init the hash, prefix array
    cache = {
        1: 0,
        2: 0
    }
    prefix = [0]*(N+1)
    for i in range(1, N+1):
        cnt = arr[i-1]
        cache[cnt] += 1
        prefix[i] = abs(cache[1] - cache[2])

    print(max(prefix))


if __name__ == "__main__":
    solution()
