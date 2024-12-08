import sys
from bisect import bisect_left


def solution():
    """ QlogN
    idea: prefix sum with bisect
        - initialize prefix array
        - find query's index in arr
        - get answer by using index and prefix array
    """
    # get data
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [int(input()) for _ in range(Q)]
    arr.sort()

    # init prefix array
    prefix = [0]*N
    prefix[0] = sum(arr)
    for i in range(1, N):
        prefix[i] = prefix[i-1] - arr[i-1]

    # do bisect and answering the question
    for query in queries:
        answer = 0
        idx = bisect_left(arr, query)
        if idx < N:
            answer += abs(query*idx - (prefix[0] - prefix[idx])) + abs(query*(N-idx) - prefix[idx])
        else:
            answer += query*N - prefix[0]
        print(answer)


if __name__ == "__main__":
    solution()
