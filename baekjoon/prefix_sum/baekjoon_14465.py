import sys


def solution():
    """ NlogN (N: 100,000)
    1 2 3 4 5 6 7 8 9 10
    1 2     5       9 10
    idea: sliding window
        - record broken position
        - calculate the broken positions in sub array(sliding window)
        - arr[i]: normal or broken
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    N, K, B = map(int, input().split())

    # init data structure
    arr = [0]*(N+1)
    for _ in range(B):
        arr[int(input())] = 1

    # sliding window
    answer = sum(arr[1:1+K])
    curr = answer
    for i in range(2, N-K+2):
        cnt = curr - arr[i-1]
        cnt += arr[i+K-1]
        if cnt < answer:
            answer = cnt

        curr = cnt

    print(answer)


if __name__ == "__main__":
    solution()
