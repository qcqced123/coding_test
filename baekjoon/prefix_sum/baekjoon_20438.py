import sys


def solution():
    """
    idea: prefix sum

반례:
50 4 5 2
24 15 27 43
3 4 6 20 25
3 25
26 52
    """
    # init data structure
    input = sys.stdin.readline
    N, K, Q, M = map(int, input().split())
    sleeper = set(map(int, input().split()))
    arr = set(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    # init cache array
    cache = [0]*(N+3)
    for q in arr-sleeper:
        for i in range(q, N+3, q):
            if i not in sleeper:
                cache[i] = 1

    # init prefix array
    prefix = [0]*(N+3)
    for i in range(3, N+3):
        if not cache[i]:
            prefix[i] = prefix[i-1] + 1
        else:
            prefix[i] = prefix[i-1]

    # answering the question
    for query in queries:
        l, r = query
        print(prefix[r]-prefix[l-1])


if __name__ == "__main__":
    solution()
