import sys


def solution():
    """ NlogN (N: 250,000)
    idea: prefix sum
        - max sum of sub array
        - same as sliding window
            - then, do not use the slicing (deep copy of 1d array)
    """
    # init data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # prefix sum with sliding window
    end, cache = M, 1
    answer = sum(arr[:end])
    curr = answer
    for i in range(1, N-M+1):
        cnt = curr - arr[i-1]
        cnt += arr[i+M-1]
        if cnt > answer:
            answer = cnt
            cache = 1

        elif cnt == answer:
            cache += 1

        curr = cnt

    if not answer:
        print("SAD")
    else:
        print(answer)
        print(cache)


if __name__ == "__main__":
    solution()
