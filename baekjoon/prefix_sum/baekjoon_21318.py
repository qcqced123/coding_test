import sys


def solution():
    """
    idea: prefix sum
        - 1차원 배열의 누적합 변형
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    prefix = [0] * (N + 1)
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(int(input()))]

    # init prefix sum array
    src = arr[0]
    init_ = 0
    for i in range(1, N):
        cnt = arr[i]
        if cnt < src:
            init_ += 1
        src = cnt

    prefix[0] = init_
    for i in range(1, N):
        src = arr[i-1]
        cnt = arr[i]
        if cnt < src:
            init_ -= 1

        prefix[i] = init_

    # answering the question
    for query in queries:
        l, r = query
        print(prefix[l-1] - prefix[r-1])


if __name__ == "__main__":
    solution()
