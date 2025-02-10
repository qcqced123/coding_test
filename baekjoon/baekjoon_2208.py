import sys


def solution():
    """
    idea: prefix sum
        - initialize the 1D prefix array
        -
    limit: NlogN
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    print(arr)

    # init prefix sum array
    prefix = [0]*N
    prefix[0] = sum(arr)
    for i in range(1, N):
        prefix[i] = prefix[i-1] - arr[i-1]



if __name__ == "__main__":
    solution()
