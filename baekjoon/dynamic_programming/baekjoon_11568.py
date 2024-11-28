import sys


def solution():
    """
    idea: dynamic programming
        - 가장 긴 증가하는 부분 수열
        - 입력 길이가 짧아서, N**2으로 풀어도 괜찮음
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [1]*N
    arr = list(map(int, input().split()))

    # update the cache
    for i in range(1, N):
        cnt = arr[i]
        for j in range(i):
            if cnt > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)

    print(max(cache))


if __name__ == "__main__":
    solution()
