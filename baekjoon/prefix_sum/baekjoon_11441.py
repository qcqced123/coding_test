import sys


def solution():
    """ QlogN (Q: 100,000, N: 100,000)
    idea: prefix sum
        - prefix[i]: sum of staring at i-th index's sub array
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    prefix = [0]*N
    queries = [tuple(map(int, input().split())) for _ in range(int(input()))]

    # update the prefix sum array
    prefix[0] = sum(arr)
    for i in range(1, N):
        prefix[i] += prefix[i-1] - arr[i-1]

    # answering the question
    for query in queries:
        l, r = query
        if r == N: print(prefix[l-1])
        else: print(prefix[l-1] - prefix[r])


if __name__ == "__main__":
    solution()
