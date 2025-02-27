import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum + hash
    limit: NlogN
    """
    # get input data
    size = 10**6
    N = int(input())
    prefix = [0]*(size+2)  # 여기 바꾸기

    # init prefix sum array
    for _ in range(N):
        src, end = map(int, input().split())
        prefix[src] += 1
        prefix[end+1] -= 1

    Q = int(input())

    # do prefix sum
    cnt = 0
    queries = list(map(int, input().split()))
    cache = {k: 0 for k in queries}
    for i in range(1, size+2):
        cnt += prefix[i]
        if i in cache:
            cache[i] = cnt

    # answering the question
    for i in queries:
        print(cache[i], end="\n")

if __name__ == "__main__":
    solution()
