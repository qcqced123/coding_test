import sys
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """
    # get input data
    cache = defaultdict(int)
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # do prefix sum with hash
    cnt = 0
    answer = 0
    cache[0] = 1
    for i in range(N):
        cnt += arr[i]
        curr = cache[cnt-K]
        if curr:
            answer += curr

        cache[cnt] += 1

    print(answer)

if __name__ == '__main__':
    solution()