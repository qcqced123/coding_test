import sys


def solution():
    """ QlogN, 비내림차순 배열
    idea: prefix sum
        - sorting
        - init prefix array (1D Array)
    """
    # init data structure
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    # init prefix array
    prefix = [0]*(N+1)
    init_ = sum(arr)
    prefix[0] = init_
    for i in range(1, N+1):
        init_ -= arr[i-1]
        prefix[i] = init_

    # answering the question
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    for query in queries:
        l, r = query
        print(prefix[l-1] - prefix[r])


if __name__ == "__main__":
    solution()
