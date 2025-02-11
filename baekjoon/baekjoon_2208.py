import sys


def solution():
    """
    idea: sliding window with prefix sum
        - do sliding window with fixed size
        - find the additional element for fixed window

    limit: NlogN
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # do sliding window with fixed size window
    cache = [0]*(N-M+1)
    for i in range(N-M+1):
        cache[i] = sum(arr[i:i+M])

    # init prefix sum array
    prefix = [0]*N
    prefix[0] = sum(arr)
    for i in range(1, N):
        prefix[i] = prefix[i-1] - arr[i-1]

    # find the additional element



if __name__ == "__main__":
    solution()
