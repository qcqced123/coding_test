import sys
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix
        -
    """
    # get input data
    metro = defaultdict(list)
    N, M = map(int, input().split())  # city, day
    arr = list(map(int, input().split()))

    # update the prefix
    k = 1
    prefix = [0]*(N+1)
    for i in range(M-1):
        l, r = min(arr[i], arr[i+1]), max(arr[i], arr[i+1])
        prefix[l] += k
        prefix[r] -= k

    # init metro dictionary
    for i in range(1, N):
        cnt = list(map(int, input().split()))
        metro[i].extend(cnt)

    # do prefix sum
    cnt = 0
    answer = 0
    for i in range(1, N):
        cnt += prefix[i]
        ticket, ic, card = metro[i]
        answer += min(ticket*cnt, card+ic*cnt)

    print(answer)


if __name__ == "__main__":
    solution()
